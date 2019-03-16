#### 本节学习内容 VIM知识讲解

##### 第一讲
- 光标移动
	
	要移动光标，注意要在正常模式下(注意要输入法不要在中文状态下)分别按下 h h k l 键

- vim的进入和退出
	
	请按<ESC>键（确保处在正常模式下）
	
	然后输入 :q!<回车> 这种方式退出编辑器不会保存原来编辑过的内容
	
	如果想要保存后再退出，输入 :wq<回车>

- vim编辑之删除
	
	在正常(Normal)模式下，可以按下 x 键来删除光标所在位置的字符
	
	"下面这一行是进行测试的文字，请删除本句话中的'测试'文字"

- vim编辑之插入
	
	在正常模式下，可以按下 i 键来插入文本
	
	"在正常模式下，可以按下 i 键来插入文本" 在该句话的"正常"修改为"编辑"

- 总结

	光标在屏幕文本中的移动既可以使用箭头键，也可以使用 h(左移) j(下行) k(上行) l(右移) 字母键

	欲进入vim编辑器(从命令行提示符)，请输入 vim 文件名 <回车>
	
		eg： vim study.txt （如果study.txt 文件存在则表示直接打开，不存在则表示创建） 

	欲退出编辑器

		<ESC> :q! <回车> 放弃所有修改

		<ESC> :w <回车> 保存编辑的内容不退出

		<ESC> :wq <回车> 保存并退出

		<ESC> :x <回车> 保存并退出等同于 :wq

	在正常模式下删除光标所在位置的字符，输入 :x

	在正常模式下要在光标所的位置插入文本，输入 i 输入必要文本 <ESC>


- 其他删除命令
	
	在正常模式下，输入以下命令 

	输入 dd 表示删除改行文字

	输入 ndd 表示删除从当前行 共n行

	输入 dw 表示删除当前位置知道单词末尾，包括空格

	输入 de 表示删除当前位置知道单词末尾，不包括空格

	输入 d$ 表示从当前光标位置直到当前行末
 
- 若撤销之前的操作，输入 u(小写的u)

- 若撤销在一行中所做的改动，请输入 U(大写的U)

- 下面的是进行练习的文字

```
root:*:0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1:System Services:/var/root:/usr/bin/false
_uucp:*:4:4:Unix to Unix Copy Protocol:/var/spool/uucp:/usr/sbin/uucico
_taskgated:*:13:13:Task Gate Daemon:/var/empty:/usr/bin/false
_networkd:*:24:24:Network Services:/var/networkd:/usr/bin/false
_networkd:*:24:24:Network Services:/var/networkd:/usr/bin/false
_networkd:*:24:24:Network Services:/var/networkd:/usr/bin/false
_networkd:*:24:24:Network Services:/var/networkd:/usr/bin/false
_networkd:*:24:24:Network Services:/var/networkd:/usr/bin/false
```

[参考](http://www.cnblogs.com/hustskyking/archive/2013/06/11/linux-learning-details.html)

<center>[下一节](./len02)</center>
