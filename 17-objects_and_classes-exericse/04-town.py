class Town:
    def __init__(self, name: str):
        name = name
        latitude = ""
        longitude = ""

    def set_latitude(self, latitude):
        latitude = latitude

    def set_longitude(self, longitude):
        longitude = longitude

    def __repr__(self):
        return f'Town: {name} | Latitude: {latitude} | Longitude: {longitude}'

town = Town("Sofia")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)
