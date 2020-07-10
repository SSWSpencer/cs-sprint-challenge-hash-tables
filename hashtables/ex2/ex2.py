#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    """
    in this code, a cache is created for all of the tickets, as well as an array for the route
    it loops through the original tickets, and stores the source as the key and the destination as the value
    it also appends the starting ticket's destination (source="NONE") to the beginning of the route

    then, it appends destinations to the route array similar to the way a singly-linked list is printed out
    it grabs the highest index currently existing in the route array, and references it in the cache. 
    doing that sets the referenced item to the referenced item's destination
    it then appends that to the route array
    it continues until the last destination added is "NONE",
    then it returns the route array



    in case that made 0 sense, here is an example of what happens:

    initial input:

        ticket_1 = Ticket("NONE", "PDX")
        ticket_2 = Ticket("PDX", "DCA")
        ticket_3 = Ticket("DCA", "NONE")
        tickets = [ticket_1, ticket_2, ticket_3]
        reconstruct_trip(tickets, 3)

    it will set the cache to be {none:pdx, pdx:dca, dca:none} and route to be [pdx]
    then it creates a variable curr to be equal to route[0], and references it in the cache (essentially cache[pdx])
    doing that will set curr = "dca" because that's what pdx references in the cache
    it appends dca to route, so route will be [pdx, dca]
    then it loops, recreating the variable curr to be equal to route[1], and references it in the cache
    doing it will set curr = "none" because that's what dca references in the cache
    it appends "none" to route, so route will be [pdx, dca, none]
    and finally it will break out of the loop because curr == "none"
    
    then it returns route

    """
    cache = {}
    route = []
    for x in range(0, len(tickets)):
        cache[tickets[x].source] = tickets[x].destination
        if tickets[x].source == "NONE":
            route.append(tickets[x].destination)
    
    index = 0
    while True: # for the first time in all of my time at lambda as well as my previous 3 years of java experience, this was probably the second time I've ever thought a do-while loop is the best way to go about a problem, and it turns out they don't exist natively in python.
        curr = cache[route[index]]
        index += 1
        route.append(curr)
        if curr == "NONE":
            break

    return(route)
