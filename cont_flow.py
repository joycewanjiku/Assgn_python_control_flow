# NEW ASSIGNMENTDue 20 Apr
# Control Flow
# Write a function that uses while, if and continue statements to print all the even numbers between 0 and 50. 
def even_numbers():
    x=10
    while x<=50:
        x+=1
        if x%3==0:
            continue
        print(x)

# Write a function that takes an integer argument and prints "Prime" if the number is prime, and "Not prime" if the number is not prime.
def prime_numbers():
    x=range(4,20)
    for i in x:
        if i %2==0:
            print(f"{i}is prime number")
    else:
        print(f"{i} is not prime")
 


# Write a function that takes a list of integers as input and prints the sum of all the even numbers in the list.
# def integers():.def prime_numbers():
def sum_even():
    sum-0
    for i in range(0,50):
        if i%2==0:
            sum=+1
            print(sum)
    

# Write a function that takes any two integers as input, and prints the sum of all the numbers between the two integers (inclusive) 
# that are divisible by 3
def divide_by_five(num2,num3):
     sum=0
     for i in range(num2,num3):
        if i%3==0:
            sum+=i

        print(sum)
