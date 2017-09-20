package main

import "fmt"

func main() {
	// 方法一
	s := "hello"
	c := []byte(s) // 将字符串 s 转为 []byte 类型
	c[0] = 'c'
	s2 := string(c) // 在转换回 string 类型
	fmt.Printf("%s\n", s2)

	// 方法二
	s1 := "hello"
	s1 = "c" + s1[1:] // 字符串虽不能改变，但可以进行切片操作
	fmt.Printf("%s\n", s1)
}
