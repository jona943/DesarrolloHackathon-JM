import os
import sys
import google.generativeai as genai
from dotenv import load_dotenv

# Agrega la ruta raíz del proyecto al sys.path para encontrar el .env
# Esto hace que el script funcione sin importar desde dónde se llame.
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
    Script para generar posts para redes sociales.
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
        print(f"Error: No se encontró el archivo 'prompt.md' en la carpeta 'post_creator'.")
        return

    # --- Interfaz de Usuario ---
    print("======================================================")
    print("🤖 Creador de Posts para Redes Sociales 🤖")
    print("======================================================")
    
    business_type = input("➡️  Primero, ¿cuál es tu tipo de negocio? (ej. 'Cafetería'): ")
    main_idea = input("➡️  ¿De qué quieres hablar hoy?: ")
    post_tone = input("➡️  ¿Qué tono quieres usar? (ej. 'Casual', 'Profesional', 'Divertido'): ")

    # --- Construcción y Ejecución del Prompt ---
    final_prompt = master_prompt.replace("[TIPO_DE_NEGOCIO]", business_type)
    final_prompt = final_prompt.replace("[IDEA_PRINCIPAL]", main_idea)
    final_prompt = final_prompt.replace("[TONO_POST]", post_tone)

    print("\n======================================================")
    print("⏳  Redactando posts con IA... Por favor, espera.")
    print("======================================================")

    generated_posts = get_gemini_response(final_prompt)
    
    print("\n--- ✅ PROPUESTAS DE POSTS ---\n")
    print(generated_posts)
    print("\n--- FIN DE LAS PROPUESTAS ---")
    
    print("\nProceso completado exitosamente.")


if __name__ == "__main__":
    main()
