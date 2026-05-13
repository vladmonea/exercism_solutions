package thefarm

import (
	"errors"
	"fmt"
	"strconv"
)

// See types.go for the types defined for this exercise.

// TODO: Define the SillyNephewError type here.
type SillyNephewError struct {
	message string 
	details string
}

func (sne SillyNephewError) Error() string {
	return fmt.Sprintf(sne.message, sne.details)
}

// DivideFood computes the fodder amount per cow for the given cows.
func DivideFood(weightFodder WeightFodder, cows int) (float64, error) {
	weight, err := weightFodder.FodderAmount()
	if err == ErrScaleMalfunction {
		weight *= 2
	} else if err != nil {
		return 0.0, err
	}
	if weight < 0 {
		return 0.0, errors.New("negative fodder")
	}
	if cows == 0 {
		return 0.0, errors.New("division by zero")
	} else if cows < 0 {
		return 0.0, &SillyNephewError{"silly nephew, there cannot be %v cows", strconv.Itoa(cows)}
	}
	return weight / float64(cows), nil
}
