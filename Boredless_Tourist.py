destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
traveler_destination_index = location_object.get_destination_index(location_object.get_traveler_location.traveler_destination)

class Location:
    def get_destination_index(destination):
        destination_index = destinations.index(destination)
        return destination_index

    def get_traveler_location(traveler):
        # traveler_destination = destinations[get_destination_index.destination_index]
        traveler_destination = test_traveler[1]
        return traveler_destination_index

location_object = Location()