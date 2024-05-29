import pyAesCrypt
import os


# Функция дешифрования файла файла
def decryprion(file, password):
    # задаем размер буфера
    buffer_size = 512 * 1024

    # вызываем метод расшифровки
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size

    )
    # чтобы видеть результат выводим на печать  имя зашифрованного файла
    print("[Файл '" + str(os.path.splitext(file)[0]) + "'дешифрован]")
    # удаляем исходный файл by remove
    os.remove(file)


# Функция сканирования директории
def walking_by_dirs(dir, password):
    # перебираем все поддериктории в указанной дериктории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # если мы нашли файл то расшифруем его
        if os.path.isfile(path):
            try:
                decryprion(path, password)
            except  Exception as ex:
                print(ex)
        # если находим директорию – то повторяем цикл в поисках файлов
        else:
            walking_by_dirs(path, password)


password = input("Введите пароль для расшифравки:")
walking_by_dirs("", password)
