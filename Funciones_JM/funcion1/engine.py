import os
import google.generativeai as genai
from dotenv import load_dotenv

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
    Script para generar slogans de negocio.
    """
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: No se encontró la API key. Revisa tu archivo .env")
        return
    
    genai.configure(api_key=api_key)

    try:
        with open('prompt.md', 'r', encoding='utf-8') as f:
            master_prompt = f.read()
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'prompt.md'.")
        return

    # --- Interfaz de Usuario ---
    print("======================================================")
    print("🤖 Generador de Slogans para Alma Local 🤖")
    print("======================================================")
    
    business_name = input("➡️  Introduce el nombre de tu negocio: ")
    business_activity = input("➡️  Describe tu negocio en pocas palabras (ej. 'Cafetería de especialidad'): ")

    # --- Construcción y Ejecución del Prompt ---
    final_prompt = master_prompt.replace("[NOMBRE_NEGOCIO]", business_name)
    final_prompt = final_prompt.replace("[ACTIVIDAD_NEGOCIO]", business_activity)

    print("\n======================================================")
    print("⏳  Creando slogans con IA... Por favor, espera.")
    print("======================================================")

    generated_slogans = get_gemini_response(final_prompt)
    
    print("\n--- ✅ SUGERENCIAS DE SLOGANS ---\n")
    print(generated_slogans)
    print("\n--- FIN DE LAS SUGERENCIAS ---")
    
    print("\nProceso completado exitosamente.")


if __name__ == "__main__":
    main()