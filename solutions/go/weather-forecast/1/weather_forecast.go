/*
Package weather: Weather forecast package.
*/
package weather

// CurrentCondition: Holds a description of the current weather condition.
var CurrentCondition string
// CurrentLocation: The name of the current location for which the forecast is being made.
var CurrentLocation string

// Forecast: Output weather forecast for a `city` based on the current weather `condition`.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
