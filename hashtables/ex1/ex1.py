#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    weight will = weights[i]
    weight_limit = limit - weight
    weight_limit will be index_pair
    as long as index_pair isn't none and is more than i, it'll be index_pair first or it will return i first
    insert into table?
    """
    for i in range(length):
        weight = weights[i]
        weight_limit = limit - weight
        index_pair = hash_table_retrieve(ht, weight_limit)
        if index_pair is not None:
            answer = (index_pair, i) if i < index_pair else(i, index_pair)
            return answer
        hash_table_insert(ht, weight, i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
