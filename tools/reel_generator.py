import os
import google.generativeai as genai
from dotenv import load_dotenv

def get_gemini_response(prompt: str) -> str:
    """
    Función para enviar un prompt a la API de Gemini y obtener una respuesta.
    Maneja la configuración y la llamada a la API.
    """
    try:
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error al contactar la API de Gemini: {e}"

def main():
    """
    Función principal que orquesta la ejecución del script.
    """
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: No se encontró la API key. Revisa tu archivo .env")
        return
    
    genai.configure(api_key=api_key)

    try:
        with open('prompts/reel_prompt.md', 'r', encoding='utf-8') as f:
            master_prompt = f.read()
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'prompts/reel_prompt.md'.")
        return

    ### CAMBIO: Bloque de bienvenida para contextualizar al usuario.
    print("======================================================")
    print("🤖 Asistente de Creación de Guiones para Reels 🤖")
    print("======================================================")
    print("Este script generará un guion para un video corto (Reel/TikTok).")
    print("Por favor, proporciona la siguiente información cuando se te solicite.")
    print("------------------------------------------------------\n")

    ### CAMBIO: Bloque de entrada #1, con descripción clara.
    print("PASO 1: Define tu negocio.")
    print("Ejemplos: 'una panadería artesanal', 'un taller de bicicletas', 'una florería'")
    # El símbolo ">" indica claramente que el programa espera una entrada.
    business_type = input("➡️  Introduce el tipo de negocio: ")

    print("\n------------------------------------------------------\n")

    ### CAMBIO: Bloque de entrada #2, con descripción clara.
    print("PASO 2: Define el tema del video.")
    print("Ejemplos: 'mostrar el proceso del pan', 'un tip para ajustar los frenos'")
    video_topic = input("➡️  Introduce el tema del video: ")

    final_prompt = master_prompt.replace("[TIPO_DE_NEGOCIO]", business_type)
    final_prompt = final_prompt.replace("[TEMA_DEL_VIDEO]", video_topic)

    print("\n======================================================")
    ### CAMBIO: Mensaje de espera más visible.
    print("⏳  Procesando con IA... El guion se está generando. Por favor, espera.")
    print("======================================================")

    generated_script = get_gemini_response(final_prompt)
    
    print("\n--- ✅ INICIO DEL GUION GENERADO ---\n")
    print(generated_script)
    print("\n--- FIN DEL GUION GENERADO ---")
    
    ### CAMBIO: Mensaje de finalización.
    print("\nProceso completado exitosamente.")


if __name__ == "__main__":
    main()