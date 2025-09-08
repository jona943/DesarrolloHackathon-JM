import os
import sys
import google.generativeai as genai
from dotenv import load_dotenv
import PIL.Image  # Importamos la librería para manejar imágenes

# Agrega la ruta raíz del proyecto al sys.path para encontrar el .env
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)
load_dotenv(os.path.join(project_root, '.env'))

def get_multimodal_gemini_response(prompt: str, image_path: str) -> str:
    """
    Función para enviar un prompt de texto y una imagen a la API de Gemini.
    """
    try:
        # Abrimos la imagen desde la ruta proporcionada
        img = PIL.Image.open(image_path)
        
        # Usamos el modelo gemini-1.5-flash que es multimodal
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        
        # La petición incluye tanto el texto del prompt como la imagen
        response = model.generate_content([prompt, img])
        return response.text
    except FileNotFoundError:
        return f"Error: No se pudo encontrar la imagen en la ruta: {image_path}"
    except Exception as e:
        return f"Error al contactar la API de Gemini: {e}"

def main():
    """
    Script para digitalizar un menú desde una foto de un pizarrón.
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
        print(f"Error: No se encontró el archivo 'prompt.md' en la carpeta 'menu_scanner'.")
        return

    # --- Interfaz de Usuario ---
    print("======================================================")
    print("🤖 Escáner de Menú a partir de Foto 🤖")
    print("======================================================")
    
    image_path = input("➡️  Introduce la ruta a la imagen del menú (ej. /Users/jonathan/Desktop/menu.jpg): ")

    print("\n======================================================")
    print("⏳  Analizando imagen y digitalizando menú... Por favor, espera.")
    print("======================================================")

    # --- Llamada a la API ---
    # Pasamos tanto el prompt como la ruta de la imagen
    generated_menu = get_multimodal_gemini_response(master_prompt, image_path)
    
    print("\n--- ✅ MENÚ DIGITALIZADO (FORMATO JSON) ---\n")
    print(generated_menu)
    print("\n--- FIN DEL MENÚ ---")
    
    print("\nProceso completado exitosamente.")


if __name__ == "__main__":
    main()
