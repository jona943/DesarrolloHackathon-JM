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
    Script para generar respuestas a reseñas de clientes.
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
        print(f"Error: No se encontró el archivo 'prompt.md' en la carpeta 'review_responder'.")
        return

    # --- Interfaz de Usuario ---
    print("======================================================")
    print("🤖 Asistente para Responder Reseñas 🤖")
    print("======================================================")
    
    business_name = input("➡️  ¿Cuál es el nombre de tu negocio?: ")
    review_text = input("➡️  Pega aquí la reseña del cliente: ")
    review_type = input("➡️  La reseña es 'Positiva' o 'Negativa'?: ")

    # --- Construcción y Ejecución del Prompt ---
    final_prompt = master_prompt.replace("[NOMBRE_DEL_NEGOCIO]", business_name)
    final_prompt = final_prompt.replace("[TEXTO_RESEÑA]", review_text)
    final_prompt = final_prompt.replace("[TIPO_RESEÑA]", review_type)

    print("\n======================================================")
    print("⏳  Elaborando una respuesta profesional... Por favor, espera.")
    print("======================================================")

    generated_response = get_gemini_response(final_prompt)
    
    print("\n--- ✅ RESPUESTA SUGERIDA ---\n")
    print(generated_response)
    print("\n--- FIN DE LA SUGERENCIA ---")
    
    print("\nProceso completado exitosamente.")


if __name__ == "__main__":
    main()
