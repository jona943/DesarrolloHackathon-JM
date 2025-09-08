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
    Script para generar ideas de promociones para un negocio.
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
        print(f"Error: No se encontró el archivo 'prompt.md' en la carpeta 'promo_brainstormer'.")
        return

    # --- Interfaz de Usuario ---
    print("======================================================")
    print("💡 Brainstorming de Promociones 💡")
    print("======================================================")
    print("Genera ideas creativas para impulsar tus ventas.")
    
    business_type = input("➡️  Introduce el tipo de negocio (ej. 'zapatería'): ")
    promo_context = input("➡️  Introduce un contexto o temporada (ej. 'Día de las Madres', 'verano') (opcional, presiona Enter para omitir): ")

    # --- Construcción y Ejecución del Prompt ---
    final_prompt = master_prompt.replace("[TIPO_DE_NEGOCIO]", business_type)
    final_prompt = final_prompt.replace("[CONTEXTO_PROMO]", promo_context)


    print("\n======================================================")
    print("⏳  Cocinando algunas ideas creativas... Por favor, espera.")
    print("======================================================")

    generated_ideas = get_gemini_response(final_prompt)
    
    print("\n--- ✅ 5 IDEAS DE PROMOCIONES PARA TU NEGOCIO ---\n")
    print(generated_ideas)
    print("\n--- FIN DE LAS IDEAS ---")
    
    print("\nProceso completado exitosamente.")


if __name__ == "__main__":
    main()
