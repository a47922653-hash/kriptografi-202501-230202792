def encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def decrypt(ciphertext, key):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift - key) % 26 + shift)
        else:
            result += char
    return result

if __name__ == "__main__":
    print("=== Program Caesar Cipher ===")
    mode = input("Pilih mode [e=encrypt / d=decrypt]: ").strip().lower()

    while mode not in {"e", "d"}:
        mode = input("Mode tidak valid. Pilih [e/d]: ").strip().lower()

    text = input("Masukkan teks: ")

    while True:
        try:
            key = int(input("Masukkan key (bilangan bulat): ").strip())
            break
        except ValueError:
            print("Key harus bilangan bulat. Coba lagi.")


    key = key % 26

    if mode == "e":
        cipher = encrypt(text, key)
        print("\n=== HASIL ENKRIPSI ===")
        print("Plaintext :", text)
        print("Key Norm  :", key)
        print("Ciphertext:", cipher)
    else:
        plain = decrypt(text, key)
        print("\n=== HASIL DEKRIPSI ===")
        print("Ciphertext:", text)
        print("Key Norm  :", key)
        print("Plaintext :", plain)
