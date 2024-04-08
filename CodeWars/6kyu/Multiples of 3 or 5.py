# DESCRIPTION:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

# Additionally, if the number is negative, return 0.

# Note: If the number is a multiple of both 3 and 5, only count it once.

# Courtesy of projecteuler.net (Problem 1)

# SOLUTION:
def solution(number):
    #criação de um somatório
    sum = 0
    
    #Para o 'm' os valores de 1 até os numeros samples
    #Irão adicionar +1 no somatório de forem multiplos de 3 ou 5
    for m in range(1,number):
        if m % 3 == 0 or m % 5 == 0:
            sum += m
    return sum
  