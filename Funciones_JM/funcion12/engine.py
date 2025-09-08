import os
import sys
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv

# Agrega la ruta raíz del proyecto al sys.path para encontrar el .env
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)
load_dotenv(os.path.join(project_root, '.env'))

def get_gemini_multimodal_response(prompt: str, image_path: str) -> str:
    """
    Función para enviar un prompt y una imagen a la API de Gemini.
    """
    try:
        img = Image.open(image_path)
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        response = model.generate_content([prompt, img])
        return response.text
    except FileNotFoundError:
        return "Error: El archivo de imagen no fue encontrado en la ruta especificada."
    except Exception as e:
        return f"Error al contactar la API de Gemini o procesar la imagen: {e}"

def main():
    """
    Script que analiza una imagen para su uso en anuncios.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: No se encontró la API key. Revisa tu archivo .env en la raíz del proyecto.")
        return
    
    genai.configure(api_key=api_key)

    try:
        prompt_path = os.path.join(os.path.dirname(__file__), 'prompt.md')
        with open(prompt_path, 'r', encoding='utf-8') as f:
            master_prompt = f.read()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo 'prompt.md' en la carpeta 'ad_image_analyzer'.")
        return

    # --- Interfaz de Usuario ---
    print("======================================================")
    print("🎨 Analizador de Imagen para Anuncios 🎨")
    print("======================================================")
    print("Sube una imagen para recibir un análisis sobre su efectividad publicitaria.")
    
    image_path = input("➡️  Arrastra y suelta el archivo de imagen aquí y presiona Enter: ").strip()

    # --- Construcción y Ejecución del Prompt ---
    print("\n======================================================")
    print("⏳  Analizando tu imagen con ojos de experto... Por favor, espera.")
    print("======================================================")

    analysis_result = get_gemini_multimodal_response(master_prompt, image_path)
    
    print("\n--- ✅ ANÁLISIS PUBLICITARIO DE TU IMAGEN ---\n")
    print(analysis_result)
    print("\n--- FIN DEL ANÁLISIS ---")
    
    print("\nProceso completado exitosamente.")


if __name__ == "__main__":
    main()
