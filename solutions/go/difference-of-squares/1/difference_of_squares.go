package diffsquares

func SquareOfSum(n int) int {
	var s int
	for i := range n + 1 {
		s += i
	}
	return s * s
}

func SumOfSquares(n int) int {
	var s int
	for i := range n + 1 {
		s += i * i
	}
	return s
}

func Difference(n int) int {
	return SquareOfSum(n) - SumOfSquares(n)
}
