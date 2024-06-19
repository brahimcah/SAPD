import configparser

# Crea un objeto ConfigParser
config = configparser.ConfigParser()

# Lee el archivo config.ini
config.read('config.ini')

# Accede a los valores
nombre = config['info']['nombre']
edad = config['info']['edad']
email = config['info']['email']

# Imprime los valores
print("Nombre:", nombre)
print("Edad:", edad)
print("Email:", email)
