package space

type Planet string

func Age(seconds float64, planet Planet) float64 {
	switch planet {
	case "Mercury":
		return seconds / 3600.0 / 24.0 / 365.25 / 0.2408467
	case "Venus":
		return seconds / 3600.0 / 24.0 / 365.25 / 0.61519726
	case "Earth":
		return seconds / 3600.0 / 24.0 / 365.25
	case "Mars":
		return seconds / 3600.0 / 24.0 / 365.25 / 1.8808158
	case "Jupiter":
		return seconds / 3600.0 / 24.0 / 365.25 / 11.862615
	case "Saturn":
		return seconds / 3600.0 / 24.0 / 365.25 / 29.447498
	case "Uranus":
		return seconds / 3600.0 / 24.0 / 365.25 / 84.016846
	case "Neptune":
		return seconds / 3600.0 / 24.0 / 365.25 / 164.79132
	default:
		return 0.0
	}
}
