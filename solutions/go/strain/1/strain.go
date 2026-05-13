package strain

type GenericInput interface {
	int | string | []int | []string
}

func Keep[GI GenericInput](in []GI, predicate func(GI) bool) []GI {
	var output []GI
	for i := range in {
		if predicate(in[i]) {
			output = append(output, in[i])
		}
	}
	return output
}

func Discard[GI GenericInput](in []GI, predicate func(GI) bool) []GI {
	var output []GI
	for i := range in {
		if !predicate(in[i]) {
			output = append(output, in[i])
		}
	}
	return output
}
