package raindrops

import "fmt"

func Convert(number int) string {
	if number == 1 {
		return "1"
	}
	var toReturn string = ""
	if number%3 == 0 {
		toReturn += "Pling"
	}
	if number%5 == 0 {
		toReturn += "Plang"
	}
	if number%7 == 0 {
		toReturn += "Plong"
	}
	if len(toReturn) == 0 {
		toReturn = fmt.Sprintf("%d", number)
	}
	return toReturn
}
