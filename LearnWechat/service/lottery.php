<?php

// 加载配置文件和要使用的类文件
require_once('./conf/main.conf.php');
require_once('./LotteryHandler.class.php');
//require_once('./common/DbPDO.class.php');
$config = require_once('./conf/prize.conf.php');

if (!empty($_GET['uid'])) {

    // 获取用户标识ump($config);exit;
    $uid = trim($_GET['uid']);

    // 获取奖项
    $lott = new LotteryHandler($config, $uid);
    if ($lott->hasChance()) {
       echo json_encode($lott->getLoterry());
    } else { // 抽过奖了
        echo json_encode(array('prize'=>0));
    }
} else {
    echo json_encode(array('code'=>400, 'message'=>'Invalid parameter OpenUDID!'));
    exit;
}
