package main

import "fmt"

type Human struct {
	name string
	age int
	phone string
}

type Student struct {
	Human
	school string
}

type Employee struct {
	Human
	company string
}

// Human 定义 mehtod
func (h *Human) SayHi() {
	fmt.Printf("Hi, I am %s you can call me on %s\n", h.name, h.phone)
}

// Employee 的 method 重写 Human 的 method
func (e *Employee) SayHi() {
	fmt.Printf("Hi, I am %s, I work at %s. Call me on %s\n", e.name,
		e.company, e.phone) // Yes you can split into 2 lines here
}

func main() {
	mark := Student{Human{"Mark", 25, "222-222-yyy"}, "MIT"}
	sam := Employee{Human{"Sam", 45, "111-888-xxxx"}, "Golang Inc"}

	mark.SayHi()
	sam.SayHi()
}
