package lasagna

// TODO: define the 'PreparationTime()' function
func PreparationTime(layers []string, timePerLayer int) int {
	if timePerLayer == 0 {
		timePerLayer = 2
	}
	return len(layers) * timePerLayer
}

// TODO: define the 'Quantities()' function
func Quantities(layers []string) (int, float64) {
	var noodles int = 0
	var sauce float64 = 0.0
	for i:= 0; i < len(layers); i++ {
		if layers[i] == "noodles" {
			noodles += 50
		}
		if layers[i] == "sauce" {
			sauce += 0.2
		}
	}
	return noodles, sauce

}

// TODO: define the 'AddSecretIngredient()' function
func AddSecretIngredient(friendsList []string, myList []string) []string{
	return append(myList, friendsList[len(friendsList) - 1])
}

// TODO: define the 'ScaleRecipe()' function
func ScaleRecipe(amountsForTwo []float64, portions int) []float64 {
	var newAmounts []float64
	for i:= 0; i < len(amountsForTwo); i++ {
		newAmounts = append(newAmounts, amountsForTwo[i] / 2.0 * float64(portions))
	}
	return newAmounts
}
