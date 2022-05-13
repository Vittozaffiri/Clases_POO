import logging

def ask_name():

    return input("cual es tu nombre? ")

def greet(name):
    logging.info(f"Salundadno al usuario con nombre {name}")
    print(f"hola {name}")
    logging.info(f"usuario {name} ha sido saludado")



if __name__ == "__main__":


    logging.basicConfig(
    filename = "ejemplo.log",
    encoding="utf-8",
    level = logging.INFO
)

    name = ask_name()
    greet(name)