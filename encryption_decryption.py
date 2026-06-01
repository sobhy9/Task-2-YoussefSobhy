# ============================================================

#   DecodeLabs | Cyber Security - Project 2
#   Basic Encryption & Decryption (Caesar Cipher + XOR)
#   Batch: 2026 | Author: Intern
# ============================================================

# ── CAESAR CIPHER ────────────────────────────────────────────

def caesar_encrypt(text: str, shift: int) -> str:
    """Encrypt plain text using Caesar cipher with a given shift key."""
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(encrypted_char)
        else:
            result.append(char)   # keep digits, spaces, punctuation as-is
    return ''.join(result)


def caesar_decrypt(cipher_text: str, shift: int) -> str:
    """Decrypt Caesar-encrypted text by reversing the shift."""
    return caesar_encrypt(cipher_text, -shift)   # decryption = negative shift


# ── XOR CIPHER ───────────────────────────────────────────────

def xor_encrypt(text: str, key: int) -> str:
    """Encrypt text using XOR bit operation with a single-byte key (0-255)."""
    return ''.join(chr(ord(char) ^ key) for char in text)


def xor_decrypt(cipher_text: str, key: int) -> str:
    """Decrypt XOR-encrypted text (XOR is its own inverse)."""
    return xor_encrypt(cipher_text, key)          # XOR is self-reversing


# ── DISPLAY HELPERS ──────────────────────────────────────────

def divider(char: str = "─", width: int = 55) -> None:
    print(char * width)


def section_header(title: str) -> None:
    divider("═")
    print(f"  {title}")
    divider("═")


# ── MAIN MENU ────────────────────────────────────────────────

def main():
    print()
    section_header("DecodeLabs | Cyber Security – Project 2")
    print("  Basic Encryption & Decryption  |  Batch 2026")
    divider()

    print("\nChoose a cipher:")
    print("  [1] Caesar Cipher  (shift-based, letters only)")
    print("  [2] XOR Cipher     (bitwise, all characters)")
    print("  [3] Run Demo       (see both ciphers in action)")
    print("  [0] Exit")
    divider()

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        caesar_mode()

    elif choice == "2":
        xor_mode()

    elif choice == "3":
        run_demo()

    elif choice == "0":
        print("\n  Goodbye! Keep building, keep securing. 🛡\n")

    else:
        print("\n  Invalid choice. Please restart and try again.")

    print()


# ── CAESAR MODE ──────────────────────────────────────────────

def caesar_mode():
    section_header("Caesar Cipher")

    text = input("Enter text to encrypt: ")

    while True:
        try:
            shift = int(input("Enter shift key (1-25): "))
            if 1 <= shift <= 25:
                break
            print("  ⚠  Please enter a number between 1 and 25.")
        except ValueError:
            print("  ⚠  Invalid input. Enter a whole number.")

    encrypted = caesar_encrypt(text, shift)
    decrypted = caesar_decrypt(encrypted, shift)

    divider()
    print(f"  Original Text  : {text}")
    print(f"  Shift Key      : {shift}")
    divider()
    print(f"  Encrypted Text : {encrypted}")
    print(f"  Decrypted Text : {decrypted}")
    divider()
    print("  ✅  Encryption & Decryption complete!")


# ── XOR MODE ─────────────────────────────────────────────────

def xor_mode():
    section_header("XOR Cipher")

    text = input("Enter text to encrypt: ")

    while True:
        try:
            key = int(input("Enter XOR key (1-255): "))
            if 1 <= key <= 255:
                break
            print("  ⚠  Please enter a number between 1 and 255.")
        except ValueError:
            print("  ⚠  Invalid input. Enter a whole number.")

    encrypted = xor_encrypt(text, key)
    decrypted = xor_decrypt(encrypted, key)

    # XOR output can contain non-printable characters, so we show hex too
    encrypted_hex = encrypted.encode('latin-1').hex()

    divider()
    print(f"  Original Text  : {text}")
    print(f"  XOR Key        : {key}")
    divider()
    print(f"  Encrypted (hex): {encrypted_hex}")
    print(f"  Decrypted Text : {decrypted}")
    divider()
    print("  ✅  XOR Encryption & Decryption complete!")
    print("  ℹ  XOR is self-inverse: encrypting twice returns original text.")


# ── DEMO ─────────────────────────────────────────────────────

def run_demo():
    section_header("Demo – Both Ciphers")

    sample_text = "Hello DecodeLabs"
    caesar_shift = 7
    xor_key = 42

    # Caesar demo
    c_enc = caesar_encrypt(sample_text, caesar_shift)
    c_dec = caesar_decrypt(c_enc, caesar_shift)

    print("\n  [ Caesar Cipher Demo ]")
    print(f"  Plain text  : {sample_text}")
    print(f"  Shift key   : {caesar_shift}")
    print(f"  Encrypted   : {c_enc}")
    print(f"  Decrypted   : {c_dec}")

    divider()

    # XOR demo
    x_enc = xor_encrypt(sample_text, xor_key)
    x_dec = xor_decrypt(x_enc, xor_key)
    x_hex = x_enc.encode('latin-1').hex()

    print("\n  [ XOR Cipher Demo ]")
    print(f"  Plain text      : {sample_text}")
    print(f"  XOR key         : {xor_key}")
    print(f"  Encrypted (hex) : {x_hex}")
    print(f"  Decrypted       : {x_dec}")

    divider()
    print("  ✅  Demo complete! Now try your own text from the main menu.")


# ── ENTRY POINT ──────────────────────────────────────────────

if __name__ == "__main__":
    main()
