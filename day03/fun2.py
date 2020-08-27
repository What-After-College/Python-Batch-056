# def farh_to_cel(temp):
#     return ((temp - 32)*(5/9))



# celcius = farh_to_cel(-40)

# print(celcius)


# n = int(input("Enter n: "))
# r = int(input("Enter r: "))
# p = n-r
# n_fact = 1
# r_fact = 1
# p_fact = 1
# for i in range(1, n+1):
#     n_fact = n_fact*i


# for i in range(1, r+1):
#     r_fact = r_fact*i

# for i in range(1, p+1):
#     p_fact = p_fact*i

# ncr = n_fact/(r_fact*p_fact)
# print(ncr)

def fact(num):
    ans = 1
    for i in range(1, num+1):
        ans = ans*i
    return ans
n = int(input("Enter n: "))
r = int(input("Enter r: "))

ncr = fact(n)/(fact(r)*fact(n-r))
print(ncr)