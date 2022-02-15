from distutils.command.config import config


def main():
    # open("/path/to/mars.jpg")
    try:
        configuration = open('config.txt')
    except FileNotFoundError as errFNF:
        print(' No se encontro el archivo', errFNF)
    except IsADirectoryError:
        print("No se puede leer")
    except (BlockingIOError, TimeoutError):
        print("FS no puede completar la lectura del archivo de configuracion")

if __name__ == '__main__':
    main()