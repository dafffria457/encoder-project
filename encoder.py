def caesar_encrypt(text, shift):
    """Шифрует текст с помощью шифра Цезаря"""
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    """Дешифрует текст, зашифрованный шифром Цезаря"""
    return caesar_encrypt(text, -shift)

if __name__ == "__main__":
    print("\n=== Шифратор/Дешифратор Цезаря ===")
    print("1. Зашифровать сообщение")
    print("2. Расшифровать сообщение")
    
    choice = input("Выберите действие (1/2): ")
    message = input("Введите сообщение: ")
    shift = int(input("Введите сдвиг (1-25): "))
    
    if choice == '1':
        encrypted = caesar_encrypt(message, shift)
        print("Зашифрованное сообщение:", encrypted)
    elif choice == '2':
        decrypted = caesar_decrypt(message, shift)
        print("Расшифрованное сообщение:", decrypted)
    else:
        print("Неверный выбор")
