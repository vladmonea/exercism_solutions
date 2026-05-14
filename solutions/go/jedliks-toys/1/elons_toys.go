package elon

import "fmt"

// TODO: define the 'Drive()' method
func (c *Car) Drive() *Car {
	battery := c.battery - c.batteryDrain
	if battery < c.batteryDrain {
		return c
	} else {
		c.battery = battery
	}
	c.distance = c.distance + c.speed
	return c
	
}

// TODO: define the 'DisplayDistance() string' method
func (c Car) DisplayDistance() string {
	return fmt.Sprintf("Driven %v meters", c.distance)
}

// TODO: define the 'DisplayBattery() string' method
func (c Car) DisplayBattery() string {
	return fmt.Sprintf("Battery at %v%%", c.battery)
}

// TODO: define the 'CanFinish(trackDistance int) bool' method
func (c Car) CanFinish(trackDistance int) bool {
	return ((trackDistance - c.distance) / c.speed ) * c.batteryDrain <= c.battery
}
