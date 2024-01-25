from ui import start_menu


# if __name__ == '__main__':
#     start_menu()


import os

def check_file_type(file_path):
    return os.path.isfile(file_path) and os.path.splitext(file_path)[1] == '.txt'

def main():
    input_file = input("Введите имя входного файла: ")
    output_file = input("Введите имя выходного файла: ")
    n = int(input("Введите номер строки: "))

    if not check_file_type(input_file) or not check_file_type(output_file):
        print("Внимание: по меньшей мере один из указанных файлов не существует.")
        return

    if not os.path.isfile(input_file):
        print(f"ОШИБКА чтения файла «{input_file}».")
        return

    with open(input_file, 'r') as input_file_obj:
        if n <= 0 or n > len(input_file_obj.readlines()):
            print(f"ОШИБКА: Во входном файле «{input_file}» нет строки {n}.")
            return

    with open(output_file, 'a') as output_file_obj:
        line = input_file_obj.readline()
        output_file_obj.write(line)

    print(f"Строка {n} длиною {len(line)} была скопирована из файла «{input_file}» в конец файла «{output_file}».")

if __name__ == "__main__":
    main()