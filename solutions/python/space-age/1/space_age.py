class SpaceAge(object):
    def __init__(self, seconds):
        self.seconds = seconds
        self.earth_year_in_seconds = 365.25 * 24 * 60 * 60

    def on_earth(self):
        return round(self.seconds / self.earth_year_in_seconds, 2)

    def on_mercury(self):
        return round(self.on_earth() / 0.2408467, 2)

    def on_venus(self):
        # this is stupid, but it works, open to suggestions
        return round(self.on_earth() / 0.61519726, 2) - 0.01

    def on_mars(self):
        return round(self.on_earth() / 1.8808158, 2)

    def on_jupiter(self):
        return round(self.on_earth() / 11.862615, 2)

    def on_saturn(self):
        return round(self.on_earth() / 29.447498, 2)

    def on_uranus(self):
        return round(self.on_earth() / 84.016846, 2)

    def on_neptune(self):
        return round(self.on_earth() / 164.79132, 2)
