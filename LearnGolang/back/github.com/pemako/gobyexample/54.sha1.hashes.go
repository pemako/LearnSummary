package main

import (
	"crypto/md5"
	"crypto/sha1"
	"fmt"
	"io"
)

func main() {
	s := "sha1 this string"

	h := sha1.New()

	h.Write([]byte(s))

	bs := h.Sum(nil)

	fmt.Println(s)
	fmt.Printf("%x\n", bs)

	a := md5.New()
	io.WriteString(a, "The fog is getting thicker!")
	io.WriteString(a, "And Leon's getting laaarger!")
	fmt.Printf("%x", a.Sum(nil))
}
