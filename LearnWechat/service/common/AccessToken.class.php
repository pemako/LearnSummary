<?php

/**
 * 主要用于检测access_token的有效性/获取新的access_token。
 * 关于access_token：
 * - 是公众号的全局唯一票据，公众号调用各接口时都需使用access_token。
 * - 有效期目前为2个小时。
 * 参照：http://mp.weixin.qq.com/wiki/11/0e4b294685f817b95cbed85ba5e82b8f.html
 */
class AccessToken {

    const VALID_TIME = 7200;
    private $_apiUrl = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s';
    private $_accessToken = null;

    /**
     * 检测、返回有效的access_token
     * @return string
     */
    public function get() {

        // 检查access_token有效性
        $accessToken = $this->_check();
        if (!$accessToken['isvalid']) {
            try { // 重新获取新的access_token
                $this->_accessToken = $this->_getNewAccessToken();
            } catch (Exception $e) {
                die('Get access_token failed: ' . $e->getMessage());
            }
        } else {
            $this->_accessToken = $accessToken['t_value'];
        }

        return $this->_accessToken;
    }

    /**
     * 根据时间戳，判断存储的access_token是否有效
     * @return array
     */
    private function _check() {
        try {
            $mysql = new SaeMysql();
            $sql = "SELECT `c_time`, `t_value` FROM `weixin_access_token`";
            $data = $mysql->getData($sql);
            $mysql->closeDb();

            //$data = DbPDO::table('weixin_access_token')->field(array('c_time', 't_value'))->find();
            if($data) {
                $now = time();
                if (($now - $data[0]['c_time']) < self::VALID_TIME) { // 有效
                    return array('isvalid'=>true, 't_value'=>$data[0]['t_value']);
                } else { // 无效
                    return array('isvalid'=>false);
                }
            } else { // 还没有存储access_token
                return array('isvalid'=>false);
            }
        } catch (Exception $e) {
            throw new Exception($e->getMessage());
        }
    }

    /**
     * 调用微信接口，重新获取access_token
     * @return  string
     */
    private function _getNewAccessToken() {

        // 获取新的access_token
        $apiUrl = sprintf($this->_apiUrl, APP_ID, APP_SECRET);
        $newAccessToken = Curl::doCurl($apiUrl);

        // 判断是否获取成功
        if(!$newAccessToken['errcode'] && !empty($newAccessToken['access_token'])) {

            // 将新获取的access_token更新到数据库
            $c_time = time() - 200; // 将获取到的时间提前一点
            $mysql = new SaeMysql();
            $sql = "SELECT `c_time`, `t_value` FROM `weixin_access_token`";
            $data = $mysql->getData($sql);
			//$data = DbPDO::table('weixin_access_token')->find();
			if(!$data){
				// 首次插入
				//DbPDO::table('weixin_access_token')->where(array('id'=>1))->add(array('c_time' => $c_time, 't_value' => $newAccessToken['access_token']));
                $sql = "INSERT INTO `weixin_access_token` (`c_time`, `t_value`) VALUES ($c_time, ".$newAccessToken['access_token'].")";
            } else {
				// 修改
				//DbPDO::table('weixin_access_token')->where(array('id'=>1))->save(array('c_time' => $c_time, 't_value' => $newAccessToken['access_token']));
                $sql = "UPDATE `weixin_access_token` SET `c_time` = $c_time , `t_value` = ". $newAccessToken['access_token']. " WHERE id = 1";
			}
            $mysql->runSql($sql);
            $mysql->closeDb();
        } else {
            throw new Exception($newAccessToken['errcode'] . '-' . $newAccessToken['errmsg']);
        }

        return $newAccessToken['access_token'];
    }
}

