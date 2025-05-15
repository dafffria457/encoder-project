import argparse
import sys

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

def process_file(input_file, output_file, shift):
    """Обрабатывает файл: шифрует/дешифрует его содержимое"""
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        processed = caesar_cipher(content, shift)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(processed)
        
        print(f"Файл успешно обработан. Результат сохранён в {output_file}")
    except Exception as e:
        print(f"Ошибка при обработке файла: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Шифратор/дешифратор Цезаря")
    parser.add_argument('-e', '--encrypt', action='store_true', help="Режим шифрования")
    parser.add_argument('-d', '--decrypt', action='store_true', help="Режим дешифрования")
    parser.add_argument('-s', '--shift', type=int, help="Величина сдвига")
    parser.add_argument('-i', '--input', help="Входной файл")
    parser.add_argument('-o', '--output', help="Выходной файл")
    
    args = parser.parse_args()
    
    if not args.shift:
        args.shift = int(input("Введите сдвиг: "))
    
    if args.decrypt:
        args.shift = -args.shift
    
    if args.input and args.output:
        process_file(args.input, args.output, args.shift)
    else:
        message = input("Введите сообщение: ") if not args.input else open(args.input, 'r', encoding='utf-8').read()
        result = caesar_cipher(message, args.shift)
        print("\nРезультат:", result)

if __name__ == "__main__":
    main()
