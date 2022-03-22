def findPrimeFactors(num):

    primeNumbers = [2, 3, 5, 7, 11, 13,17,19,23,29,31]
    primeFactors= []

    for i in primeNumbers:
        while num % i == 0:
            num = num / i
            primeFactors.append(i)

    return primeFactors

print(findPrimeFactors(26))