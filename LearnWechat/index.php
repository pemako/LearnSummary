<?php

// 定义项目根目录
defined('APP_BASE') or define('APP_BASE', __DIR__ . DIRECTORY_SEPARATOR);

// 加载全局配置文件和自动加载类
require_once( APP_BASE . 'service/conf/main.conf.php');
require_once( APP_BASE . 'service/common/Curl.class.php');
//require_once( APP_BASE . 'service/common/DbPDO.class.php');
require_once( APP_BASE . 'service/common/AccessToken.class.php');
require_once( APP_BASE . 'service/Response.class.php');
require_once( APP_BASE . 'service/ResponseHandler.class.php');

$rServer = new Response();

if (isset($_GET['echostr'])) {
    $rServer->checkRequest(); // 用于第一次绑定域名时的验证
} else {
    $rServer->responseRequest(); // 响应用户请求入口
}
