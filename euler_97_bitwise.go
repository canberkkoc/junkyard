// https://projecteuler.net/problem=97
package main

import (
	"fmt"
)

func main() {
	a := uint64(28433)
	for i := 0; i < 7830457; i++ {
		if (a & 0x8000000000000000) == 0x8000000000000000 {
			a = a % 10000000000
		}
		a = a << 1

	}
	fmt.Println(a%10000000000 + 1)
}
