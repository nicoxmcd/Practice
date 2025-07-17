apples = [7,4,2,1]
containers = [2,9,2,1,3]

# how many containers does it take to store all the apples?
# All the apple = so just the total number of apples
# if we store the apples as is in the containers listed it would probably take more apples
# SO lets make the biggest container come first
# AI said my code was pretty efficient :)

total_apples = 0

for item in apples:
    total_apples += item

containers.sort(reverse=True)

print(total_apples) # Good, prints 16
print(containers)

total_containers = 0

# Fitting the apples into the containers
for apple_container in containers:
    # Loop should stop if apples is equal to or less than 0
    if total_apples <= 0:
        break
    # if there are more than 0 or equal to 0 apples after subtracting from the container
    elif total_apples - apple_container >= 0:
        # subtract container amount from total_apples, make container 0
        total_apples -= apple_container
        print(str(total_apples) + " total apples remain")
        # if there's leftover apples after subtracting, consider container at 0 and add to total apple_containers
        total_containers += 1    
        continue

    elif total_apples - apple_container < 0:
        total_containers += 1
        break

print(total_containers)