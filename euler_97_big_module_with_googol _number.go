package main

import (
	"fmt"
	"math/big"
	
)

func main() {
	a := big.NewInt(28433)
	b := uint(7830457)
	c, _ := new(big.Int).SetString("10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",0)
	a.Lsh(a,b)
	a.Mod(a,c)
	fmt.Println(a.Add(a,big.NewInt(1)))
}
