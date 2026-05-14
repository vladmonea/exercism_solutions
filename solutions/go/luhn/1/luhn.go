package luhn

import (
	"fmt"
	"strconv"
)

func Valid(id string) bool {
	if len(id) <= 1 {
		return false
	}
	var luhn int
	for i := len(id) - 1; i > 0; i -= 2 {
		a, err := strconv.Atoi(string(id[i-1]))
		if err != nil {
			continue
		}
		b, err := strconv.Atoi(string(id[i]))
		if err != nil {
			continue
		}
		luhn += a + 2*b
	}
	fmt.Printf("%v %v\n", id, luhn)
	return luhn%10 == 0
}
