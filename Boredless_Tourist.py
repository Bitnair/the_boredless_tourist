destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
attractions = []
#Structure of attractions 3D list [[['ATTRACTION1', ['TAG1', 'TAG2']], ['ATTRACTION2', ['TAG1', 'TAG2']]],
#attractions_with_interest = []

# Create an empty 2D list for attractions
for destination in destinations:
    attractions.append([])


def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index

def get_traveler_location(traveler):
    traveler_destination = test_traveler[1]  
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index

def add_attraction(destination, attraction):
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index].append(attraction)
    if destination in destinations:
        attractions_for_destination
    else:
        destinations.append(destination)
        attractions_for_destination
     
def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index] #returns attractions + tags
    attractions_with_interest = [] #saved attractions matching our interests
        
    for attraction in attractions_in_city:
        possible_attraction = attraction
        attraction_tags = attraction[1]            
        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attraction[0])              
    return attractions_with_interest

def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)
    interests_string = 'Hi ' + traveler[0] + ", we think you'll like these places around "
    
    for attraction in traveler_attractions:
        

add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])




##TEST SECTION
# These are the attractions included in attractions list
# [[['the Louvre', ['art', 'museum']], ['Arc de Triomphe', ['historical site', 'monument']]], 
# [['Yu Garden', ['garden', 'historcical site']], ['Yuz Museum', ['art', 'museum']], ['Oriental Pearl Tower', ['skyscraper', 'viewing deck']]], 
# [['Venice Beach', ['beach']], ['LACMA', ['art', 'museum']]], 
# [['São Paulo Zoo', ['zoo']], ['Pátio do Colégio', ['historical site']]], 
# [['Pyramids of Giza', ['monument', 'historical site']], ['Egyptian Museum', ['museum']]]]
la_arts = find_attractions("Los Angeles, USA", ['art'])
print(la_arts)

print()

# >>> point 53