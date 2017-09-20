package main

import (
	"fmt"
	"runtime"
)

func say(s string) {
	for i := 0; i < 5; i++ {
		runtime.Gosched()
		fmt.Println(s)
	}
}

func main() {
	go say("world") // 开始一个新的 Goroutines执行
	say("hello") // 当前的 Goroutines 执行
}
