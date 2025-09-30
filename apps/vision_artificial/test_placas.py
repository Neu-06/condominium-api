import os
import requests
import time

# Configuración de Plate Recognizer
API_URL = "https://api.platerecognizer.com/v1/plate-reader/"
API_TOKEN = "3bfcad5ee8d854fe155db1ec3e3fe64f252e763c"
HEADERS = {"Authorization": f"Token {API_TOKEN}"}

# Carpeta con imágenes de prueba
DATASET_DIR = "d:/Practicas/FullStack/Smart Condominium/Condominium/apps/condominium-api/apps/vision_artificial/ImagenesPrueba"

def test_placas_en_directorio():
    imagenes = [f for f in os.listdir(DATASET_DIR) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    print(f"Total de imágenes encontradas: {len(imagenes)}\n")
    resultados = []

    for idx, img_name in enumerate(imagenes, 1):
        img_path = os.path.join(DATASET_DIR, img_name)
        print(f"[{idx}/{len(imagenes)}] Analizando: {img_name} ...")
        with open(img_path, "rb") as img_file:
            files = {'upload': img_file}
            try:
                response = requests.post(API_URL, headers=HEADERS, files=files)
                if response.status_code == 200:
                    data = response.json()
                    placas = [r['plate'] for r in data.get('results', [])]
                    print(f"    Placas detectadas: {placas if placas else 'Ninguna'}")
                    resultados.append({'imagen': img_name, 'placas': placas})
                else:
                    print(f"    Error ({response.status_code}): {response.text}")
                    resultados.append({'imagen': img_name, 'error': response.text})
            except Exception as e:
                print(f"    Excepción: {e}")
                resultados.append({'imagen': img_name, 'error': str(e)})
        time.sleep(1)  # Para evitar rate limit de la API

    print("\nResumen de resultados:")
    for r in resultados:
        if 'placas' in r:
            print(f"  {r['imagen']}: {r['placas']}")
        else:
            print(f"  {r['imagen']}: ERROR - {r['error']}")

if __name__ == "__main__":
    print("===== TEST DE RECONOCIMIENTO DE PLACAS =====\n")
    test_placas_en_directorio()
    print("\nPruebas finalizadas.")