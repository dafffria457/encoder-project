def caesar_cipher(text, shift, alphabet=None):
    """Шифрует/дешифрует текст с помощью шифра Цезаря"""
    if alphabet is None:
        alphabet = (
            'abcdefghijklmnopqrstuvwxyz'
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
            'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        )
    
    result = []
    for char in text:
        if char in alphabet:
            idx = alphabet.index(char)
            new_idx = (idx + shift) % len(alphabet)
            result.append(alphabet[new_idx])
        else:
            result.append(char)
    return ''.join(result)

def get_valid_shift():
    """Получает корректный сдвиг от пользователя"""
    while True:
        try:
            shift = int(input("Введите сдвиг (целое число): "))
            return shift
        except ValueError:
            print("Ошибка: сдвиг должен быть целым числом")

if __name__ == "__main__":
    print("\n=== Улучшенный шифратор Цезаря ===")
    print("1. Зашифровать сообщение")
    print("2. Расшифровать сообщение")
    
    while True:
        choice = input("Выберите действие (1/2): ")
        if choice in ('1', '2'):
            break
        print("Неверный выбор, попробуйте снова")
    
    message = input("Введите сообщение: ")
    shift = get_valid_shift()
    
    if choice == '2':
        shift = -shift
    
    result = caesar_cipher(message, shift)
    print("\nРезультат:", result)
