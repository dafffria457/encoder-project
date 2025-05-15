def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

if __name__ == "__main__":
    message = input("Введите сообщение: ")
    shift = int(input("Введите сдвиг: "))
    print("Зашифрованное сообщение:", caesar_cipher(message, shift))
