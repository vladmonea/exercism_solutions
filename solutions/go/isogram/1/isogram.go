package isogram

import (
	"strings"
	"unicode"
)

func IsIsogram(word string) bool {
	if len(word) == 0 {
		return true
	}
	isoMap := map[rune]int{}
	for _, c := range strings.ToLower(word) {
		if !unicode.IsLetter(c) {
			continue
		}
		_, ok := isoMap[c]
		if ok {
			return false
		} else {
			isoMap[c] = 1
		}
	}
	return true
}
