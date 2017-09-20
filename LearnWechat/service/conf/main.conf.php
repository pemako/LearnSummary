<?php

/**
 * 针对当前公共号的一些共用配置文件
 */

// 自定义token
defined('TOKEN') or define('TOKEN', 'weixin2');

// 开发者ID，从当前公众号的开发者中获取
defined('APP_ID') or define('APP_ID', '**');
defined('APP_SECRET') or define('APP_SECRET', '**');


// 数据库配置
defined('DB_DSN') or define('DB_DSN', 'mysql:dbname=weixin;host=127.0.0.1');
defined('DB_USER') or define('DB_USER', '**');
defined('DB_PWD') or define('DB_PWD', '***');
defined('DB_TB_PREFIX') or define('DB_TB_PREFIX', '');
