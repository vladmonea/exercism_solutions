package etl

var upperToLower = map[string]string{
	"A": "a", "B": "b", "C": "c", "D": "d", "E": "e", "F": "f", "G": "g", "H": "h", "I": "i", "J": "j", "K": "k", "L": "l", "M": "m", "N": "n", "O": "o", "P": "p", "Q": "q", "R": "r", "S": "s", "T": "t", "U": "u", "V": "v", "W": "w", "X": "x", "Y": "y", "Z": "z",
}

func Transform(in map[int][]string) map[string]int {
	output := map[string]int{}
	for key, values := range in {
		for _, value := range values {
			output[upperToLower[value]] = key
		}
	}
	return output
}
