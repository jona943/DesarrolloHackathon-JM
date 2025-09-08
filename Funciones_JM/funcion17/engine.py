import os
import sys
import google.generativeai as genai
from dotenv import load_dotenv
import speech_recognition as sr

# --- Configuración de Rutas y API Key ---
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)
load_dotenv(os.path.join(project_root, '.env'))

def get_gemini_response(prompt: str) -> str:
    """Función genérica para enviar un prompt a la API de Gemini."""
    try:
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error al contactar la API de Gemini: {e}"

def transcribe_audio_from_mic():
    """Captura audio del micrófono y lo transcribe a texto."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎙️  Ajustando ruido ambiental... Un momento.")
        r.adjust_for_ambient_noise(source, duration=1)
        print("✅ ¡Listo! Di tu idea para el post ahora...")
        
        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=15)
            print("🧠  Reconociendo tu voz... Procesando.")
            text = r.recognize_google(audio, language='es-ES')
            print(f"✔️  Hemos entendido: '{text}'")
            return text
        except sr.WaitTimeoutError:
            return "ERROR: No se detectó ninguna voz. Inténtalo de nuevo."
        except sr.UnknownValueError:
            return "ERROR: No se pudo entender el audio. Habla más claro."
        except sr.RequestError as e:
            return f"ERROR: Problema con el servicio de reconocimiento de voz; {e}"

def main():
    """Script para convertir una idea hablada en un post de redes sociales."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: No se encontró la API key.")
        return
    genai.configure(api_key=api_key)

    # --- Reutilizamos el prompt del Creador de Posts (Funcionalidad #2) ---
    try:
        # La ruta ahora apunta a la carpeta 'post_creator'
        prompt_path = os.path.join(project_root, 'post_creator', 'prompt.md')
        with open(prompt_path, 'r', encoding='utf-8') as f:
            master_prompt = f.read()
    except FileNotFoundError:
        print("Error: Se necesita el módulo 'post_creator' para funcionar.")
        return

    # --- Interfaz de Usuario ---
    print("======================================================")
    print("🎙️ De Voz a Post 🎙️")
    print("======================================================")
    print("Transforma tus ideas habladas en contenido para redes sociales al instante.")
    
    # --- Paso 1: Transcripción ---
    transcribed_text = transcribe_audio_from_mic()
    
    if transcribed_text.startswith("ERROR:"):
        print(f"\n❌ {transcribed_text}")
        return

    # --- Paso 2: Redacción con IA ---
    # Usamos la transcripción como la idea principal
    final_prompt = master_prompt.replace("[IDEA_PRINCIPAL]", transcribed_text)
    # Dejamos el tono como 'Casual' por defecto para esta función rápida
    final_prompt = final_prompt.replace("[TONO_POST]", "Casual")
    
    print("\n======================================================")
    print("✍️  Redactando el post basado en tu idea... Por favor, espera.")
    print("======================================================")

    generated_post = get_gemini_response(final_prompt)
    
    print("\n--- ✅ POSTS GENERADOS A PARTIR DE TU VOZ ---\n")
    print(generated_post)
    print("\n--- FIN DE LOS POSTS ---")
    
    print("\nProceso completado exitosamente.")

if __name__ == "__main__":
    main()
