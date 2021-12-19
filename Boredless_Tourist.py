destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
attractions = []
#attractions_2 = [attractions_2.append(destinations) for destination in destinations]

#Create an attractions 2D list with destinations
#for destination in destinations:
#    attractions.append([destination])

# Create an attractions empty 2D list
for destination in destinations:
    attractions.append([])

print(attractions)

def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index

def get_traveler_location(traveler):
    traveler_destination = test_traveler[1]  
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index

def add_attraction(destination, attraction):
    get_destination_index(destination)

#First we should attempt to find the index of the destination. 
# Use get_destination_index() with the passed in destination in order to retrieve the 
# index of the destination. Save the results into destination_index.


test_destination_index = get_traveler_location(test_traveler[1])
print(test_destination_index)