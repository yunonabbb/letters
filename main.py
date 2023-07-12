name_input = input("Введите строку: ")
num_characters = len(name_input)
num_digits = sum(char.isdigit() for char in name_input)
num_numbers = sum(word.isdigit() for word in name_input.split())
num_letters = sum(char.isalpha() for char in name_input)
num_upper_letters = sum(char.isupper() for char in name_input)
num_lower_letters = sum(char.islower() for char in name_input)
num_spaces = name_input.count(" ")
mod_input = name_input.replace(" ", "-")


print("Количество символов:", num_characters)
print("Количество цифр:", num_digits)
print("Количество чисел:", num_numbers)
print("Количество букв:", num_letters)
print("Количество букв в верхнем регистре:", num_upper_letters)
print("Количество букв в нижнем регистре:", num_lower_letters)
print("Количество пробелов:", num_spaces)

words = name_input.split()
num_words = len(words)
print("Слова:")
for word in words:
    print(word)
print("Количество слов:", num_words)

