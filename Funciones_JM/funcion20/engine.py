import os
import sys
import google.generativeai as genai
from dotenv import load_dotenv

# --- Configuración de Rutas y API Key ---
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
    Script para generar una sección de Preguntas Frecuentes (FAQ).
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
        print(f"Error: No se encontró el archivo 'prompt.md' en la carpeta 'faq_assistant'.")
        return

    # --- Interfaz de Usuario ---
    print("======================================================")
    print("🤔 Asistente de Preguntas Frecuentes (FAQ) 🤔")
    print("======================================================")
    print("Genera automáticamente una sección de FAQ para tu sitio web o perfil de negocio.")
    
    business_description = input("➡️  Introduce una descripción breve de tu negocio: ")

    # --- Construcción y Ejecución del Prompt ---
    final_prompt = master_prompt.replace("[DESCRIPCION_NEGOCIO]", business_description)

    print("\n======================================================")
    print("💡  Generando preguntas y respuestas... Por favor, espera.")
    print("======================================================")

    generated_faq = get_gemini_response(final_prompt)
    
    print("\n--- ✅ SECCIÓN DE FAQ GENERADA ---\n")
    print(generated_faq)
    print("\n--- FIN DE LA SECCIÓN ---")
    
    print("\nProceso completado exitosamente.")


if __name__ == "__main__":
    main()
