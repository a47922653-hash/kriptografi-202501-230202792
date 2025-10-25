import math

Key = 26          # ukuran ruang kunci (Caesar Cipher)
A = 26          # ukuran alfabet
R = 0.75        # redundansi bahasa
CPS = 1e6       # kecepatan brute force (percobaan per detik)

# --- Langkah 1: Entropi ---
def entropy(keyspace_size):
    return math.log2(keyspace_size)

print("Entropy Caesar Cipher Kunci", Key, " =", entropy(Key), "bit")
print("Entropy AES Kunci 2^128 =", entropy(2**128), "bit")

# --- Langkah 2: Unicity Distance ---
def unicity_distance(HK, R=R, A=A):
    return HK / (R * math.log2(A))

HK = entropy(Key)
print("Unicity Distance Caesar Cipher =", unicity_distance(HK), "karakter")

# --- Langkah 3: Brute Force ---
def brute_force_time(keyspace_size, attempts_per_second=CPS):
    seconds = keyspace_size / attempts_per_second
    days = seconds / (3600 * 24)
    return days

print("Waktu brute force Caesar Cipher (", Key, "kunci) =", brute_force_time(Key), "hari atau", format (brute_force_time(Key), ".12f"), "hari")
print("Waktu brute force AES-128 =", brute_force_time(2**128), "hari")
