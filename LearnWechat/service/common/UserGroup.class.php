<?php

/**
 * 开发者可以使用接口，对公众平台的分组进行查询、创建、修改、删除等操作，也可以使用接口在需要时移动用户到某个分组。
 ***/

include_once('./AccessToken.class.php');
include_once('./Curl.class.php');
include_once('./DbPDO.class.php');

class UserGroup {

	private $_accessToken = '';

	public function __construct(){
		$objAccessToken = new AccessToken();
		$this->_accessToken = $objAccessToken->get();
	}

	/**
	 * 创建分组
	 * 一个公众账号，最多支持创建100个分组。
	 * @param data json格式 name:分组的名称
	 */	
	public function create($data){
		$url = 'https://api.weixin.qq.com/cgi-bin/groups/create?access_token='.$this->_accessToken;
		$result = Curl::doCurl($url, $data);
		return $result;
	}


	/**
	 * 查看所有分组
	 */
	public function query(){
		$url = 'https://api.weixin.qq.com/cgi-bin/groups/get?access_token='.$this->_accessToken;
		$result = Curl::doCurl($url);
		return $result;
	}


	/**
	 * 查询用户所在分组
	 * 通过用户的OpenID查询其所在的GroupID。 接口调用请求说明
	 * http请求方式: POST（请使用https协议）
	 * https://api.weixin.qq.com/cgi-bin/groups/getid?access_token=ACCESS_TOKEN
	 * POST数据格式：json
	 * POST数据例子：{"openid":"od8XIjsmk6QdVTETa9jLtGWA6KBc"}
	 * @return groupId
	 */
	public function queryUser($data){
		$url = 'https://api.weixin.qq.com/cgi-bin/groups/getid?access_token='.$this->_accessToken;
		$result = Curl::doCurl($url, $data);
		return $result;
	}


	/**
	 * 修改分组名
	 * http请求方式: POST（请使用https协议）
	 * https://api.weixin.qq.com/cgi-bin/groups/update?access_token=ACCESS_TOKEN
	 * POST数据格式：json
	 * POST数据例子：{"group":{"id":108,"name":"test2_modify2"}}
	 */

	public function update($data){
		$url = 'https://api.weixin.qq.com/cgi-bin/groups/update?access_token='.$this->_accessToken;
		$result = Curl::doCurl($url, $data);
		return $result;
	}


	/**
	 * 移动用户分组
	 * https://api.weixin.qq.com/cgi-bin/groups/members/update?access_token=ACCESS_TOKEN
	 * POST数据格式：json
	 * POST数据例子：{"openid":"oDF3iYx0ro3_7jD4HFRDfrjdCM58","to_groupid":108}
	 **/

	public function move($data){
		$url = 'https://api.weixin.qq.com/cgi-bin/groups/members/update?access_token='.$this->_accessToken;
		$result = Curl::doCurl($url, $data);
		return $result;
	}

	/**
	 * 批量移动用户分组
	 * https://api.weixin.qq.com/cgi-bin/groups/members/batchupdate?access_token=ACCESS_TOKEN
	 * POST数据格式：json
	 * POST数据例子：{"openid_list":["oDF3iYx0ro3_7jD4HFRDfrjdCM58","oDF3iY9FGSSRHom3B-0w5j4jlEyY"],"to_groupid":108}
	 **/

	public function moveBatch($data){
		$url = 'https://api.weixin.qq.com/cgi-bin/groups/members/batchupdate?access_token='.$this->_accessToken;
		$result = Curl::doCurl($url, $data);
		return $result;
	}


	/**
	 * 注意本接口是删除一个用户分组，删除分组后，所有该分组内的用户自动进入默认分组。 接口调用请求说明
	 * http请求方式: POST（请使用https协议）
	 * https://api.weixin.qq.com/cgi-bin/groups/delete?access_token=ACCESS_TOKEN
	 * POST数据格式：json
	 * POST数据例子：{"group":{"id":108}}
	 **/
	public function delete($data){
		$url = 'https://api.weixin.qq.com/cgi-bin/groups/delete?access_token='.$this->_accessToken;
		$result = Curl::doCurl($url, $data);
		return $result;
	}
}


$obj = new UserGroup();

// $data = '{"openid":"okw2Sjs5K8PGKpRQVivN9hicdBog"}';
// print_r($obj->queryUser($data));


// $data = '{"group":{"id":101, "name":"demo1"}';
// print_r($obj->update($data));




// $data = '{"openid":"okw2Sjs5K8PGKpRQVivN9hicdBog", "to_groupid":1}';
// print_r($obj->move($data));


// $data = '{"openid_list":["okw2Sjjt_TOo9k4Y7m8kpvWQs74U","okw2Sju8POyk1D682fveTLO7yGTg"], "to_groupid":1}';
// print_r($obj->moveBatch($data));

// print_r($obj->query());

$data = '{"group":{"id":101}}';

print_r($obj->delete($data));

