<?php

return array(
	'default' => '很高兴为您服务，有什么问题可以直接留言，我们会尽快安排专人为您解答。',
	'rule1' => array(
		'keywords'  => array('案例', '合作伙伴'),
		'reply'     => '多盟经典案例：http://www.domob.cn/case/case.htm'
	),
	'rule2' => array(
		'keywords'  => array('客服', '电话', '网址', '官网', '合作', '推广', '首页'),
		'reply'     => "多盟官网：www.domob.cn\n合作邮箱：BD@domob.cn\n客服电话：400-6368-168\n\n广告主快捷入口：http://www.domob.cn/sponsor/sponsor.htm?t=tab0\n开发者快捷入口：http://www.domob.cn/developers/developers.htm?t=tab0"
	),
	'rule3' => array(
		'keywords'  => array('工具', 'sdk', 'SDK', '开发工具', '积分墙'),
		'reply'     => '多盟开发者平台：http://www.domob.cn/developers/developers.htm?t=tab0'
	),
	'rule4' => array(
		'keywords'  => array('公司简介', '介绍', '多盟介绍'),
		'reply'     => '多盟（Domob），中国第一智能手机广告平台，成立于2010年9月。多盟整合了智能手机领域最优质的应用以及广告资源，搭建了广告主和应用开发者之间的广告技术服务平台。并借助大规模数据处理的平台优势以及贴近应用开发者的服务模式，为应用开发者提供产品推广服务和收益，以及为致力于在智能手机平台推广产品、品牌的广告主提供高效的服务。多盟提供了公平、合理、高效的资源配置平台，为应用开发者和广告主创造价值最大化。多盟拥有以业内资深专家及知名高级工程师为核心的研发队伍，对广告平台系统拥有独特的技术优势。团队在互联网行业有多年的积累，拥有丰富的广告资源，多盟希望给行业带来独特的价值。移动互联网将因广告而更精彩！'
	),
	'rule5' => array(
		'keywords'  => array('新闻', '动态'),
		'reply'     => 'http://www.domob.cn/news/index.htm?t=tab0'
	),
	'rule6' => array(
		'keywords'  => array('优势', '比其他平台', '特点', '对比'),
		'reply'     => " 一、高额的收入回报：多盟所获广告收入与开发者三七分成，目前多盟系统中不乏日均收入2万的媒体\n\n二、丰富的广告资源：多盟与众多优质广告主合作，确保广告填充率99%以上，保证点击率的同时提升开发者的收入\n\n三、强大的技术力量：多盟拥有独特的技术优势，保证系统稳定运行的同时，为开发者的日常技术问题提供解决方案\n\n四、多样化的广告样式：支持Banner、插屏、开屏、互动式插屏、文字链、富媒体等多种展现样式\n\n五、精准的数据统计：为开发者提供精确的数据依据，统计系统公平、透明计算广告收入，开发者可实时监测\n\n六、完善的服务：多盟保证新提交应用的快速审核；对开发者广告费用提现审核及时响应，快速到帐"
	),
	'rule7' => array(
		'keywords'  => array('小编', '你好', '在不', '在吗', '有人吗？'),
		'reply'     => '大神有何吩咐？'
	),
	'rule8' => array(
		'keywords'  => array('充值卡', '抢', '手机卡', '50', '电话卡', '活动'),
		'reply'     => '充值卡活动随机抽取哈，请亲们耐心等待，敬请持续关注domob微信活动通告。'
	),
	'rule9' => array(
		'keywords'  => array('第一智能手机广告平台','多盟抽奖'),
		'reply'     => array(
			array(
				'Title'         => 'Domob多盟 幸运大转盘',
				'Description'   => '点击玩转幸运大转盘',
				'PicUrl'        => 'http://duomengwx.moxz.cn/service/images/banner.jpg',
				'Url'           => 'hhttp://duomengwx.moxz.cn/choujiang/index2.htm?uid=%s'
			)
		)
	),
	'rule10' => array(
		'keywords' => array('抽奖统计'),
		'reply' => array(
			'func' => 'LotteryCount'
		)
	),
	'rule11' => array(
		'keywords' => array('兑奖'),
		'reply' => array(
			'func' => 'Lottery'
		)
	),
	
);
