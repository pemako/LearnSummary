<?php

/**
 * 对接收到的用户输入进行处理，响应对应的信息
 */

class ResponseHandler {

    /**
     * 接收事件消息
     * @param object $obj 包含用户所发送消息内容的对象
     * @return 最终响应消息
     */
    public static function receiveEvent($obj) {

        $content = '';

        // 根据不同的事件类型组织内容
        switch ($obj->Event) {
            case 'subscribe':
                $content = '欢迎关注中国 PEMAKO。';
                if (!empty($object->EventKey)) {
                    $paramsQr = str_replace('qrscene_', '', $object->EventKey);
                    $content .= "\n来自二维码场景 ".$paramsQr;
                }
                break;
            case 'unsubscribe':
                $content = '取消关注成功';
                break;
            case 'SCAN':
                $content = '扫描场景 '.$obj->EventKey;
                break;
            case 'CLICK':
                $content = self::_getContentByEventKey($obj);
                break;
            case 'LOCATION':
            	$url = "http://api.map.baidu.com/geocoder/v2/?ak=B944e1fce373e33ea4627f95f54f2ef9&location=$obj->Latitude,$obj->Longitude&output=json&coordtype=gcj02ll";
            	$output = file_get_contents($url);
            	$address = json_decode($output, true);
            	$content = "地理位置 ".$address["result"]["addressComponent"]["province"]." ".$address["result"]["addressComponent"]["city"]." ".$address["result"]["addressComponent"]["district"]." ".$address["result"]["addressComponent"]["street"];
            	break;
            case 'VIEW':
                $content = '点击菜单跳转链接 '.$obj->EventKey;
                break;
            case "MASSSENDJOBFINISH":
                $content = "消息ID：".$object->MsgID."，结果：".$object->Status."，
                    粉丝数：".$object->TotalCount."，过滤：".$object->FilterCount."，
                    发送成功：".$object->SentCount."，发送失败：".$object->ErrorCount;
                break;
            default:
                $content = 'receive a new event: '.$obj->Event;
                break;
        }

        return self::_handleResMsg($obj, $content);
    }

    /**
     * 根据不同的自定义菜单的类型，获取响应内容
     * @param  object $obj 包含用户所发送消息内容的对象
     * @return 自定义菜单对应的响应内容
     */
    private static function _getContentByEventKey($obj) {
        $content = '';
        switch ($obj->EventKey) {
            case 'clk_choujiang':
                $content = array(
                    array(
                        'Title' => 'Domob多盟 幸运大转盘',
                        'Description' => '点击玩转幸运大转盘',
                        'PicUrl' => 'http://pemakocn.sinaapp.com/service/images/banner.jpg',
                        'Url' => 'http://pemakocn.sinaapp.com/choujiang/index2.htm?uid=%s'
                    )
                );
                break;
            default:
                $content = '您点击了菜单：'.$obj->EventKey;
                break;
        }

        return $content;
    }

    /**
     * 接收纯文本消息
     * @param  obj $obj 包含用户所发送消息内容的对象
     * @return 最终的响应消息
     */
    public static function receiveText($obj) {
    	// 进行天气预报
    	$data = explode(' ', $obj->Content);
		if($data[1] === '天气'){
			return self::_getWeather($obj, $data[0]);
		} else if(strtolower($data[1]) == 'pm'){
			return self::_getPM($obj, $data[0]);
		}
    	
		// 进行中英文翻译 输入格式为 需要翻译的内容 翻译
		if (trim(substr($obj->Content,strrpos($obj->Content,' '))) === '翻译'){
			$keywords = substr($obj->Content, 0, strrpos($obj->Content, ' '));
			return self::_getFanyi($obj, $keywords);
		}
		
		// 查询PM2.5值
		
        $keywordsArr = require_once('./service/conf/keywords.conf.php');
        $content = '';

        // 匹配关键字，获取对应的响应信息
        foreach ($keywordsArr as $k => $v) {
            if (is_array($v)) {
                if (in_array($obj->Content, $v['keywords'])) {
                    $content = $v['reply'];
                }
            }
        }

        // 未匹配关键字，显示默认响应信息
        $content = empty($content) ? sprintf($keywordsArr['default'], $obj->Content) : $content;
        return self::_handleResMsg($obj, $content);
    }
    
    /**
     * 进行翻译
     */ 
    private static function _getFanyi($obj, $keyword){
    		$apihost = "http://fanyi.youdao.com/";
    		$apimethod = "openapi.do?";
    		$apiparams = array('keyfrom'=>"txw1958", 'key'=>"876842050", 'type'=>"data", 'doctype'=>"json", 'version'=>"1.1", 'q'=>$keyword);
    		$apicallurl = $apihost.$apimethod.http_build_query($apiparams);
    	
    		$ch = curl_init();
    		curl_setopt($ch, CURLOPT_URL, $apicallurl);
    		curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    		$output = curl_exec($ch);
    		if(curl_errno($ch)){ echo 'CURL ERROR Code: '.curl_errno($ch).', reason: '.curl_error($ch);}
    		curl_close($ch);
    	
    		$youdao = json_decode($output, true);
    		$result = "";
    		switch ($youdao['errorCode']){
    			case 0:
    				if (isset($youdao['basic'])){
    					$result .= $youdao['basic']['phonetic']."\n";
    					foreach ($youdao['basic']['explains'] as $value) {
    						$result .= $value."\n";
    					}
    				}else{
    					$result .= $youdao['translation'][0];
    				}
    				break;
    			default:
    				$result = "系统错误：错误代码：".$youdao['errorCode'];
    				break;
    		}
    		return self::_transmitText($obj, $result);
    }

    /**
     * PM2.5测试
     */
    private static function _getPM($obj, $city){
    	$url = "http://www.pm25.in/api/querys/aqi_details.json?stations=no&city=".urlencode($city)."&token=5j1znBVAsnSf5xQyNQyq";
    	
    	$ch = curl_init();
    	curl_setopt($ch, CURLOPT_URL, $url);
    	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    	$output = curl_exec($ch);
    	curl_close($ch);
    	
    	$cityAir = json_decode($output, true);
    	if (isset($cityAir['error'])){
    		return $cityAir['error'];
    	}else{
    		$result = "空气质量指数(AQI)：".$cityAir[0]['aqi']."\n".
    				"空气质量等级：".$cityAir[0]['quality']."\n".
    				"细颗粒物(PM2.5)：".$cityAir[0]['pm2_5']."\n".
    				"可吸入颗粒物(PM10)：".$cityAir[0]['pm10']."\n".
    				"一氧化碳(CO)：".$cityAir[0]['co']."\n".
    				"二氧化氮(NO2)：".$cityAir[0]['no2']."\n".
    				"二氧化硫(SO2)：".$cityAir[0]['so2']."\n".
    				"臭氧(O3)：".$cityAir[0]['o3']."\n".
    				"更新时间：".preg_replace("/([a-zA-Z])/i", " ", $cityAir[0]['time_point']);
    		$aqiArray = array();
    		$aqiArray[] = array("Title" =>$cityAir[0]['area']."空气质量", "Description" =>$result, "PicUrl" =>"", "Url" =>"");
    		//return $aqiArray;
    	}
    	$content = $aqiArray;
    	foreach ($content as $k => $v) {
    		$content[$k]['Url'] = sprintf($v['Url'], $obj->FromUserName);
    	}
    	return self::_transmitNews($obj, $content);
    }
    
    /**
     * 发送城市 + 天气返回3天内的天气预报信息
     */
    private static function _getWeather($obj, $city){ 
    	$url = "http://api.map.baidu.com/telematics/v3/weather?location=".urlencode($city)."&output=json&ak=ECe3698802b9bf4457f0e01b544eb6aa";
    	$ch = curl_init();
    	curl_setopt($ch, CURLOPT_URL, $url);
    	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    	$output = curl_exec($ch);
    	curl_close($ch);
    	$result = json_decode($output, true);
    	if ($result["error"] != 0){
    		return $result["status"];
    	}
    	$curHour = (int)date('H',time());
    	$weather = $result["results"][0];
    	$weatherArray[] = array("Title" =>$weather['currentCity']."天气预报", "Description" =>"", "PicUrl" =>"", "Url" =>"");
    	for ($i = 0; $i < count($weather["weather_data"]); $i++) {
    		$weatherArray[] = array("Title"=>$weather["weather_data"][$i]["date"]."\n".
    				$weather["weather_data"][$i]["weather"]." ".
    				$weather["weather_data"][$i]["wind"]." ".
    				$weather["weather_data"][$i]["temperature"],
    				"Description"=>"",
    				"PicUrl"=>(($curHour >= 6) && ($curHour < 18))?$weather["weather_data"][$i]["dayPictureUrl"]:$weather["weather_data"][$i]["nightPictureUrl"],
    				"Url"=>""
    		);
    	}
    	 
    	$content = $weatherArray;

    	foreach ($content as $k => $v) {
    		$content[$k]['Url'] = sprintf($v['Url'], $obj->FromUserName);
    	}
    	return self::_transmitNews($obj, $content);
    }
    
    
    /**
     * 根据响应信息的类型调用相应的处理方法，构造最终的响应消息
     * @param  object $obj 包含用户所发送消息内容的对象
     * @param  mixed $content 响应内容
     * @return 处理好的最终响应消息
     */
    private static function _handleResMsg($obj, $content) {

        // 判断响应信息的类型
        if (is_array($content)) {
            if (isset($content[0]['PicUrl'])) { // 图文
                foreach ($content as $k => $v) {
                    $content[$k]['Url'] = sprintf($v['Url'], $obj->FromUserName);
                }
                return self::_transmitNews($obj, $content);
            } else if (isset($content['MusicUrl'])) { // 音乐
                return self::_transmitMusic($obj, $content);
            } else if (isset($content['func'])) { // 自定义类型
                $funcName = '_get'.$content['func'];
                return self::$funcName($obj);
            }
        } else { // 纯文本
            return self::_transmitText($obj, $content);
        }
    }
    
    public static function _getLottery($obj){
    	$uid = $obj->FromUserName;
    	$conn = mysql_connect('127.0.0.1', 'root', '$love716424AZLN');
    	mysql_select_db('weixin', $conn);
    	$sql = "select pid from weixin_lottery_record where uid='{$uid}'";
    	$res = mysql_query($sql);
    	$data = mysql_fetch_array($res);
    	if($data){
    		if($data[0]['pid'] == 0){
    			$content = "很遗憾你么你有中奖！";
    		} else {
    			$content = "恭喜你中了". $data[0]['pid']. "等奖";
    		}
    		return self::_transmitText($obj,$content);
    	} else {
    		$content =  '请先进行抽奖！';
    		return self::_transmitText($obj,$content);
    	}
    }
    
    /**
     * 接收图片消息
     * @param  obj $obj 包含用户所发送消息内容的对象
     * @return 最终的响应消息
     */
    public static function receiveImage($obj) {
        $tmpStr = "您发送的是图片消息\n地址：%s\n媒体ID：%s";
        $content = sprintf($tmpStr, $obj->PicUrl, $obj->MediaId);
        return self::_transmitText($obj, $content);
        //return self::_transmitImage($obj, $obj->MediaId);
    }

    /**
     * 接收位置消息
     * @param  obj $obj 包含用户所发送消息内容的对象
     * @return 最终的响应消息
     */
    public static function receiveLocation($obj) {
        $tmpStr = "纬度：%s\n经度：%s\n缩放级别：%s\n位置：%s";
        $content = sprintf($tmpStr, $obj->Location_X, $obj->Location_Y, $obj->Scale, $obj->Label);
        return self::_transmitText($obj, $content);
    }

    /**
     * 接收语音消息
     * @param  obj $obj 包含用户所发送消息内容的对象
     * @return 最终的响应消息
     */
    public static function receiveVoice($obj) {
        if (!empty($obj->Recognition)){
            $content = "您刚才说的是：".$obj->Recognition;
            return self::_transmitText($obj, $content);
        } else {
            return self::_transmitVoice($obj, $obj->MediaId);
        }
    }

    /**
     * 接收视频消息
     * @param  obj $obj 包含用户所发送消息内容的对象
     * @return 最终的响应消息
     */
    public static function receiveVideo($obj) {
        $contentArr = array(
            'MediaId'       =>  $obj->MediaId,
            'ThumbMediaId'  =>  $obj->ThumbMediaId,
            'Title'         =>  '这是视频消息的标题',
            'Description'   =>  '这是视频消息的描述'
        );
        $tmpStr = "您发送的是视频消息\nMediaId：%s\nThumbMediaId：%s";
        $content = sprintf($tmpStr, $obj->MediaId, $obj->ThumbMediaId);
        //return self::_transmitText($obj, $content);
        return self::_transmitVideo($obj, $contentArr);
    }

    /**
     * 接收链接消息
     * @param  obj $obj 包含用户所发送消息内容的对象
     * @return 最终的响应消息
     */
    public static function receiveLink($obj) {
        $tmpStr = "您发送的是链接消息\n标题：%s\n内容：%s\n地址：%s";
        $content = sprintf($tmpStr, $obj->Title, $obj->Description, $obj->Url);
        return self::_transmitText($obj, $content);
    }

    /**
     * 将原始的文本响应消息转为xml格式，以便微信服务器解析转发
     * @param  object $obj 由接收到的消息解析得到的对象
     * @param  string $content 将要响应的消息
     * @return 最终组合好的xml格式响应消息
     */
    private static function _transmitText($obj, $content) {
        $textTpl =
            "<xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[text]]></MsgType>
                <Content><![CDATA[%s]]></Content>
            </xml>";
        return sprintf($textTpl, $obj->FromUserName, $obj->ToUserName, time(), $content);
    }

    /**
     * 将原始的文本响应消息转为xml格式，以便微信服务器解析转发
     * @param  object $obj 由接收到的消息解析得到的对象
     * @param  array $newsArray 将要响应的消息
     * @return 最终组合好的xml格式响应消息
     */
    private static function _transmitNews($object, $newsArray) {

        if(!is_array($newsArray)) return;

        $itemStr = '';
        $itemTpl =
            "<item>
                <Title><![CDATA[%s]]></Title>
                <Description><![CDATA[%s]]></Description>
                <PicUrl><![CDATA[%s]]></PicUrl>
                <Url><![CDATA[%s]]></Url>
            </item>";
        foreach ($newsArray as $item) {
            $itemStr .= sprintf($itemTpl, $item['Title'], $item['Description'], $item['PicUrl'], $item['Url']);
        }
        $newsTpl =
            "<xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[news]]></MsgType>
                <Content><![CDATA[]]></Content>
                <ArticleCount>%s</ArticleCount>
                <Articles>".$itemStr."</Articles>
            </xml>";

        return sprintf($newsTpl,
            $object->FromUserName, $object->ToUserName, time(), count($newsArray));
    }

    private static function _transmitImage($obj, $content) {
        $imgMsgTpl =
            "<xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[image]]></MsgType>
                <Image>
                    <MediaId><![CDATA[%s]]></MediaId>
                </Image>
            </xml>";
        return sprintf($imgMsgTpl, $obj->FromUserName, $obj->ToUserName, time(), $content);
    }

    /**
     * [_transmitVideo description]
     * @param  [type] $obj        [description]
     * @param  [type] $contentArr [description]
     * @return [type]             [description]
     */
    private static function _transmitVideo($obj, $contentArr) {
        $videoMsgTpl =
            "<xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[video]]></MsgType>
                <Video>
                    <MediaId><![CDATA[%s]]></MediaId>
                    <Title><![CDATA[%s]]></Title>
                    <Description><![CDATA[%s]]></Description>
                </Video>
            </xml>";
        return sprintf($videoMsgTpl, $obj->FromUserName, $obj->ToUserName, time(),
            $contentArr['MediaId'], $contentArr['Title'], $contentArr['Description']);
    }
}

