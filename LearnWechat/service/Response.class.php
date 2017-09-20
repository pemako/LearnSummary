<?php

/**
 *
 */
class Response {

    /**
     * 检测是否是微信服务端请求
     * @return
     */
    public function checkRequest() {
        $wx_str_random = trim($_GET['echostr']);
        if ($this->_checkSignature()) { // 校验签名
            echo $wx_str_random;
            exit;
        }
    }

    /**
     * 微信签名验证
     * @return  true 签名正确/false 签名错误
     */
    private function _checkSignature() {

        // 获取请求中的签名和生成签名所需的参数
        $signature = trim($_GET['signature']);
        $timestamp = trim($_GET['timestamp']);
        $nonce = trim($_GET['nonce']);

        // 对所需参数先按字典顺序排序，然后拼接成字符串进行sha1加密
        $tmpArr = array(TOKEN, $timestamp, $nonce);
        sort($tmpArr, SORT_STRING);
        $tmpStr = implode('', $tmpArr);
        $sign = sha1($tmpStr);

        return $sign == $signature ? true : false;
    }

    /**
     * 根据不同的请求类型，响应用户的输入信息
     * @return  与请求对应的响应信息
     */
    public function responseRequest() {

        $allowedMsgType = array('event', 'text', 'image', 'location', 'voice', 'video', 'link');
        $postStr = $GLOBALS['HTTP_RAW_POST_DATA'];
        $result = '';

        if (!empty($postStr)) {

            // 记录接收到的请求消息
            // 读取微信服务器POST过来的用户消息XML数据包
            $postObj = simplexml_load_string($postStr, 'SimpleXMLElement', LIBXML_NOCDATA);
            $postMsgType = trim($postObj->MsgType);

            // 判断是否是微信支持的响应消息类型
            if (in_array($postMsgType, $allowedMsgType)) {
                $handleFuncName = 'receive'.ucfirst($postMsgType); // 构造与消息类型对应的处理方法名
                $result = ResponseHandler::$handleFuncName($postObj); // 通过处理方法构造响应结果
            } else {
                $result = 'Unsuported msg type: '.$postMsgType;
            }

            echo $result;
        } else {
            echo '';
            exit;
        }
    }
}
