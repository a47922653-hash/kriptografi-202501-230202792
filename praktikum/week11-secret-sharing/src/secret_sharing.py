import random

# Prime jauh lebih besar dari secret (aman untuk string pendek-menengah)
P = 2**521 - 1

def _b2i(b):
    return int.from_bytes(b, "big")

def _i2b(i, length):
    return i.to_bytes(length, "big")

def split_secret(secret, k, n):
    secret_bytes = secret.encode("utf-8")
    s = _b2i(secret_bytes)
    length = len(secret_bytes)

    if s >= P:
        raise ValueError("Secret terlalu besar untuk prime field yang dipakai. Perbesar P.")

    coeffs = [s] + [random.randrange(0, P) for _ in range(k - 1)]
    shares = []
    for x in range(1, n + 1):
        y = 0
        for i, a in enumerate(coeffs):
            y = (y + a * pow(x, i, P)) % P
        shares.append((x, y))

    return shares, length

def recover_secret(shares, length):
    # Lagrange interpolation di x=0
    res = 0
    for i, (xi, yi) in enumerate(shares):
        num = 1
        den = 1
        for j, (xj, _) in enumerate(shares):
            if i != j:
                num = (num * (-xj)) % P
                den = (den * (xi - xj)) % P
        li = num * pow(den, P - 2, P) % P
        res = (res + yi * li) % P

    return _i2b(res, length).decode("utf-8")

# ===== DEMO =====
secret = "KriptografiUPB2025"
shares, length = split_secret(secret, 3, 5)
print("Shares:", shares)

recovered = recover_secret(shares[:3], length)
print("Recovered secret:", recovered)
