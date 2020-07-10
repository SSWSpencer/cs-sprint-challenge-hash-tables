def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here


"""
     this code stores every value of weights in a cache
     the keys of the cache are every value in the weights array/list/whatever they're called in python #js4life
     the keys' values are whatever number is required to be found elsewhere in the weights list for their sum to equal limit
              for example, if weights == [1,3,4,6] and limit = 10, cache would be{1:9, 3:7, 4:6, and 6:4}
     the keys of cache are looped through, and in each iteration, the key's value is searched for in cache
              so with the previous example, when it loops through [1,3,4,6], when it's on 1, it searches for 9 in the cache, when it's on 3 it searches for 7 in the cache, and so on
     if it finds two values that add up to the limit, it sets them to a and b, and breaks out of the loop
     if a match was not found in the list, a will be equal to the last key, and b will remain NoneType
     if a and b both have values, there is a sum of two numbers in the weights array that equals limit
     it will then return their indexes from the original weights array
     otherwise, a match was not found, and it will return none

"""
    cache = {}
    for x in weights:
        cache[x] = limit - x

    a = None
    b = None

    for key in cache:
        a = key
        if cache[key] in weights:
            b = cache[key]
            break
    
    if a is not None and b is not None:
        return [weights.index(b, (weights.index(a)+1)), weights.index(a)]
    else:
        return None
