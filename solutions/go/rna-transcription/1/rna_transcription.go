package strand

var translationTable = map[rune]string{
	'A': "U", 'C': "G", 'G': "C", 'T': "A",
}

func ToRNA(dna string) string {
	if len(dna) == 0 {
		return ""
	}
	var translated string
	for _, n := range dna {
		translated += translationTable[n]
	}
	return translated
}
