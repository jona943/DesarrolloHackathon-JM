import os
import sys
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv

# --- Configuración de Rutas y API Key ---
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
        return f"Error: No se encontró el archivo de imagen en la ruta: {image_path}"
    except Exception as e:
        return f"Error al contactar la API de Gemini o procesar la imagen: {e}"

def main():
    """
    Script para generar ideas de marketing a partir de una imagen de una situación.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: No se encontró la API key. Revisa tu archivo .env en la raíz.")
        return
    
    genai.configure(api_key=api_key)

    try:
        prompt_path = os.path.join(os.path.dirname(__file__), 'prompt.md')
        with open(prompt_path, 'r', encoding='utf-8') as f:
            master_prompt = f.read()
    except FileNotFoundError:
        print(f"Error: No se encontró 'prompt.md' en la carpeta 'idea_from_image_generator'.")
        return

    # --- Interfaz de Usuario ---
    print("======================================================")
    print("📸 Generador de Ideas a partir de una Imagen 📸")
    print("======================================================")
    print("Convierte un problema visual en una solución de marketing instantánea.")
    print("Toma una foto de algo que quieras mejorar (ej. tu local vacío, un producto que no se vende).")
    
    image_path = input("➡️  Arrastra y suelta el archivo de imagen aquí y presiona Enter: ").strip()

    # --- Construcción y Ejecución del Prompt ---
    # El prompt maestro ya está completo, solo necesita la imagen.
    
    print("\n======================================================")
    print("🧠  Analizando la situación y generando ideas... Por favor, espera.")
    print("======================================================")

    generated_ideas = get_gemini_multimodal_response(master_prompt, image_path)
    
    print("\n--- ✅ IDEAS ACCIONABLES GENERADAS ---\n")
    print(generated_ideas)
    print("\n--- FIN DE LAS IDEAS ---")
    
    print("\nProceso completado exitosamente.")


if __name__ == "__main__":
    main()
