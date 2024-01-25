# Aqui se importa la configuración o se genera una genérica en caso de no existir el archivo 'config.py'
try:
    from config.config import api_cfg
except:
    # Pendiente: debe crear el archivo con los parámetros genéricos
    api_cfg = {
        "API_HOST" : "0.0.0.0",
        "API_PORT" : 5500
    }