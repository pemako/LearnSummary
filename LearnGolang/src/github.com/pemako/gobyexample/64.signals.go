// 信号处理
// os.Signal
// Go 通过向一个通道发送 os.Signal 值来进行信号通知
// 我们希望当服务器接收到一个 SIGTERM 信号时能够自动关机，
// 或者一个命令行工具在接收到一个 SIGINT 信号时停止处理输
// 入信息。这里讲的就就是在 Go 中如何通过通道来处理信号。

package main

import (
	"fmt"
	"os"
	"os/signal"
	"syscall"
)

func main() {
	sigs := make(chan os.Signal, 1)
	done := make(chan bool, 1)

	signal.Notify(sigs, syscall.SIGINT, syscall.SIGTERM)

	go func() {
		sig := <-sigs
		fmt.Println()
		fmt.Println(sig)
		done <- true
	}()

	fmt.Println("awaiting signal")
	<-done
	fmt.Println("exiting")

}
