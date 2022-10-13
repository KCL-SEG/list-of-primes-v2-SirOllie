"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    currentInt = 2
    checkingInt = 1

    if number_of_primes < 0:
        raise ValueError("value given is not valid (negative)")
    elif number_of_primes == 0:
        raise ValueError("value given is not valid (zero)")
    else:
        while number_of_primes > 0:
            if checkingInt > 1 and (currentInt % checkingInt != 0):
                checkingInt = checkingInt - 1
            else:
                if checkingInt == 1:
                    list.append(currentInt)
                    number_of_primes = number_of_primes - 1
                    currentInt = currentInt + 1
                    checkingInt = currentInt - 1
                else:
                    currentInt = currentInt + 1
                    checkingInt = currentInt - 1
        return list
