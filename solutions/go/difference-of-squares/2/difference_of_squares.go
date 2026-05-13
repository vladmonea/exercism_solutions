package diffsquares

func SquareOfSum(n int) int {
	var s int
	for i := 0; i <= n; i++ {
		s += i
	}
	return s * s
}

func SumOfSquares(n int) int {
	var s int
	for i := 0; i <= n; i++ {
		s += i * i
	}
	return s
}

func Difference(n int) int {
	return SquareOfSum(n) - SumOfSquares(n)
}
