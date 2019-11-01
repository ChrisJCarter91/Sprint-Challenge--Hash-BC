#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    So we need our liked pairs to match so the values connect.
        IE SLC flies to PIT which flies to ORD so we need to connect these tickets
    Need to loop through the tickets
    check for no source for starting point
    if not none, insert source and destination to the hash table
    loop the route
    next route will start with destination from the previous (-1)
    """
    for t in tickets:
        hash_table_insert(hashtable, t.source, t.destination)

    current = hash_table_retrieve(hashtable, "NONE")
    route[0] = current
    counter = 0
    while current is not "NONE":
        counter += 1
        current = hash_table_retrieve(hashtable, current)
        route[counter] = current

    return route
