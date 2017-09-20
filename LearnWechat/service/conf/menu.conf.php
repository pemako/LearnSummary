<?php
/**
 * 自定义菜单配置项
 */
return '{
    "button": [
        {
            "name": "DOMOB",
            "sub_button": [
                {
                    "name": "关于多盟",
                    "type": "view",
                    "url": "http://duomengwx.moxz.cn/menu/about.html"
                },
                {
                    "name": "公司荣誉",
                    "type": "view",
                    "url": "http://duomengwx.moxz.cn/menu/honour.html"
                },
                {
                    "name": "多盟DSPAN",
                    "type": "view",
                    "url": "http://duomengwx.moxz.cn/menu/dspan.html"
                },
                {
                    "name": "优质媒体",
                    "type": "view",
                    "url": "http://duomengwx.moxz.cn/menu/medias.html"
                },
                {
                    "name": " 合作案例",
                    "type": "view",
                    "url": "http://duomengwx.moxz.cn/menu/cases.html"
                }
            ]
        },
        {
            "name": "移动资讯",
            "type": "view",
            "url": "http://mp.weixin.qq.com/mp/getmasssendmsg?__biz=MjM5NjA2NjE0Ng==#wechat_webview_type=1&wechat_redirect"
        },
        {
            "name": "更多",
            "sub_button": [
                {
                    "name": "授权验证",
                    "type": "view",
                    "url": "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx0188a6062fc51b93&redirect_uri=http%3A%2F%2Fpemakocn.sinaapp.com%2Fservice%2Foauth2%2Foauth2_openid.php&response_type=code&scope=snsapi_userinfo&state=STATE#wechat_redirect"
                },
                {
                    "name": "JSSDK测试",
                    "type": "view",
                    "url": "http://pemakocn.sinaapp.com/jssdkdemo/index.htm"
                },
                {
                    "name": "热门招聘",
                    "type": "view",
                    "url": "http://duomengwx.moxz.cn/menu/jobs.html"
                },
                {
                    "name": "幸运抽奖",
                    "type": "click",
                    "key": "clk_choujiang"
                }
            ]
        }
    ]
}';
