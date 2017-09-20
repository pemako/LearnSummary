<?php

/**
 *  微信中一些常用的方法
 *
 */

include_once('./AccessToken.class.php');
include_once('./Curl.class.php');
include_once('./DbPDO.class.php');

class Util {

	private $_accessToken = '';

	public function __construct(){
		//获取accessToken
		$objAccessToken = new AccessToken();
		$this->_accessToken = $objAccessToken->get();
	}


	// 获取微信服务器IP地址
	public function getWechatServerIpList(){
		$url = 'https://api.weixin.qq.com/cgi-bin/getcallbackip?access_token='.$this->_accessToken;
		$result = Curl::doCurl($url);
		return $result['ip_list'];
	}


	/**
	 * 获取关注者列表
	 * 当公众号关注者数量超过10000时，可通过填写next_openid的值，从而多次拉取列表的方式来满足需求。
	 * 具体而言，就是在调用接口时，将上一次调用得到的返回中的next_openid值，作为下一次调用中的next_openid值。
	 * @param string next_openid
	 * @param string access_token
	 * @return Array
	 * @ total
	 * @ count
	 * @ array data['openid']
	 * @ next_openid
	 */
	public function getUserList(){
		// next_openid 不填默认从头开始拉取
		$url = 'https://api.weixin.qq.com/cgi-bin/user/get?access_token='.$this->_accessToken.'&next_openid=';
		$result = Curl::doCurl($url);
		return $result;
	}


	/**
	 * 设置用户备注名
	 * 开发者可以通过该接口对指定用户设置备注名，该接口暂时开放给微信认证的服务号
	 * http请求方式: POST（请使用https协议）
	 * https://api.weixin.qq.com/cgi-bin/user/info/updateremark?access_token=ACCESS_TOKEN
	 * POST数据格式：JSON
	 * POST数据例子：{"openid":"oDF3iY9ffA-hqb2vVvbr7qxf6A0Q","remark":"pangzi"}
	 */
	public function remarkUser($data){
		$url = 'https://api.weixin.qq.com/cgi-bin/user/info/updateremark?access_token='.$this->_accessToken;
		$result = Curl::doCurl($url,$data);
		return $result;
	}


	/**
	 * 获取用户基本信息
	 * 公众号可通过本接口来根据OpenID获取用户基本信息，包括昵称、头像、性别、所在城市、语言和关注时间
	 * http请求方式: GET
	 * https://api.weixin.qq.com/cgi-bin/user/info?access_token=ACCESS_TOKEN&openid=OPENID&lang=zh_CN
	 */
	public function getUserinfo($openid){
		$url = 'https://api.weixin.qq.com/cgi-bin/user/info?access_token='.$this->_accessToken.'&openid='.$openid.'&lang=zh_CN';
		$result = Curl::doCurl($url,$openid);
		return $result;
	}


	/**
	 * 获取用户地理位置
	 * 开通了上报地理位置接口的公众号，用户在关注后进入公众号会话时，会弹框让用户确认是否允许公众号使用其地理位置。
	 * 弹框只在关注后出现一次，用户以后可以在公众号详情页面进行操作。
	 */
	public function getUserLocation(){

	}
	
	/**
	 * 用户分析数据接口
	 * 1、接口侧的公众号数据的数据库中仅存储了2014年12月1日之后的数据，将查询不到在此之前的日期，即使有查到，也是不可信的脏数据；
	 * 2、请开发者在调用接口获取数据后，将数据保存在自身数据库中，即加快下次用户的访问速度，也降低了微信侧接口调用的不必要损耗。
	 * 
	 * 获取用户增减数据
	 * 最大时间跨度为7天
	 * 需要传递请求的时间格式为 json 字符串 { "begin_date": "2014-12-09", "end_date": "2015-12-14"}
	 * 
	 * 正常情况下返回信息
	 * ref_date			数据的日期
	 * user_source		用户的渠道，数值代表的含义如下：
	 * 		0代表其他 
	 * 		30代表扫二维码 
	 * 		17代表名片分享 
	 * 		35代表搜号码（即微信添加朋友页的搜索） 
	 * 		39代表查询微信公众帐号 
	 * 		43代表图文页右上角菜单
	 * new_user			新增的用户数量
	 * cancel_user		取消关注的用户数量，new_user减去cancel_user即为净增用户数量
	 * cumulate_user	总用户量
	 */
	
	public function getUserSummary($data){
		$url = 'https://api.weixin.qq.com/datacube/getusersummary?access_token='.$this->_accessToken;
		$result = Curl::doCurl($url, $data);
		return $result;
	}
	
	/**
	 * 获取累计用户数据 getusercumulate
	 * 最大时间跨度为7天
	 * URL https://api.weixin.qq.com/datacube/getusercumulate?access_token=ACCESS_TOKEN
	 * 
	 * 
	 */


	
	//创建菜单
	public function create_menu($data){
		$url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=".$this->access_token;
		$res = Curl::doCurl($url, $data);
		return $res;
	}
	
	//发送客服消息，已实现发送文本，其他类型可扩展
	public function send_custom_message($touser, $type, $data){
		$msg = array('touser' =>$touser);
		switch($type)
		{
			case 'text':
				$msg['msgtype'] = 'text';
				$msg['text']    = array('content'=>urlencode($data));
				break;
		}
		$url = "https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token=".$this->access_token;
		return Curl::doCurl($url, urldecode(json_encode($msg)));
	}
	
	//生成参数二维码
	public function create_qrcode($scene_type, $scene_id){
		switch($scene_type)
		{
			case 'QR_LIMIT_SCENE': //永久
				$data = '{"action_name": "QR_LIMIT_SCENE", "action_info": {"scene": {"scene_id": '.$scene_id.'}}}';
				break;
			case 'QR_SCENE':       //临时
				$data = '{"expire_seconds": 1800, "action_name": "QR_SCENE", "action_info": {"scene": {"scene_id": '.$scene_id.'}}}';
				break;
		}
		$url = "https://api.weixin.qq.com/cgi-bin/qrcode/create?access_token=".$this->access_token;
		$result = Curl::doCurl($url, $data);
		return "https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=".urlencode($result["ticket"]);
	}
	
	//创建分组
	public function create_group($name){
		$data = '{"group": {"name": "'.$name.'"}}';
		$url = "https://api.weixin.qq.com/cgi-bin/groups/create?access_token=".$this->access_token;
		$res = Curl::doCurl($url, $data);
		return $res;
	}
	
	//移动用户分组
	public function update_group($openid, $to_groupid){
		$data = '{"openid":"'.$openid.'","to_groupid":'.$to_groupid.'}';
		$url = "https://api.weixin.qq.com/cgi-bin/groups/members/update?access_token=".$this->access_token;
		$res = Curl::doCurl($url, $data);
		return $res;
	}
	
	//查询所有分组
	public function get_groups(){
		$url = "https://api.weixin.qq.com/cgi-bin/groups/get?access_token=".$this->access_token;
		$res = Curl::doCurl($url);
		return $res;
	}
	
	//上传多媒体文件(除图文)
	public function upload_media($type, $file){
		$data = array("media"  => "@".dirname(__FILE__).'\\'.$file);
		$url = "http://file.api.weixin.qq.com/cgi-bin/media/upload?access_token=".$this->access_token."&type=".$type;
		$res = Curl::doCurl($url, $data);
		return $res;
	}
	
	//上传图文消息素材
	public function upload_news($news){
		foreach ($news as &$item) {
			foreach ($item as $k => $v) {
				$item[$k] = urlencode($v);
			}
		}
	
		$data = array("articles"=>$news);
		$url = "https://api.weixin.qq.com/cgi-bin/media/uploadnews?access_token=".$this->access_token;
		$res = Curl::doCurl($url, urldecode(json_encode($data)));
		return $res;
	}
	
	//高级群发(根据分组)
	public function mass_send_group($groupid, $type, $data){
		$msg = array('filter' => array('group_id'=>$groupid));
		$msg['msgtype'] = $type;
	
		switch($type)
		{
			case 'text':
				$msg[$type] = array('content'=> $data);
				break;
			case 'image':
			case 'voice':
			case 'mpvideo':
			case 'mpnews':
				$msg[$type] = array('media_id'=> $data);
				break;
	
		}
		$url = "https://api.weixin.qq.com/cgi-bin/message/mass/sendall?access_token=".$this->access_token;
		$res = Curl::doCurl($url, json_encode($msg));
		return $res;
	}
	
	//地理位置逆解析
	public function location_geocoder($latitude, $longitude){
		$url = "http://api.map.baidu.com/geocoder/v2/?ak=B944e1fce373e33ea4627f95f54f2ef9&location=".$latitude.",".$longitude."&coordtype=gcj02ll&output=json";
		$result = Curl::doCurl($url);
		return $result["result"]["addressComponent"];
	}
	
}


$obj = new Util();

// $data = '{"openid":"okw2Sjjt_TOo9k4Y7m8kpvWQs74U", "remark":"刘洋"}';
// print_r($obj->remarkUser($data));

// $data = 'okw2Sjs5K8PGKpRQVivN9hicdBog';
// print_r($obj->getUserinfo($data));

// $data = '{ "begin_date": "2014-12-09", "end_date": "2015-12-14"}';

// print_r($obj->getUserSummary($data));



