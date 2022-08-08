num = int(input("Enter a number" ))
prime_list = []
#method for checking if number is prime
def prime(n):
    c=0
    for i in range(1,n+1):
        if n % i == 0:
            c+=1
    if c == 2:
        return True
    else:
        return False        
x = prime(num)
num2 = num+1
if x == True:
    print("Number is prime")
    n = 0
    #Taking all 10 consecutive prime numbers after the number inputted and storing them in an array
    while n <= 10:
        l = prime(num2)
        if l == True:
            prime_list.append(num2)
            n+=1
            num2+=1
        else:
            num2+=1

print("The 10 consecutive prime numbers after",num,"is",prime_list)
lcm = 1
#LCM of the numbers would be just their multiplication
#because all of them are prime and have no common factor other than 1 
for a in range(len(prime_list)):
    lcm *= prime_list[a]
print("The LCM of the above numbers is:",lcm,"their HCF is 1 ")
