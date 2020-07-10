def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    pos = {}
    neg = {}
    for i in range(0, len(a)):
        if a[i] > 0:
            if a[i] not in pos:
                pos[a[i]] = 1
            elif a[i] in pos:
                pos[a[i]] += 1
        if a[i] < 0:
            if a[i] not in neg:
                neg[a[i]] = 1
            elif a[i] in pos:
                neg[a[i]] += 1
    
    for key in pos:
        if (key * -1) in neg:
            result.append(key)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))


    """
    In this code, it creates separate caches for the positive and negative numbers
    it adds every positive number to the pos dictionary, and every negative number to the neg dictionary
    the key is the number, the value is how often it shows up in the array
            note: this is probably not the most efficient way of doing it, but if the array looks like [1,1,1,1,-2,-2,-2,-2,-1]
            then the pos cache is {1:4} and the neg cache is {-2:4, -1:1}. so it only references each individual number once
            there is probably a quicker way of doing it, but this way is still faster than storing every positive number in an array and every negative number in an array, so I digress
    
    it then loops through every key in the positive cache, and searches for the (itself * -1) in the negative cache
    if it exists, it appends the value to the results array
    
    after the loop is complete, it returns the result array

    """