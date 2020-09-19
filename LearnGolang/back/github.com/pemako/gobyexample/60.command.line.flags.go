// 命令行标志，Go 提供了一个 flag 包，支持基本的命令行标志解析。
// 基本的标记声明仅支持字符串、整数和布尔值选项

package main

import (
	"flag"
	"fmt"
)

func main() {
	// flag.String 函数返回一个字符串指针(不是一个字符串值)
	// 第一个参数为定义参数名，第二个参数为默认值，第三个参数为说明
	wordPtr := flag.String("word", "foo", "a string")

	numbPtr := flag.Int("numb", 42, "an int")
	boolPtr := flag.Bool("fork", false, "a bool")

	var svar string
	flag.StringVar(&svar, "svar", "bar", "a string var")

	flag.Parse()

	fmt.Println("word:", *wordPtr)
	fmt.Println("numb:", *numbPtr)
	fmt.Println("fork:", *boolPtr)
	fmt.Println("svar:", svar)
	fmt.Println("tail:", flag.Args())
}
