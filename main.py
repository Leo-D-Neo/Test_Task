import cv2
import numpy as np


# ф-я для получения корректной команды от пользователя
def input_command():
    while True:
        print("Введите команду:\n"
              "\t1 - уменьшает разрешение видео в 2 раза\n"
              "\t2 - переводит видео в черно-белый формат\n"
              "\t3 - выводит порядковый номер кадра в углу видео\n"
              "\tq - выход")
        command = input()

        if command in ['1', '2', '3', 'q']:
            break
        else:
            print("Ошибка, неизвестная команда")
    return command


# ф-я уменьшения разрешения видео и запись его в новый файл
def reduces_resolution_two_times(cap, out):
    new_frame_width = int(cap.get(3)/2)
    new_frame_height = int(cap.get(4)/2)
    new_frame_size = (new_frame_width, new_frame_height)

    while True:
        ret, frame = cap.read()

        if ret == True:
            new_frame =  cv2.resize(frame, new_frame_size)
            out.write(new_frame)

        # Break the loop
        else:
            break


# ф-я переводит видео в черно-белый формат и записывает его в новый файл
def RGB_to_Gray(cap, out):
    while True:
        ret, frame = cap.read()

        if ret == True:
            new_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            out.write(new_frame)

        # Break the loop
        else:
            break


# ф-я выводит порядковый номер кадра и сохраняет видео в файл
def frame_count(cap, out):
    i = 0
    while True:
        ret, frame = cap.read()

        if ret == True:
            new_frame = cv2.putText(frame, str(i), (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))
            out.write(new_frame)
            i += 1

        # Break the loop
        else:
            break



# Получаем путь к файлу и создаем объект захвата видео
print("Введите путь видео файлу:")
path = input()
cap = cv2.VideoCapture(path)

# Проверяем удалось ли захватить видео
if cap.isOpened() == False:
    print("Error opening video stream or file")
    exit(0)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
frame_size = (frame_width, frame_height)
fps = int(cap.get(5))

#Ввод команды
command = input_command()

if command == "q":
    cap.release()
    exit(0)

# Получаем путь к новому файлу и создаем объект записи видео
print("Введите путь нового видео файла:")
new_path = input()

#Выполнение команды
if command == "1":
    new_frame_size = (frame_width//2, frame_height//2)
    out = cv2.VideoWriter(new_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, new_frame_size)
    reduces_resolution_two_times(cap, out)

if command == "2":
    out = cv2.VideoWriter(new_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, frame_size, False)
    RGB_to_Gray(cap, out)

if command == "3":
    out = cv2.VideoWriter(new_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, frame_size)
    frame_count(cap, out)

print("Готово")

# When everything done, release the video capture object
cap.release()
out.release()

