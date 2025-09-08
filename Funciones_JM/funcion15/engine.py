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
    Script para redactar mensajes para clientes frecuentes.
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
        print(f"Error: No se encontró el archivo 'prompt.md' en la carpeta 'frequent_customer_messenger'.")
        return

    # --- Interfaz de Usuario ---
    print("======================================================")
    print("💬 Creador de Mensajes para Clientes Frecuentes 💬")
    print("======================================================")
    print("Comunícate de forma cercana con tus clientes más leales.")
    
    message_objective = input("➡️  ¿Qué quieres comunicarles? (ej. 'anunciar el nuevo horario de verano'): ")

    # --- Construcción y Ejecución del Prompt ---
    final_prompt = master_prompt.replace("[OBJETIVO_MENSAJE]", message_objective)


    print("\n======================================================")
    print("⏳  Redactando un mensaje amigable... Por favor, espera.")
    print("======================================================")

    generated_message = get_gemini_response(final_prompt)
    
    print("\n--- ✅ MENSAJE LISTO PARA ENVIAR ---\n")
    print(generated_message)
    print("\n--- FIN DEL MENSAJE ---")
    
    print("\nProceso completado exitosamente.")


if __name__ == "__main__":
    main()
