# 🤖 Alma Local - Herramientas de IA para Negocios  

Este repositorio contiene una colección de **scripts en Python** diseñados para potenciar a los negocios locales utilizando la **API de Google Gemini**.  
Cada script es una herramienta independiente que realiza una tarea específica (ej: generar guiones para Reels, crear misiones de empresa, etc.).  

---

## 📋 Prerrequisitos  

- Tener instalado **Python 3** en tu sistema.  
- Verifica la versión:  

```bash
python3 --version   # macOS / Linux
python --version    # Windows

Si no está instalado, descárgalo desde python.org.

⸻

🚀 Guía de Instalación y Configuración

Paso 1: Obtén el Proyecto

Descarga o clona este repositorio y colócalo en tu computadora, por ejemplo:

DesarrolloHackathon-JM/

Paso 2: Configura tu API Key
	1.	Crea un archivo .env en la carpeta raíz del proyecto.
	2.	Obtén tu API Key en Google AI Studio.
	3.	Agrega tu clave dentro del archivo .env:

GEMINI_API_KEY="TU_API_KEY_AQUI"



Paso 3: Instala las Dependencias

Abre tu terminal y navega hasta la carpeta raíz (DesarrolloHackathon-JM/).
Luego ejecuta el comando según tu sistema:

🍎 macOS

cd ruta/a/DesarrolloHackathon-JM
pip3 install -r requirements.txt

🐧 Linux (Ubuntu)

cd ruta/a/DesarrolloHackathon-JM

# Instalar pip si no lo tienes
sudo apt update
sudo apt install python3-pip

# Instalar dependencias
pip3 install -r requirements.txt

🪟 Windows

cd C:\ruta\a\DesarrolloHackathon-JM
py -m pip install -r requirements.txt

💡 En algunos casos el comando puede ser python en lugar de py.

⸻

🛠️ Cómo Usar las Herramientas

Todos los scripts se ejecutan desde la carpeta raíz del proyecto.

Ejemplo: Generador de Reels
	1.	Abre tu terminal.
	2.	Asegúrate de estar en la carpeta raíz (DesarrolloHackathon-JM).
	3.	Ejecuta el script:

	•	macOS / Linux:

python3 tools/reel_generator.py


	•	Windows:

py tools/reel_generator.py



El programa se iniciará en modo interactivo y pedirá la información necesaria.
¡Sigue las instrucciones en pantalla y obtendrás tu resultado! 🎉

⸻

📂 Estructura del Proyecto

DesarrolloHackathon-JM/
│── tools/                # Scripts individuales (ej. reel_generator.py)
│── requirements.txt      # Librerías necesarias
│── .env                  # Clave privada de Gemini (no compartir)
│── README.md             # Este archivo


⸻

✨ Notas
	•	Cada herramienta dentro de tools/ es independiente.
	•	Puedes duplicar la estructura de ejecución para cada script nuevo.
	•	El proyecto crecerá con más utilidades enfocadas en negocios locales.
	