<?php

/**
 * 获取用户地理位置信息
 * 
 * 百度地图Geocoding API服务接口地址为 http://api.map.baidu.com/geocoder/v2/?ak=B944e1fce373e33ea4627f95f54f2ef9&location=22.539968,113.954979&output=json&coordtype=gcj02ll
 */


function receiveEvent($object){
	$contentStr = "";
	switch ($object->Event)
	{
		case "subscribe":
			$contentStr = "欢迎关注".(isset($object->EventKey)?("\n场景 ".$object->EventKey):"");
			break;
		case "unsubscribe":
			$contentStr = "取消关注";
			break;
		case "LOCATION":
			$url = "http://api.map.baidu.com/geocoder/v2/?ak=B944e1fce373e33ea4627f95f54f2ef9&location=$object->Latitude,$object->Longitude&output=json&coordtype=gcj02ll";
			$output = file_get_contents($url);
			$address = json_decode($output, true);
			$contentStr = "位置 ".$address["result"]["addressComponent"]["province"]." ".$address["result"]["addressComponent"]["city"]." ".$address["result"]["addressComponent"]["district"]." ".$address["result"]["addressComponent"]["street"];
			break;
		default:
			break;
	}
	$resultStr = $this->transmitText($object, $contentStr);
	return $resultStr;
}
