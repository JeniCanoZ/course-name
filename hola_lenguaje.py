import os


def main():
    nombre = os.getenv("USERNAME")
    lenguaje = os.getenv("LANGUAGE")
    print(f"¡Hola Mundo desde {lenguaje} soy {nombre}!")


if __name__ == "__main__":
    main()
