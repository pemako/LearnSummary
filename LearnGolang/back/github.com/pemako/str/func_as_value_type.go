package main

import (
	"fmt"
	"os"
)

type testInt func(int) bool // 声明一个函数类型

func isOdd(integer int) bool {
	if integer % 2 == 0 {
		return false
	}
	return true
}

func isEven(integer int) bool {
	if integer % 2 == 0 {
		return true
	}
	return false
}

// 声明的函数类型在这个地方当做一个参数
func filter(slice []int, f testInt) []int {
	var result []int
	for _, value := range slice {
		if f(value) {
			result = append(result, value)
		}
	}
	return result
}

var user = os.Getenv("USER")
func init() {
	if user == "" {
		panic("no value for $USER")
	}
}

func main() {
	slice := []int {1, 2, 3, 4, 5, 7}
	fmt.Println("slice = ", slice)
	odd := filter(slice, isOdd) // 函数当做值来传递
	fmt.Println("Odd elements of slice are: ", odd)
	even := filter(slice, isEven)
	fmt.Println("Even elements of slice are: ", even)

}
