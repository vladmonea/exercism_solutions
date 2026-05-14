package dndcharacter

import (
	"math"
	"math/rand"
)

type Character struct {
	Strength     int
	Dexterity    int
	Constitution int
	Intelligence int
	Wisdom       int
	Charisma     int
	Hitpoints    int
}

var abilities = []string{"strength", "dexterity", "constitution", "intelligence", "wisdom", "charism", "hitpoints"}

// Modifier calculates the ability modifier for a given ability score
func Modifier(score int) int {
	subtractTen := float64(score - 10)
	divideByTwo := subtractTen / 2.0
	return int(math.Floor(divideByTwo))
}

// Ability uses randomness to generate the score for an ability
func Ability() int {
	throws := []int{}
	for range 4 {
		current := rand.Intn(6)
		if current == 0 {
			current = 1
		}
		throws = append(throws, current)
	}
	throws = removeMin(throws)
	return sumArray(throws)
}

func removeMin(array []int) []int {
	min := 6
	minPos := 0
	for i, v := range array {
		if v <= min {
			min = v
			minPos = i
		}
	}
	return append(array[:minPos], array[minPos+1:]...)
}

func sumArray(array []int) int {
	s := 0
	for i := range array {
		s += array[i]
	}
	return s
}

// GenerateCharacter creates a new Character with random scores for abilities
func GenerateCharacter() Character {
	strength := Ability()
	dexterity := Ability()
	constitution := Ability()
	intelligence := Ability()
	wisdom := Ability()
	charism := Ability()
	hitpoints := 10 + Modifier(constitution)
	return Character{strength, dexterity, constitution, intelligence, wisdom, charism, hitpoints}
}
