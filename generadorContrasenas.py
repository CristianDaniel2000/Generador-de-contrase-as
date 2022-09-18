import random

print("Bievenido al generador de contraseñas")

# Definimos las variables
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*().,?;:'

def GeneradorDecontrasenas():
    flag_pregunta = True
    while flag_pregunta:
        try:
            numero_contrasenas = input("¿Cuántas contraseñas quieres generar?: ")
            numero_contrasenas = int(numero_contrasenas)
            while True:
                try:
                    longitud_contrasenia = input("Ingresa el número de caracteres que quieres que tenga la contraseña: ")
                    longitud_contrasenia = int(longitud_contrasenia)
                    try:
                        for pwd in range(numero_contrasenas):
                            contrasenaGenerada = ''
                            for caracter in range(longitud_contrasenia):
                                contrasenaGenerada += random.choice(chars)
                            print("Contraseña generada: ", contrasenaGenerada)
                        break
                    except Error as er:
                        print("Ha ocurrido un error: ", er)
                except ValueError:
                    print("Ingresa un valor numérico!")
        except ValueError as err:
            print("Ingresa un valor numérico!")
        flag_pregunta = input("¿Quieres generar más contraseñas? (Si/No): ")
        if flag_pregunta.upper() == "SI":
            #continue
            flag_pregunta = True
        else:
            flag_pregunta = False

def main():
    GeneradorDecontrasenas()

if __name__=="__main__":
    main()
