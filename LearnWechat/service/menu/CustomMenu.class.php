<?php

/**
 * 自定义菜单完成添加、查询、删除功能
 */

class CustomMenu {

	private $_accessToken = ''; // 当前公共号的全局唯一票据

	/**
	 * 初始化获取 可用的token值
	 */
	public function __construct(){
		// 获取access_token 
		$objAccessToken = new AccessToken();
		$this->_accessToken = $objAccessToken->get();
	}

	/**
	 * 创建菜单
	 * URL  https://api.weixin.qq.com/cgi-bin/menu/create?access_token=ACCESS_TOKEN
	 * data json string
	 */
	public function create($jsonMenuinfo){
		$createApiUrl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=".$this->_accessToken;
		$result = Curl::doCurl($createApiUrl, $jsonMenuinfo);
		if($result['errcode'] == 0 && $result['errmsg'] == 'ok') {
            echo json_encode(array('code'=>2000, 'message'=>'The menu is successfully created！'));
        } else {
            die('Create menu failed: ' . $result['errcode'] . '-' . $result['errmsg']);
        }
	}
	
	
	/**
	 * 删除菜单
	 * URL https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=ACCESS_TOKEN
	 */
	public function delete(){
		$deleteApiUrl = "https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=".$this->_accessToken;
		// 调用接口删除
		$result = Curl::doCurl($deleteApiUrl);
		if($result['errcode'] == 0 && $result['errmsg'] == 'ok'){
			echo json_encode(array('code'=>2000,'message'=>'delete success'));			
		} else {
			die('Delete menu faield:'. $result['errcode'] . '-' .$result['errmsg']);
		}
	}

	/**
	 * 查询已设置的菜单
	 * URL https://api.weixin.qq.com/cgi-bin/menu/get?access_token=ACCESS_TOKEN
	 */
	public function query(){
		$queryApiUrl = "https://api.weixin.qq.com/cgi-bin/menu/get?access_token=".$this->_accessToken;
		$result = Curl::doCurl($queryApiUrl);
		return $result;
	}

	
	/**
	 * 获取自定义菜单配置接口
	 * URL https://api.weixin.qq.com/cgi-bin/get_current_selfmenu_info?access_token=ACCESS_TOKEN
	 */
	public function config(){
		$queryApiUrl = "https://api.weixin.qq.com/cgi-bin/get_current_selfmenu_info?access_token=".$this->_accessToken;
		$result = Curl::doCurl($queryApiUrl);
		return $result;
	}
}

include_once '../conf/main.conf.php';
include_once '../common/AccessToken.class.php';
include_once '../common/Curl.class.php';
//include_once '../common/DbPDO.class.php';
$jsonMenuinfo = include('../conf/menu.conf.php');

$obj = new CustomMenu();

//print_r( $obj->query());
//print_r( $obj->query());
print_r( $obj->delete());
//print_r( $obj->create($jsonMenuinfo));

