# Linear time O(n)
def linear(n):
    sum = 1
    for x in range(n):
        sum += x
    print(sum)

def constant(n):
    sum = n*(n-1)/2
    print(sum)

def main():
    print("Hello World")
    user = int(input("enter a number "))
    print("linear time sum")
    linear(user)
    print("constant time sum")
    constant(user)

if __name__ == "__main__": 
    main()