import os

def main():
    nombre = os.getenv("USERNAME")
    print(f"¡Hola, {nombre} desde GITHUB!")

if __name__ =="__main__":
    main()