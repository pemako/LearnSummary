<?php

// 因为SAE不支持文件的读写改用memcache方式存放
// 这里使用的是SAE的memcache进行存储access_token的

class JSSDK {
	
	private $appId;
	private $appSecret;
	private $mmc;

	public function __construct($appId, $appSecret){
		$this->appId = $appId;
        $this->appSecret = $appSecret;	
        $this->mmc = memcache_init();
	}
	
	/**
	 * 校验签名
	 */
	public function getSignPackage($url) {
		$jsapiTicket = $this->getJsApiTicket ();
		// 注意 URL 一定要动态获取，不能 hardcode.
		//$protocol = (! empty ( $_SERVER ['HTTPS'] ) && $_SERVER ['HTTPS'] !== 'off' || $_SERVER ['SERVER_PORT'] == 443) ? "https://" : "http://";
		//$url = "$protocol$_SERVER[HTTP_HOST]$_SERVER[REQUEST_URI]";
		
		$timestamp = time();
		$nonceStr = $this->createNonceStr();
	
		// 这里参数的顺序要按照 key 值 ASCII 码升序排序
		$string = "jsapi_ticket=$jsapiTicket&noncestr=$nonceStr&timestamp=$timestamp&url=$url";
		$signature = sha1($string);
		$signPackage = array (
				"appId" => $this->appId,
				"nonceStr" => $nonceStr,
				"timestamp" => $timestamp,
				"url" => $url,
				"signature" => $signature,
				"rawString" => $string
		);
		return $signPackage;
	}
	
	/**
	 * 获取随机字符串
	 */
	private function createNonceStr($length = 16) {
		$chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
		$str = "";
		for($i = 0; $i < $length; $i ++) {
			$str .= substr ( $chars, mt_rand ( 0, strlen ( $chars ) - 1 ), 1 );
		}
		return $str;
	}
	
	/**
	 * 获取 jsapi_ticket
	 * url https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token=ACCESS_TOKEN&type=jsapi
	 * jsapi_ticket是公众号用于调用微信JS接口的临时票据。
	 * 正常情况下，jsapi_ticket的有效期为7200秒，通过access_token来获取。
	 * 由于获取jsapi_ticket的api调用次数非常有限，频繁刷新jsapi_ticket会导致api调用受限，影响自身业务，开发者必须在自己的服务全局缓存jsapi_ticket
	 * 
	 * 本例把获取到的ticket保存的文件中
	 */
	
	 function getJsApiTicket(){
        if ($this->mmc != false){
            $data = json_decode(memcache_get($this->mmc, 'jsapi_ticket'));
        }
		if($data->expire_time < time() || !$data){
			// 重新获取ticket
			$access_token = $this->getAccessToken();
			$url = "https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token={$access_token}&type=jsapi";
			$res = json_decode($this->httpGet($url));
			$ticket = $res->ticket;
			if($ticket){
				$data->expire_time = time() + 7000;
				$data->jsapi_ticket = $ticket;
                memcache_set($this->mmc, 'jsapi_ticket', json_encode($data));
			}
		} else {
			$ticket = $data->jsapi_ticket;
		}
		return $ticket;
	}
	
	/**
	 * 把access token的值保存到文件中
	 * @return unknown
	 */
	function getAccessToken(){
        if ($this->mmc != false){
            $data = json_decode(memcache_get($this->mmc, 'access_token'));
        }
		if(!$data || $data->expire_time < time()){
			// 重新获取token
			$url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=".$this->appId."&secret=".$this->appSecret;
			$res = json_decode($this->httpGet($url));
			$access_token = $res->access_token;
			if($access_token){
				$data->expire_time = time () + 7000;
				$data->access_token = $access_token;
                
                memcache_set($this->mmc, 'access_token', json_encode($data));
			}
		} else {
			$access_token = $data->access_token;
		}
		
		return $access_token;
	}
	
	private function httpGet($url) {
		$curl = curl_init ();
		curl_setopt ( $curl, CURLOPT_RETURNTRANSFER, true );
		curl_setopt ( $curl, CURLOPT_TIMEOUT, 500 );
		curl_setopt ( $curl, CURLOPT_SSL_VERIFYPEER, false );
		curl_setopt ( $curl, CURLOPT_SSL_VERIFYHOST, false );
		curl_setopt ( $curl, CURLOPT_URL, $url );
		
		$res = curl_exec ( $curl );
		curl_close ( $curl );
		
		return $res;
	}
}


$obj = new JSSDK('Your APP_ID','Your APP_SECRIET');

$access_token = $obj->getAccessToken();

//echo $access_token;

//$ticket = $obj->getJsApiTicket();
//echo $ticket;exit;

$url = $_REQUEST['url'];
$ticket = $obj->getSignPackage($url);
echo json_encode($ticket);
