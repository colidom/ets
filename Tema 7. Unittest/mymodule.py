#!/usr/bin/env python
# -*- coding: utf-8 -*-
def sum(a, b):
    """
    Retorna a + b.
    
    >>> sum(5, 7)
    12
    >>> sum(5, "Python")
    Traceback (most recent call last):
        ...
    TypeError
    """
    for n in (a, b):
        if not isinstance(n, int) and not isinstance(n, float):
            raise TypeError
    return a + b

def get_prime_numbers(max_number):
    """
    Retorna una lista de números primos.
    
    >>> get_prime_numbers(10)
    [2, 3, 5, 7]
    """
    numbers = [True, True] + [True] * (max_number-1)
    last_prime_number = 2
    i = last_prime_number
    
    while last_prime_number**2 <= max_number:
        i += last_prime_number
        while i <= max_number:
            numbers[i] = False
            i += last_prime_number
        j = last_prime_number + 1
        while j < max_number:
            if numbers[j]:
                last_prime_number = j
                break
            j += 1
        i = last_prime_number
    
    return [i + 2 for i, not_crossed in enumerate(numbers[2:]) if not_crossed]

def is_prime(n):
    """
    Determina si n es primo.
    
    >>> is_prime(5)
    True
    >>> is_prime(6)
    False
    """
    return n in get_prime_numbers(n)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
