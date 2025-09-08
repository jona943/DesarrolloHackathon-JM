import os
import sys
import google.generativeai as genai
from dotenv import load_dotenv

# Agrega la ruta raíz del proyecto al sys.path para encontrar el .env
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)
load_dotenv(os.path.join(project_root, '.env'))

def get_gemini_response(prompt: str) -> str:
    """
    Función genérica para enviar un prompt a la API de Gemini.
    """
    try:
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error al contactar la API de Gemini: {e}"

def main():
    """
    Script para generar un calendario de contenido semanal para redes sociales.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: No se encontró la API key. Revisa tu archivo .env en la raíz del proyecto.")
        return
    
    genai.configure(api_key=api_key)

    try:
        # Busca el prompt en la misma carpeta que este script
        prompt_path = os.path.join(os.path.dirname(__file__), 'prompt.md')
        with open(prompt_path, 'r', encoding='utf-8') as f:
            master_prompt = f.read()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo 'prompt.md' en la carpeta 'content_calendar_generator'.")
        return

    # --- Interfaz de Usuario ---
    print("======================================================")
    print("🗓️  Calendario de Contenido Semanal 🗓️")
    print("======================================================")
    print("Genera un plan de 7 días de ideas para tus redes sociales.")
    
    business_type = input("➡️  Introduce el tipo de negocio (ej. 'cafetería', 'librería'): ")

    # --- Construcción y Ejecución del Prompt ---
    final_prompt = master_prompt.replace("[TIPO_DE_NEGOCIO]", business_type)

    print("\n======================================================")
    print("⏳  Diseñando tu estrategia semanal... Por favor, espera.")
    print("======================================================")

    generated_calendar = get_gemini_response(final_prompt)
    
    print("\n--- ✅ TU PLAN DE CONTENIDO PARA 7 DÍAS ---\n")
    print(generated_calendar)
    print("\n--- FIN DEL PLAN ---")
    
    print("\nProceso completado exitosamente.")


if __name__ == "__main__":
    main()
