package chessboard

// Declare a type named Rank which stores if a square is occupied by a piece - this will be a slice of bools
type Rank [8]bool

// Declare a type named Chessboard contains a map of eight Ranks, accessed with values from "A" to "H"
type Chessboard map[string]Rank

// CountInRank returns how many squares are occupied in the chessboard,
// within the given rank
func CountInRank(cb Chessboard, rank string) int {
	var count int = 0
	file, fileExists := cb[rank]
	if !fileExists {
		return 0
	}
	for square := range file {
		if file[square] == true {
			count += 1
		}
	}
	return count
}

// CountInFile returns how many squares are occupied in the chessboard,
// within the given file
func CountInFile(cb Chessboard, file int) int {
	if file > 8 || file < 1{
		return 0
	}
	var count int = 0
	for _, files := range cb {
		if files[file - 1] == true {
			count += 1
		}
	}
	return count
}

// CountAll should count how many squares are present in the chessboard
func CountAll(cb Chessboard) int {
	var count int = 0
	for _, files := range cb {
		count += len(files)
	}
	return count
}

// CountOccupied returns how many squares are occupied in the chessboard
func CountOccupied(cb Chessboard) int {
	var count int = 0
	for rank := range cb {
		count += CountInRank(cb, rank)
	}
	return count
}
