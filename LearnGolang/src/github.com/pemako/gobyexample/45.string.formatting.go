package main

import (
	"fmt"
	"os"
)

type point struct {
	x, y int
}

func main() {
	p := point{1, 2}
	fmt.Printf("%v\n", p)

	// 如果值是一个结构体，%+v的格式化输出内容将包括结构体的字段名
	fmt.Printf("%+v\n", p)

	fmt.Printf("%#v\n", p)
	// %T打印值的类型
	fmt.Printf("%T\n", p)

	// %d机型标准的十进制格式化
	fmt.Printf("%d\n", 123)

	fmt.Printf("%b\n", 13)
	fmt.Printf("%c\n", 33)
	fmt.Printf("%x\n", 456)
	fmt.Printf("%f\n", 78.9)

	fmt.Printf("%e\n", 12345000000.0)
	fmt.Printf("%E\n", 12345000000.0)

	fmt.Printf("%s\n", "\"string\"")
	fmt.Printf("%q\n", "\"string\"")

	fmt.Printf("%x\n", "hex this")

	fmt.Printf("%p\n", &p)

	fmt.Printf("|%6d|%6d|\n", 12, 345)
	fmt.Printf("|%6.2f|%6.2f|\n", 1.2, 3.45)
	fmt.Printf("|%-6.2f|%-6.2f|\n", 1.2, 3.45)
	fmt.Printf("|%6s|%6s|\n", "foo", "b")
	fmt.Printf("|%-6s|%-6s|\n", "foo", "b")

	s := fmt.Sprintf("a %s", "string")
	fmt.Println(s)

	fmt.Fprintf(os.Stderr, "an %s\n", "error")
}
