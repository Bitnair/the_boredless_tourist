destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
traveler_destination_index = ''


def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index

def get_traveler_location(traveler):
    traveler_destination = test_traveler[1]
    return traveler_destination_index

# print(get_destination_index('Los Angeles, USA'))
# destinations.index('Los Angeles, USA')
print(destinations)