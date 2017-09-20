// 环境变量 os.Setenv 来设置一个键值对。os.Getenv 获取一个健对应的值
// 如果健不存在，将返回一个空字符串
// 使用 os.Environ 来列出所有环境变量键值对

package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	os.Setenv("FOO", "1")
	fmt.Println("FOO:", os.Getenv("FOO"))
	fmt.Println("BAR:", os.Getenv("BAR"))

	fmt.Println()
	for _, e := range os.Environ() {
		fmt.Println(e)
		pair := strings.Split(e, "=")
		fmt.Println(pair[0])
	}
}
