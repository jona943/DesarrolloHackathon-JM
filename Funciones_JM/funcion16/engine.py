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
    Script para reescribir un texto en diferentes tonos.
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
        print(f"Error: No se encontró el archivo 'prompt.md' en la carpeta 'tone_translator'.")
        return

    # --- Interfaz de Usuario ---
    print("======================================================")
    print("🎭 Traductor de Tono 🎭")
    print("======================================================")
    print("Adapta tu mensaje para cualquier situación.")
    
    original_text = input("➡️  Escribe el texto que quieres transformar: ")

    print("\nElige el tono al que quieres traducir tu texto:")
    tones = ["Profesional", "Divertido", "Urgente", "Amigable", "Persuasivo"]
    for i, tone in enumerate(tones, 1):
        print(f"  {i}. {tone}")
    
    choice = ""
    while not choice.isdigit() or not 1 <= int(choice) <= len(tones):
        choice = input(f"➡️  Selecciona un número (1-{len(tones)}): ")

    desired_tone = tones[int(choice) - 1]

    # --- Construcción y Ejecución del Prompt ---
    final_prompt = master_prompt.replace("[TEXTO_ORIGINAL]", original_text)
    final_prompt = final_prompt.replace("[TONO_DESEADO]", desired_tone)


    print("\n======================================================")
    print(f"⏳  Traduciendo tu texto a un tono '{desired_tone}'... Por favor, espera.")
    print("======================================================")

    rewritten_text = get_gemini_response(final_prompt)
    
    print("\n--- ✅ TEXTO REESCRITO ---\n")
    print(rewritten_text)
    print("\n--- FIN DEL TEXTO ---")
    
    print("\nProceso completado exitosamente.")


if __name__ == "__main__":
    main()
