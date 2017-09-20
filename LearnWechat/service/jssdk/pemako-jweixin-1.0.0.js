/**
 *  调用微信JS
 */
(function(that){
	
	that.action = 'http://pemakocn.sinaapp.com/service/jssdk/pemakoWeixinApi.php';

	/**
	 * 提供一些对内或对外的方法
	 */
	(function(lib){
		// query 格式参数为json格式
		lib.queryStrToJson = function(querystr, decode){
			var params = {};
			querys = querystr.split('&');
			for (var i in querys) {
				var _s = querys[i].indexOf('=');
				if (_s == -1) continue;
				params[querys[i].substring(0, _s)] = !decode ? querys[i].substring(_s + 1) : decodeURIComponent(querys[i].substring(_s + 1));
			}
			return params;
		};
		
		// json格式转换为query格式参数，当参数值不是一个对象的时候，原样返回
		lib.jsonToQueryStr = function(json, encode) {
			var param = new Array();
			if (typeof(json) != 'object') return json;
			for (var i in json) {
				json[i] = !encode ? json[i] : encodeURIComponent(json[i]);
				param.push(i + '=' + json[i])
			}
			return param.join('&');
		};
		
		// 判断josn中是否存在一个key
		lib.inJosn = function(str, json) {
			for (var k in json) {
				if (k == str) return true;
			}
			return false;
		};
		
		// 将两个json合并在一起
		lib.jsonMerge = function(p, sp) {
			for (var k in sp) {
				// 如果key之前存在，这里给出提示，让开发者修改字段名
				if (lib.inJosn(k, p)) lib.log(k + ', the key already exists!');
				p[k] = sp[k];
			}
			return p;
		}
		
		// 获取浏览器类型
		lib.getBrowserType = function() {
			var ua = navigator.userAgent,app = navigator.appVersion;
			return {
				android: ua.indexOf('Android') > -1 || ua.indexOf('Linux') > -1, //android系统
				iPhone: ua.indexOf('iPhone') > -1, //是否iPhone终端
				iPad: ua.indexOf('iPad') > -1, //是否iPad终端
				iOS: !!ua.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/) || ua.indexOf('Mac') > -1, //iOS系统
				wp: !!ua.match(/windows (ce|phone)/i), //是否winphone终端
				webApp: ua.indexOf('Safari') == -1, //是否web应该程序
				webKit: ua.indexOf('AppleWebKit') > -1, //webkit内核
			};
		};
		
		// 判断一个链接是否有search部分
		lib.isHasSearchByUrl = function(u) {
				var pos = u.indexOf('?');
				return pos != -1 ? (u.substring(pos + 1) == '' ? false : true) : false;
			}
		
		// 给一个链接增加GET传递的参数
		lib.urlConcatTrack = function(u, json) {
			var conc = '?';
			if (lib.isHasSearchByUrl(u)) conc = '&';
			return u += conc + lib.jsonToQueryStr(json, true);
		};
		
		// 控制台输出
		lib.log = function(str) {
			console.log(str);
		};
		
		/* ajax数据提交
		 * param json object
		 * url 数据提交的地址
		 * data 提交的数据，json或query格式
		 * type 提交方式，get/post
		 * fun 回调方法
		 * dataType 返回数据类型
		 */
		lib.ajax = function(param) {
			param.type = param.type || 'get';
			//param.type.toLowerCase();
			if (!param.url) lib.log('submit url is empty');
			param.fun = param.fun || function(s) {};
			if (param.type == 'get') {
				if (param.data) {
					param.url = lib.urlConcatTrack(param.url, param.data);
				}
				param.data = null;
			} else if (param.type == 'post') {
				param.data = lib.jsonToQueryStr(param.data, true) || null;
			} else {
				lib.log('do not support the type of submission: ' + param.type);
			}
			var xhr = new XMLHttpRequest();
			xhr.open(param.type, param.url, true);
			param.type == 'post' ? xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded') : null;
			xhr.send(param.data);
			xhr.onreadystatechange = function() {
				if (xhr.readyState == 4 && xhr.status == 200) {
					var res = xhr.responseText;
					if (param.dataType == 'json') {
						try {
							res = eval('(' + res + ')');
							that.weixinConfig(param.debug,param.appId, res.timestamp, res.nonceStr, res.signature, param.jsApiList);
						} catch (e) {}
					}
					param.fun(res);
				}
			}
		};
		
	})(that.lib = {});
	
	// 初始化
	that.init = function(appId, jsApiList, debug){
		var debug = debug || false;
		// 获取URL #号前面的部分
		var current_href = location.href;
		if(current_href.search(/#/) < 0) {
			current_href = encodeURIComponent(current_href);
		} else {
			current_href = encodeURIComponent(current_href.match(/.*#/)[0].substr(0,current_href.match(/.*#/)[0].length-1));
		}
		
		url = that.action + '?url=' + current_href;
		
		// 向服务端发起请求进行签名验证 验证通过后，调用 weixinConfig
		var param = {
			type:'get',
			url: url,
			debug:debug,
			appId:appId,
			jsApiList : jsApiList,
			dataType:'json',
		};	
		that.lib.ajax(param);
	};
	
	
	// 接口配置
	that.weixinConfig = function(debug, appId, timestamp, nonceStr, signature, jsApiList){
		wx.config({
			debug : 	debug, // 开启调试模式
			appId : 	appId, // 必填，公众号的唯一标识
			timestamp : timestamp, // 必填，生成签名的时间戳
			nonceStr : 	nonceStr, // 必填，生成签名的随机串
			signature : signature, // 必填，生成的签名
			jsApiList : jsApiList // 必填，需要使用的JS接口列表
		});
	};
	
})(window.pemakoWeixinApi={})
