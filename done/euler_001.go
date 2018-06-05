// Jesse Rubin ~ Project Euler
// p001

package main

import (
	"fmt"
	"strconv"
)

func threes_n_fives(upper_lim int) int {
	psum := 0
	for i := 1; i < upper_lim; i++ {
		if i%3 == 0 || i%5 == 0 {
			psum += i
		}
	}
	return psum
}

func main() {
	ANSWER := threes_n_fives(1000)
	fmt.Printf(strconv.Itoa(ANSWER))
}
