package main

import (
	"encoding/json"
	"fmt"
	"os"
)

type Response1 struct {
	Page   int
	Fruits []string
}

type Response2 struct {
	Page   int
	Fruits []string
}

func main() {
	bolB, _ := json.Marshal(true)
	fmt.Println(string(bolB))

	intB, _ := json.Marshal(1)
	fmt.Println(string(intB))

	fltB, _ := json.Marshal(2.34)
	fmt.Println(string(fltB))

	strB, _ := json.Marshal("gopher")
	fmt.Println(string(strB))

	slcD := []string{"apple", "peach", "pear"}
	fmt.Println(slcD)
	slcB, _ := json.Marshal(slcD)
	fmt.Println(string(slcB))

	mapD := map[string]int{"apple": 5, "lettuce": 7}
	mapB, _ := json.Marshal(mapD)
	fmt.Println(mapD)
	fmt.Println(string(mapB))

	res1D := &Response1{
		Page:   1,
		Fruits: []string{"apple", "peach", "pear"}}
	fmt.Println(res1D)
	res1B, _ := json.Marshal(res1D)
	fmt.Println(string(res1B))

	res2D := Response2{
		Page:   1,
		Fruits: []string{"apple", "peach", "pear"}}
	fmt.Println(res2D)
	res2B, _ := json.Marshal(res2D)
	fmt.Println(string(res2B))

	byt := []byte(`{"num":6.13, "strs":["a", "b"]}`)

	fmt.Println(string(byt))
	var dat map[string]interface{}

	if err := json.Unmarshal(byt, &dat); err != nil {
		panic(err)
	}
	fmt.Println(dat)

	num := dat["num"].(float64)
	fmt.Println(num)

	strs := dat["strs"].([]interface{})
	str1 := strs[0].(string)
	fmt.Println(str1)

	str := `{"page":1, "fruits":["apple", "peach"]}`
	res := &Response2{}
	json.Unmarshal([]byte(str), &res)
	fmt.Println(res)
	fmt.Println(res.Fruits[0])

	enc := json.NewEncoder(os.Stdout)
	d := map[string]int{"appke": 5, "lettuce": 7}
	enc.Encode(d)
}
