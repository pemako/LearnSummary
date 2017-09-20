// os.Args 提供原始命令行参数访问功能。
// 注意：
// 切片中的第一个参数是该程序的路径，并且 os.Args[1:]保存所有程序的参数

package main

import (
	"fmt"
	"os"
)

func main() {
	argsWithProg := os.Args
	argsWithoutProg := os.Args[1:]

	arg := os.Args[3]

	fmt.Println(argsWithProg)
	fmt.Println(argsWithoutProg)
	fmt.Println(arg)
}
