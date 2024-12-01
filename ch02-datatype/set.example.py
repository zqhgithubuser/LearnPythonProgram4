small_primes = set()

small_primes.add(2)
small_primes.add(3)
small_primes.add(5)
print(small_primes)  # {2, 3, 5}

small_primes.add(1)
print(small_primes)  # {1, 2, 3, 5}

small_primes.remove(1)
print(small_primes)  # {2, 3, 5}

bigger_primes = {5, 7, 11, 13}
print(small_primes | bigger_primes)  # {2, 3, 5, 7, 11, 13}
print(small_primes & bigger_primes)  # {5}
print(small_primes - bigger_primes)  # {2, 3}


small_primes = frozenset([2, 3, 5, 7])
bigger_primes = frozenset([5, 7, 11])
# small_primes.add(11)
print(small_primes & bigger_primes)  # frozenset({5, 7})
