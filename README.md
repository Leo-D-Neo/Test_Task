# Test_Task
Разработано консольное приложение для выполнения тестового задания. Для того чтобы запустить програму нужно иметь на своем ПК установленые интерпретатор python 3.9 и библиотеку openCV (и ее зависимости) .
>Примечание: символом `>` обозначается ввод пользователя
## Инструкция по использованию программы
1. Запускаем приложение командой `python3 main.py`
2. Программа запрашивает путь к изображению (можно ввести либо абсолютный, либо относительный)
Например: 
    ```
    Введите путь к видеофайлу: 
    > test.mp4
    ```

3. Затем программа предостовляет выбор команд пользователю
    ```
    Введите команду:
    	1 - уменьшает разрешение видео в 2 раза
    	2 - переводит видео в черно-белый формат
    	3 - выводит порядковый номер кадра в углу видео
    	q - выход
    ```
    
    Пример ввода:
    
    `> 3`

	Если пользователь введет что-то кроме предоставленых команд, программа сообщит что `Ошибка, неизвестная команда` и продублирует возможные команды.

4. После програма запросит указать куда сохранить изменненое видео. Нужно указать название файла (вместе с путем). Программа сама создаст файл если такого нет , и если есть файл с таким именем то перезапишет его. Указвать расширение ***не*** нужно так, как результат всегда сохраняется в формате .mp4.   

    Например:
    ```
    Введите путь нового видео файла(без указания расширения):
    > result
    ```

5. По окончанию обработки видео программа выведет сообщение `Готово`  

## Пример работы
**Начальные условия**: Видефайл под названием `test.mp4` располагается в той же папке что и программа `main.py`

**Работа с программой**: 
```
Введите путь к видеофайлу:
test.mp4
Введите команду:
	1 - уменьшает разрешение видео в 2 раза
	2 - переводит видео в черно-белый формат
	3 - выводит порядковый номер кадра в углу видео
	q - выход
2
Введите путь нового видео файла(без указания расширения):
a
Готово
```

**Результат**: Создан новый видеофайл под названием `a.mp4`, который является черно-белым форматом исходного видео  `test.mp4`.







