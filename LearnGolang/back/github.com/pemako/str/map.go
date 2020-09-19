package main

import "fmt"

func main() {
	rating := map[string]float32{"C":5, "Go":4.5, "Python":4.5, "C++":2}
	csharpRating, ok := rating["C#"]
	if ok {
		fmt.Println("C# is in the map and its rating is ", csharpRating)
	} else {
		fmt.Println("We have no rating associated with C# in the map")
	}

	delete(rating, "C")
}
