destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
traveler_destination_index = ''


def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index

def get_traveler_location(traveler):
    traveler_destination = test_traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index
    
test_destination_index = get_traveler_location(test_traveler[1])

#Use traveler_destination along with get_destination_index() to retrieve the index of the destination 
# where the traveler is. Save the index of the traveler’s destination into the 
# variable traveler_destination_index.
