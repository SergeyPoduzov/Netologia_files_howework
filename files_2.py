
# Третья задача Нетологии по файлам
filename1=r'files\1.txt'
filename2=r'files\2.txt'
filename3=r'files\3.txt'
#открытие последовательно и чтение 3-х файлов
with open(filename1,encoding='utf-8') as file_object:
  text1=file_object.readlines()

with open(filename2,encoding='utf-8') as file_object:
  text2=file_object.readlines()

with open(filename3,encoding='utf-8') as file_object:
  text3=file_object.readlines()

#Переименуем название файлов
filename1='1.txt'
filename2='2.txt'
filename3='3.txt'

# #делелам кортеж: нвзвание файла, длина, содердание
dict=[(filename1,len(text1), text1),(filename2,len(text2), text2),(filename3,len(text3), text3)]

#Отсортируем по знчения - по длине слов

dict.sort(key=lambda i: i[1])

# Присоединение к файлу: (изменился ключ на 'a'):
filename='files\programming.txt'
with open (filename,'a') as file_object1:
    for text in dict:
        file_object1.write(text[0]+"\n")
        file_object1.write(str(text[1])+"\n")
        for line in text[2]:
            file_object1.write(line)
        file_object1.write("\n")

print("Печать итогового файла")
with open(filename) as file_object:
  text=file_object.readlines()

for line in text:
    line=line.rstrip()
    print(line)