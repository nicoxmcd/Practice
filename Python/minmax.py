
def minmax(arr):
    # Defining a very easy number to beat as the min, use the MAX constraint
    min = 9 ** 10
    # Defining a very easy number to beat as the max, use the MIN constraint, however if we were allowing negatives, make it same as min but negative
    max = 0 
    for item in arr:
        if item < min:
            min = item
        elif item > max:
            max = item
        else:
            continue
    print("max is " + str(max))
    print("min is " + str(min))


minmax([2,4,5,32,4,90, 32,0])
# time complexity is O(n) if the array was just a user based input  with endless indices