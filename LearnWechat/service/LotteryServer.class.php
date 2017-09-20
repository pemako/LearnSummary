<?php
/**
 *
 */
class LotteryServer {

    public $prizeArr = array();
    public $uid = '';

    /**
     * 查看抽奖资格
     * @return boolean
     */
    public function hasChance() {
        $db = new DbConn();
        if(!$db->findByUid($this->uid)) {
            return true; // 有资格抽奖
        }
        return false;
    }

    /**
     * 根据概率获取奖项ID
     * @param  [type] $arr [description]
     * @return [type]         [description]
     */
    private function getPrizeId($arr) {

        $prizeId = ''; // 奖项ID

        // 概率数组的总概率精度
        $proSum = array_sum($arr);

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
     * 完成抽奖动作，返回抽奖结果
     * @return array 抽奖结果
     */
    public function loterry() {

        $tmpArr = array();
        $db = new DbConn();

        foreach ($this->prizeArr as $k => $v) {
            $tmpArr[$v['id']] = $v['v'];
        }

        do {
            $prizeId = $this->getPrizeId($tmpArr); // 奖项id
            $nums = $db->countByPid($prizeId); // 查询已获取当前奖项的人数
        } while($nums >= $this->prizeArr[$prizeId-1]['num']);

        //$prizeId = $this->getPrizeId($tmpArr); // 奖项id
        //$angle = $this->getRotation($this->prizeArr[$prizeId-1]); // 旋转角度

        // 插入数据库，记录用户中奖情况
        $db->add($this->uid, $prizeId, $this->prizeArr[$prizeId-1]['prize'], time());

        return array('prize'=>$prizeId);
    }

    /**
     * 根据所中奖项，获取旋转角度（---------未启用--------角度由前端直接控制，本类只是根据概率返回中奖id）
     * @param  array $arr 中得的奖项数组
     * @return int 旋转角度
     */
    private function getRotation($arr) {

        $resultArr = array();

        //$resultArr['prize'] = $arr['id'];
        $min = $arr['min'];
        $max = $arr['max'];
        if($arr['id']==4){ // 谢谢参与奖金
            $i = mt_rand(0,5);
            $resultArr['angle'] = mt_rand($min[$i],$max[$i]);
        }else{
            $resultArr['angle'] = mt_rand($min,$max); //随机生成一个角度
        }

        return $resultArr;
    }
}
