<?php

/**
 * LotteryHandler.class.php
 * 根据配置的抽奖概率，计算、返回用户所中奖项
 */

class LotteryHandler {

    private $_prizeConf     = array();  // 奖项/概率设置
    private $_uid           = '';       // 用户标识
    private $_link;
    /**
     * 实例化属性
     */
    public function __construct($config, $uid) {
        $this->_link = new SaeMysql();
        if (!empty($config) && is_array($config)) {
            $this->_prizeConf = $config;
        }
        $this->_uid = $uid;
    }

    /**
     * 查看用户是否有抽奖资格
     * @return boolean
     */
    public function hasChance() {
        $sql = "SELECT * FROM `weixin_lottery_record` WHERE uid= '".$this->_uid."'";
        $data = $this->_link->getData($sql);
      // $data = DbPDO::table('weixin_lottery_record')->where(array('uid'=>$this->_uid))->find();
        if(!$data) {
            return true; // 有抽奖资格
        }
        return false;
    }

    /**
     * 完成抽奖动作，返回抽奖结果
     * @return array 抽奖结果
     */
    public function getLoterry() {

        $tmpArr = array();
        $prizeId = '';

        // 根据配置文件，建立奖项与概率的对应
        foreach ($this->_prizeConf as $k => $v) {
            $tmpArr[$v['id']] = $v['v'];
        }

        // 根据奖项概率及对应奖项的已中奖人数，获取用户最后所获得的奖项
        do {
            $prizeId = $this->_getPrizeId($tmpArr); // 获取奖项id
            $sql = "SELECT * FORM `weixin_lottery_record` WHERE pid = ".$prizeId;
            $data = $this->_link->getData($sql);
            //$data = DbPDO::table('weixin_lottery_record')->where(array('pid'=>$prizeId))->find(); // 查询已获取当前奖项的人数
            $nums = !empty($data) ? count($data) : 0;
        } while($nums >= $this->_prizeConf[$prizeId-1]['num']);

        //$prizeId = $this->_getPrizeId($tmpArr); // 奖项id
        //$angle = $this->_getRotation($this->_prizeConf[$prizeId-1]); // 旋转角度

        // 存储用户中奖记录
        /*
        DbPDO::table('weixin_lottery_record')->add(array(
            'uid'   => $this->_uid,
            'pid'   => $prizeId,
            'prize' => $this->_prizeConf[$prizeId-1]['prize'],
            'ltime' => time()
        ));
         */
        $uid = $this->_uid;
        $prize = $this->_prizeConf[$prizeId-1]['prize'];
        $time = time();
        //$sql = "INSERT INTO `weixin_lottery_record` (`uid`, `pid`, `prize`, `ltime`) VALUES (".$this->_uid.", $prizeId, ".$this->_prizeConf[$prizeId-1]['prize'].",".time());
        $sql = "INSERT INTO `weixin_lottery_record` (`uid`, `pid`, `prize`, `ltime`) VALUES ('{$uid}', {$prizeId}, '{$prize}', {$time})";
        $this->_link->runSql($sql);

        return array('prize'=>$prizeId);
    }

    /**
     * 根据概率获取奖项ID
     * @param  [type] $arr [description]
     * @return [type]         [description]
     */
    private function _getPrizeId($arr) {

        $prizeId = ''; // 最终的中奖标识id
        $proSum = array_sum($arr); // 概率数组的总概率精度

        // 概率数组循环
        foreach ($arr as $key => $proCur) {
            $randNum = mt_rand(1, $proSum);
            if ($randNum <= $proCur) {
                $prizeId = $key;
                break;
            } else {
                $proSum -= $proCur;
            }
        }
        unset ($arr);

        return $prizeId;
    }

    /**
     * 根据所中奖项，获取旋转角度
     * ----- 当前未启用，角度由前端直接控制，当前类只是根据概率返回中奖id -----
     * @param  array $arr 中得的奖项数组
     * @return int 旋转角度
     */
    private function _getRotation($arr) {

        $resultArr = array();
        $min = $arr['min'];
        $max = $arr['max'];

        if ($arr['id'] == 4){ // 谢谢参与奖
            $i = mt_rand(0, 5);
            $resultArr['angle'] = mt_rand($min[$i], $max[$i]);
        } else {
            $resultArr['angle'] = mt_rand($min, $max); //随机生成一个角度
        }

        return $resultArr;
    }
}
