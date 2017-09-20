<?php

/**
 * 天气预报
 */


// var_dump(getWeatherInfo("深圳"));
// 使用百度API进行获取天气
/*
function getWeatherInfo($cityName) {
	if ($cityName == "" || (strstr($cityName, "+"))){
		return "发送天气+城市，例如'天气深圳'";
	}
	$url = "http://api.map.baidu.com/telematics/v3/weather?location=".urlencode($cityName)."&output=json&ak=ECe3698802b9bf4457f0e01b544eb6aa";
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
		$weatherArray[] = array("Title"=>
				$weather["weather_data"][$i]["date"]."\n".
				$weather["weather_data"][$i]["weather"]." ".
				$weather["weather_data"][$i]["wind"]." ".
				$weather["weather_data"][$i]["temperature"],
				"Description"=>"",
				"PicUrl"=>(($curHour >= 6) && ($curHour < 18))?$weather["weather_data"][$i]["dayPictureUrl"]:$weather["weather_data"][$i]["nightPictureUrl"], "Url"=>"");
	}
	return $weatherArray;
}

*/


function getWeatherInfo($cityName)
{
	if ($cityName == ""){
		return "发送天气+城市，例如'天气深圳'";
	}
	$citycode = fromKeywordToCode($cityName);
	if ($citycode == ""){
		return "没有该城市？";
	}

	$winddirection = array("0"=>"无持续风向","1"=>"东北风","2"=>"东风","3"=>"东南风","4"=>"南风","5"=>"西南风","6"=>"西风","7"=>"西北风","8"=>"北风","9"=>"旋转风");
	$windpower = array("0"=>"微风","1"=>"3-4级","2"=>"4-5级","3"=>"5-6级","4"=>"6-7级","5"=>"7-8级","6"=>"8-9级","7"=>"9-10级","8"=>"10-11级","9"=>"11-12级");
	$phenomenon = array("00"=>"晴","01"=>"多云","02"=>"阴","03"=>"阵雨","04"=>"雷阵雨","05"=>"雷阵雨伴有冰雹","06"=>"雨夹雪","07"=>"小雨","08"=>"中雨","09"=>"大雨","10"=>"暴雨","11"=>"大暴雨","12"=>"特大暴雨","13"=>"阵雪","14"=>"小雪","15"=>"中雪","16"=>"大雪","17"=>"暴雪","18"=>"雾","19"=>"冻雨","20"=>"沙尘暴","21"=>"小到中雨","22"=>"中到大雨","23"=>"大到暴雨","24"=>"暴雨到大暴雨","25"=>"大暴雨到特大暴雨","26"=>"小到中雪","27"=>"中到大雪","28"=>"大到暴雪","29"=>"浮尘","30"=>"扬沙","31"=>"强沙尘暴","53"=>"霾","99"=>"无");

	$weatherArray = array();
	$weatherArray[] = array("Title" =>$cityName."天气预报", "Description" =>"", "PicUrl" =>"", "Url" =>"");

	//实况
	$liveInfo = json_decode(getWeatherData($citycode, "observe"), true);
	$weatherArray[] = array("Title" =>"【实况】温度".$liveInfo["l"]["l1"]."℃ 湿度".$liveInfo["l"]["l2"]."%% ".$winddirection[$liveInfo["l"]["l4"]].$liveInfo["l"]["l3"]."级 发布时间：".$liveInfo["l"]["l7"], "Description" =>"", "PicUrl" =>"", "Url" =>"");

	//指数
	$indexInfo = json_decode(getWeatherData($citycode, "index"), true);
	$indextitle = "";
	for ($i = 0; $i < count($indexInfo["i"]); $i++) {
		$indextitle .= "【".$indexInfo["i"][$i]["i4"]."】".$indexInfo["i"][$i]["i5"]."\n";
		break;
	}
	$weatherArray[] = array("Title" =>trim($indextitle), "Description" =>"", "PicUrl" =>"", "Url" =>"");

	//3日
	$forecast3dInfo = json_decode(getWeatherData($citycode, "forecast3d"), true);
	$day3Info = $forecast3dInfo["f"]["f1"];
	$weekArray = array("日","一","二","三","四","五","六");
	for ($i = 0; $i < count($day3Info); $i++) {
		if (date("H") < 18){
			$offset = strtotime("+".$i." day");
			$forecast3dtitle = date("m月d日",$offset)." 周".$weekArray[date('w',$offset)]." ".
					$phenomenon[$day3Info[$i]["fa"]].(($day3Info[$i]["fa"] != $day3Info[$i]["fb"])?("转".$phenomenon[$day3Info[$i]["fb"]]):"")." ".
					$day3Info[$i]["fc"]."℃~".$day3Info[$i]["fd"]."℃ ".
					$winddirection[$day3Info[$i]["fe"]]." ".$windpower[$day3Info[$i]["fg"]]." ".
					"日出日落：".str_replace("|", "~", $day3Info[$i]["fi"]);
			$picurl = "http://discuz.comli.com/weixin/weather/icon/d".$day3Info[$i]["fa"].".jpg";
		}else{
			$offset = strtotime("+".($i+1)." day");
			$forecast3dtitle = date("m月d日",$offset)." 周".$weekArray[date('w',$offset)]." ".
					$phenomenon[$day3Info[$i]["fb"]]." ".$day3Info[$i]["fd"]."℃".
					$winddirection[$day3Info[$i]["fe"]]." ".$windpower[$day3Info[$i]["fg"]]." ".
					"日出日落：".str_replace("|", "~", $day3Info[$i]["fi"]);
			$picurl = "http://discuz.comli.com/weixin/weather/icon/d".$day3Info[$i]["fb"].".jpg";
		}
		$weatherArray[] = array("Title" =>trim($forecast3dtitle), "Description" =>"", "PicUrl" =>$picurl, "Url" =>"");
	}
	return $weatherArray;
}


function getWeatherData($areaid, $type)
{
	//将自己申请到的接口，如果没有接口，可以使用百度的天气代码
	$appid = "";
	$private_key = "";

	$urls = 'http://webapi.weather.com.cn/data/?areaid='.$areaid.'&type='.$type.'&date='.date("YmdHi").'&appid=';
	$public_key = $urls.$appid;
	$key = urlencode(base64_encode(hash_hmac('sha1', $public_key, $private_key, true)));
	$url = $urls.substr($appid,0,6).'&key='.$key;

	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, $url);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	$output = curl_exec($ch);
	curl_close($ch);
	return $output;
}

function fromKeywordToCode($keyword)
{
	Global $mysql_host;
	Global $mysql_host_s;
	Global $mysql_port;
	Global $mysql_user;
	Global $mysql_password;
	Global $mysql_database;

	$mysql_table = "weather";
	$mysql_state = "SELECT * FROM `".$mysql_table."` WHERE `area` LIKE  '%".$keyword."%' LIMIT 0 , 1";
	$con = @mysql_connect($mysql_host.':'.$mysql_port, $mysql_user, $mysql_password, true);
	if (!$con){
		die('Could not connect: ' . mysql_error());
	}
	mysql_query("SET NAMES 'UTF8'");
	mysql_select_db($mysql_database, $con);
	$result = mysql_query($mysql_state);
	$citycode = "";
	while($row = mysql_fetch_array($result))
	{
		$citycode = $row['code'];
		break;
	}
	mysql_close($con);
	return $citycode;
}


