package speed

// TODO: define the 'Car' type struct
type Car struct{
	battery int
	batteryDrain int
	speed int
	distance int
}

// NewCar creates a new remote controlled car with full battery and given specifications.
func NewCar(speed, batteryDrain int) Car {
	return Car{speed: speed, batteryDrain: batteryDrain, battery: 100, distance: 0}
}

// TODO: define the 'Track' type struct
type Track struct{
	distance int
}

// NewTrack created a new track
func NewTrack(distance int) Track {
	return Track{distance: distance}
}

// Drive drives the car one time. If there is not enough battery to drive on more time,
// the car will not move.
func Drive(car Car) Car {
	if car.battery < car.batteryDrain {
		return car
	} else {
		var speed int = car.speed
		var batteryDrain int = car.batteryDrain
		var battery int = car.battery - car.batteryDrain
		var distance int = car.distance + car.speed
		return Car{speed: speed, batteryDrain: batteryDrain, battery: battery, distance: distance}
	}
}

// CanFinish checks if a car is able to finish a certain track.
func CanFinish(car Car, track Track) bool {
	if ((track.distance - car.distance) / car.speed ) * car.batteryDrain < car.battery {
		return true
	} else {
		return false
	}
}
