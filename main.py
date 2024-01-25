import os

# Input the file names
input_file_name = input("Введите имя входного файла: ")
output_file_name = input("Введите имя выходного файла: ")

# Check if the files exist
if not (os.path.exists(input_file_name) and os.path.exists(output_file_name)):
    print("По меньшей мере один из указанных файлов не существует. Программа завершает работу.")
    exit()

# Check if the files are text files
if not (input_file_name.endswith('.txt') and output_file_name.endswith('.txt')):
    print("По меньшей мере один из указанных файлов не является текстовым. Программа завершает работу.")
    exit()

# Read the number of lines in the input file
with open(input_file_name, 'r') as input_file:
    n_lines_inputfile = sum(1 for line in input_file)

# Input the line number to be copied
N = int(input("Введите номер строки входного файла для копирования в выходной файл: "))

# Check if N is within the valid range
if N <= 0 or N > n_lines_inputfile:
    print("Введённый номер строки за пределами допустимого диапазона. Программа завершает работу.")
    exit()

# Read line N from the input file
with open(input_file_name, 'r') as input_file:
    lines = input_file.readlines()
    line_N = lines[N - 1]

# Output the number of characters on line N
print(f"(i) Строка {N} входного файла содержит {len(line_N)} символ (-а, -ов).")

# Copy line N from the input file to the output file
with open(output_file_name, 'a') as output_file:
    output_file.write(line_N)
    print(f"(i) Строка {N} входного файла скопирована в выходной файл.")
