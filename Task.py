# -Task_1-
from numpy import unicode_


print('Напишите программу, удаляющую из текста все слова, содержащие ""абв"".')

def del_string(del_str, txt):   #функция удаления строки
    txt = txt.split()
    list1 = []
    for i in txt:
        if del_str not in i:
            list1.append(i)
    return " ".join(list1)

str1 = 'абв'
with open('c:\\Users\\Onotole\\Desktop\\Python-Dz05\\Python_Dz-05\\tetx_to_delete.txt', encoding='utf-8') as text:  # читаем из файла строку и удаляем, и зщаписываем в новый файл
    text = text.read()
    fil = open('C:\\Users\\Onotole\\Desktop\\Python-Dz05\\Python_Dz-05\\New_Del_text.txt', 'w', encoding='utf-8')
    fil.write(''.join(del_string(str1, text)))
    fil.close()
print('Удаление произведено.')


# -Task_4-
print('Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.')

def compression(text):       #функция сокращения строки
    list1 = []
    count = 1
    for i in range(len(text)):
        if i == len(text) - 1:
            list1.append(f'{count}{text[i]}')
        else:
            if text[i] == text[i + 1]:
                count += 1
            else:
                list1.append(f'{count}{text[i]}')
                count = 1
    return "".join(list1)

with open('C:\\Users\\Onotole\\Desktop\\Python-Dz05\\Python_Dz-05\\Text_file.txt', encoding='utf-8') as text:   #Читаем данные из файла и сокращаем
    text = list(text.read())
    compression(text)

# Записываем результат в новый файл
data = open('C:\\Users\\Onotole\\Desktop\\Python-Dz05\\Python_Dz-05\\Compress_file.txt', 'w', encoding='utf-8')
data.write("".join(compression(text)))
data.close()
print('Сжатие произошло.')