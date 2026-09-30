import re
from collections import Counter

# === Функції для базових операцій з рядками ===

def find_substring(text, substring):
    """
    Пошук підрядка в тексті.
    Повертає індекс першого входження або -1, якщо підрядок не знайдено.
    """
    return text.find(substring)  
    

def replace_substring(text, old, new):
    """
    Заміна підрядка в тексті.
    """
    return text.replace(old, new)
    

def split_text(text, delimiter=' '):
    """
    Розділення тексту за роздільником.
    """
    return text.split(delimiter)
    

def format_string_f(name, age):
    """
    Форматування рядка з використанням f-string.
    Приклад: "Мене звати [name] і мені [age] років."
    """
    return f"Мене звати {name} і мені {age} років."
    

def format_string_method(name, age):
    """
    Форматування рядка з використанням методу .format().
    Приклад: "Мене звати [name] і мені [age] років."
    """
    return "Мене звати {} і мені {} років.".format(name, age)
   

# === Функції для роботи з регулярними виразами ===

def extract_emails(text):
    """
    Витяг email адрес з тексту.
    """
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(pattern, text)
    

def validate_phone_number(number):
    """
    Валідація українського телефонного номера.
    Формат: +380xxxxxxxxx
    """
    pattern = r"^\+380\d{9}$"
    return bool(re.match(pattern, number))

def extract_hashtags(text):
    """
    Витяг хештегів з тексту.
    """
    pattern = r"#\w+"
    return re.findall(pattern, text)
    pass

def extract_mentions(text):
    """
    Витяг згадувань користувачів з тексту (напр. @user).
    """
    pattern = r"@\w+"
    return re.findall(pattern, text)
    pass

# === Функції для аналізу тексту ===

def count_words(text):
    """
    Підрахунок кількості слів у тексті.
    """
    # TODO: Реалізуйте функцію
    words = re.findall(r'\b\w+\b', text)
    return len(words)

def count_sentences(text):
    """
    Підрахунок кількості речень у тексті.
    """
    return len(re.findall(r'[.!?]+', text))
    

def word_frequency(text):
    """
    Підрахунок частоти слів у тексті.
    Повертає об'єкт Counter.
    """
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)
    

def analyze_text(text):
    """
    Комплексний аналіз тексту.
    Повертає словник з результатами аналізу.
    """
    return {
        'word_count': count_words(text),
        'sentence_count': count_sentences(text),
        'emails': extract_emails(text),
        'hashtags': extract_hashtags(text),
        'mentions': extract_mentions(text),
        # Беремо лише 5 найпопулярніших слів, щоб не виводити все полотно тексту
        'top_words': word_frequency(text).most_common(5) 
        }

def format_analysis_results(results):
    """
    Форматування результатів аналізу для зручного виведення.
    """
    # TODO: Реалізуйте функцію
    output = "=== Результати аналізу тексту ===\n"
    output += f"Кількість слів: {results['word_count']}\n"
    output += f"Кількість речень: {results['sentence_count']}\n"
    
    # Використовуємо .join() щоб красиво зліпити списки через кому
    output += f"Email-адреси: {', '.join(results['emails'])}\n"
    output += f"Хештеги: {', '.join(results['hashtags'])}\n"
    
    output += "Топ-5 найчастіших слів:\n"
    for word, count in results['top_words']:
        output += f"  - {word}: {count} разів\n"
        
    return output

# === Функція для вилучення даних за варіантом ===

def extract_variant_data(text, variant_pattern):
    """
    Вилучає дані з тексту за допомогою патерну, специфічного для варіанту.
    """
    r"[A-Za-z]+-VR\d+"
   

# === Головна частина програми ===

def read_file_content(filepath):
    """
    Читає вміст файлу.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Помилка: Файл не знайдено за шляхом {filepath}")
        return None

def main():
    """
    Головна функція, що керує виконанням програми.
    """
    print("Ласкаво просимо до аналізатора тексту!")

    # Шлях до файлу з текстом
    text_filepath = r'C:\Users\Ssimov\Desktop\УЧЕБА\2курс\python\git\lab4\src\data\neoterra_text.txt'

    # Читання тексту з файлу
    text_to_analyze = read_file_content(text_filepath)
    if not text_to_analyze:
        return # Завершити, якщо файл не прочитано

    while True:
        try:
            print("\nОберіть опцію:")
            print("1. Аналіз тексту 'NeoTerra 3000'")
            print("2. Валідація телефонного номера")
            print("3. Вилучення даних за варіантом")
            print("4. Вихід")
            choice = input("Ваш вибір: ")

            if choice == '1':
                results = analyze_text(text_to_analyze)
                print(format_analysis_results(results))

            elif choice == '2':
                phone = input("Введіть номер телефону для валідації: ")
                if validate_phone_number(phone):
                    print("Номер телефону валідний.")
                else:
                    print("Номер телефону невалідний.")

            elif choice == '3':
                variant = input("Введіть номер вашого варіанту (1-30): ")
                # TODO: Визначте патерн для вашого варіанту
                # Наприклад, для варіанту 1 (квантові комп'ютери):
                # pattern = r'\b[A-Z]{2}-\d{4}\b'
                # variant_data = extract_variant_data(text_to_analyze, pattern)
                # print(f"Знайдені дані: {variant_data}")
                print("Цю частину необхідно реалізувати самостійно згідно вашого варіанту.")

            elif choice == '4':
                print("Дякуємо за використання аналізатора!")
                break

            else:
                print("Невірний вибір. Спробуйте ще раз.")

        except Exception as e:
            print(f"Виникла помилка: {e}")

if __name__ == '__main__':
    main()
