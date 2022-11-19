import glob

book_files = []

file_list = glob.glob("sorted_files/*.txt")
for file_number in range(len(file_list)):
    with open(file_list[file_number], 'r', encoding='utf-8') as file:
        file = file.readlines()
        book_files.append([len(file), file_list[file_number], file])

book_files.sort()

for file_num in range(len(book_files)):
    with open('output.txt', 'a', encoding='utf-8') as file_total:   
        file_total.write(book_files[file_num][1] + '\n')
        file_total.writelines(str(book_files[file_num][0]) + '\n')
        file_total.writelines(str(" ".join(book_files[file_num][2])) + '\n')
        file_total.write('\n')
