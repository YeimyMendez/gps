import requests

def obtener_informacion_de_ubicacion(ip_address):
    # Reemplaza 'TU_CLAVE_DE_API' con tu clave de API real de MaxMind
    api_key = '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'
    url = f'https://geolocation-db.com/json/{ip_address}&position=true'

    try:
        response = requests.get(url, headers={'Authorization': f'Bearer {api_key}'})
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            # Maneja el caso de error, por ejemplo, registrando el error o mostrando un mensaje al usuario
            return None
    except Exception as e:
        # Maneja excepciones si ocurren errores en la solicitud
        return None
