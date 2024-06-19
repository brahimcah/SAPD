import ftplib

def check_ftp_connection(host, username, password, port=21):
    """
    Verifica si se puede establecer una conexión FTP con el servidor especificado.
    
    Args:
        host (str): La dirección del servidor FTP.
        username (str): El nombre de usuario para la autenticación.
        password (str): La contraseña para la autenticación.
        port (int): El puerto del servidor FTP (por defecto es 21).

    Returns:
        bool: True si la conexión es exitosa, False en caso contrario.
    """
    try:
        # Crear una instancia de FTP
        ftp = ftplib.FTP()
        
        # Intentar conectar al servidor FTP
        print(f"Conectando a {host}:{port}...")
        ftp.connect(host, port)
        
        # Intentar iniciar sesión con las credenciales proporcionadas
        print("Iniciando sesión...")
        ftp.login(username, password)
        
        # Cerrar la conexión
        ftp.quit()
        
        # Si todo va bien, la conexión fue exitosa
        print("Conexión FTP exitosa.")
        return True
    except ftplib.all_errors as e:
        # Si ocurre un error, imprimirlo y retornar False
        print(f"Error al conectar al servidor FTP: {e}")
        return False

# Ejemplo de uso
host = "un-click.org"
username = "ftp-sapd"
password = "hVkP$emIn9x9"

if check_ftp_connection(host, username, password):
    print("Puedes conectarte al servidor FTP.")
else:
    print("No se pudo establecer una conexión FTP.")
