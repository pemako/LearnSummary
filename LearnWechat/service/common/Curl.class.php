<?php

/**
 * 供curl调用操作
 */
class Curl {

    private static $_instance = null;
    private static $_curl = null;

    /**
     * [__construct description]
     * @param [type] $config [description]
     */
    public function __construct() {
        try {
            self::$_curl = curl_init();
        } catch (Exception $e) {
            throw new Exception("Can't init CURL!");
        }
    }

    /**
     * 阻止克隆对象
     */
    private function __clone() { }

    /**
     * 获取当前类实例
     * @return object
     */
    private static function getInstance() {
        if (!self::$_instance) {
            self::$_instance = new self();
        }
        return self::$_instance;
    }

    /**
     * 以静态类方式调用方法时，自动执行次方法，如 PDOx::method();
     * @param  string $method    静态方法名
     * @param  array $arguments 参数数组
     * @return
     */
    final public static function __callStatic($method, $arguments) {
        try {
            $instance = self::getInstance();
            return call_user_func_array(array($instance, $method), $arguments);
        } catch (Exception $e) {
            throw new Exception($e->getMessage());
        }
    }

    /**
     * 执行curl操作
     * @param  string $ctype 请求类型，GET或POST
     * @return 返回查询后的数据
     */
    private static function doCurl($url, $data=null) {

        // 设置curl参数
        curl_setopt(self::$_curl, CURLOPT_URL, $url);
        curl_setopt(self::$_curl, CURLOPT_SSL_VERIFYPEER, FALSE);
        curl_setopt(self::$_curl, CURLOPT_SSL_VERIFYHOST, FALSE);
        if (!empty($data)) {
            curl_setopt(self::$_curl, CURLOPT_POST, 1);
            curl_setopt(self::$_curl, CURLOPT_POSTFIELDS, $data);
        }
        curl_setopt(self::$_curl, CURLOPT_RETURNTRANSFER, 1);

        // 执行操作，并返回结果
        $output = curl_exec(self::$_curl);
        self::_closeCurl();
        return json_decode($output, true);
    }

    /**
     * 关闭创建的curl资源
     * @return
     */
    public static function _closeCurl() {
        curl_close(self::$_curl);
    }
}
