#!/bin/bash

Main() {
	if [ $# != 3 ]; then
		if [ ! -d "chapter$1" ]; then
			mkdir chapter$1 && cd chapter$1;

			for i in `seq -w 01 $2`; do
				if [ ! -f "program$1_$i" ]; then
					touch  "program$1_$i.c";
					echo "// author <pemakoa@gmail.com>

#include <stdio.h>

int main(void)
{
	
	return 0;
}" > "program$1_$i.c";
					echo "program$1_$i.c";
				else
					echo "program$1_$i 文件已存在";
				fi
			done;
		else
			echo "需要创建的文件夹已存在，请换一个名称";
			exit 1
		fi
	else
		echo "请输入要创建的文件夹名称 及需要生成的文件个数";
		exit 2;
	fi

}

# 输入的第一个参数为需要创建的文件夹名称 文件名默认加上 chapter
# 第二个参数为需要在该文件夹下生成的文件个数,文件名默认 program
Main $1 $2