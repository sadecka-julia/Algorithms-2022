
def gcd(p, q):
    while q != 0:
        p, q = q, p % q
    return p


def is_coprime(x, y):
    return gcd(x, y) == 1


print(is_coprime(7878, 6725))
print(is_coprime(4417, 4741))
print(is_coprime(6706, 3749))
print(is_coprime(6975, 6661))
print(is_coprime(1072, 5565))
print(is_coprime(6657, 3875))
print(is_coprime(9752, 9808))
print(is_coprime(4800, 4004))
print(is_coprime(2259, 4017))
print(is_coprime(9234, 533))
print(is_coprime(7793, 3594))
print(is_coprime(6235, 928))
print(is_coprime(4998, 689))
print(is_coprime(2324, 5384))
print(is_coprime(4393, 4912))
print(is_coprime(7634, 80))
print(is_coprime(6706, 5347))
print(is_coprime(2154, 7617))
print(is_coprime(517, 8100))
print(is_coprime(3308, 3760))
