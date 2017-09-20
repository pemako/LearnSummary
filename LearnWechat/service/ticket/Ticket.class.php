<?php

/**
 * 生成带参数的二维码
 */

include_once '../common/AccessToken.class.php';
include_once '../common/Curl.class.php';
include_once '../common/DbPDO.class.php';
include_once '../conf/main.conf.php';

class Ticket {
	
	private $_accessToken = '';
	
	public function __construct(){
		$objAccessToken = new AccessToken();
		$this->_accessToken = $objAccessToken->get();
	}
	
	/**
	 * 二维码请求说明
	 * http请求方式: POST
	 * URL: https://api.weixin.qq.com/cgi-bin/qrcode/create?access_token=TOKEN
	 * POST数据格式：json
	 * 
	 * 临时二维码参数格式
	 * POST数据例子：{"expire_seconds": 1800, "action_name": "QR_SCENE", "action_info": {"scene": {"scene_id": 123}}}
	 * 
	 * 永久二维码参数格式
	 * POST数据例子：{"action_name": "QR_LIMIT_SCENE", "action_info": {"scene": {"scene_id": 123}}}
	 * 或者也可以使用以下POST数据创建字符串形式的二维码参数：
	 * {"action_name": "QR_LIMIT_STR_SCENE", "action_info": {"scene": {"scene_str": "123"}}}
	 * 
	 * 参数说明
	 * expire_seconds	该二维码有效时间，以秒为单位。 最大不超过1800。
	 * action_name	二维码类型，QR_SCENE为临时,QR_LIMIT_SCENE为永久,QR_LIMIT_STR_SCENE为永久的字符串参数值
	 * action_info	二维码详细信息
	 * scene_id	场景值ID，临时二维码时为32位非0整型，永久二维码时最大值为100000（目前参数只支持1--100000）
	 * scene_str	场景值ID（字符串形式的ID），字符串类型，长度限制为1到64，仅永久二维码支持此字段
	 */
	function create($data){
		$url = "https://api.weixin.qq.com/cgi-bin/qrcode/create?access_token=".$this->_accessToken;
		$result = Curl::doCurl($url, $data);
		return $result;
	}
	
	/**
	 * 根据tiket的值换取 二维码
	 * HTTP GET请求（请使用https协议）
	 * https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=TICKET
	 * 提醒：TICKET记得进行UrlEncode
	 */
	function getCode($ticket){
		$url = "https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=".urlencode($ticket);
		return $url;
	}
	
	/**
	 * 组装需要下载二维码信息
	 */
	function downLoadFile($url){
		$ch = curl_init($url);
		curl_setopt($ch, CURLOPT_HEADER, 0);
		curl_setopt($ch, CURLOPT_NOBODY, 0);    //只取body头
		curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
		curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, FALSE);
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
		$package = curl_exec($ch);
		$httpinfo = curl_getinfo($ch);
		curl_close($ch);
		return array_merge(array('body' => $package), array('header' => $httpinfo));
	}
}

$obj = new Ticket();
//$data = '{"expire_seconds": 1800, "action_name": "QR_SCENE", "action_info": {"scene": {"scene_id": 10000}}}';
// 永久
$data = '{"action_name": "QR_LIMIT_SCENE", "action_info": {"scene": {"scene_id": 1000}}}';

// 获取ticket
$ticket = $obj->create($data); 
$ticket = $ticket['ticket'];

// 获取二维码的地址
$info = $obj->getCode($ticket);

echo "<img src=$info>";

$imageInfo = $obj->downLoadFile($info);
// var_dump($imageInfo);
// 把图片信息写入到文件中
$filename = "qrcode.jpg";
$local_file = fopen($filename, 'wr');
if (false !== $local_file){
	if (false !== fwrite($local_file, $imageInfo["body"])) {
		fclose($local_file);
	}
}

