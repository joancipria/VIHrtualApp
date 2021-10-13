# VIHrtual-App
VIHrtual-App es un chatbot de código libre para la divulgación médica del VIH. Este repositorio contiene el código fuente del servidor. Puedes acceder al repositorio del cliente web desde [aquí](https://github.com/joancipria/VihrtualApp-app/).

<img style="width: 50%" title="a title" alt="Alt text" src="https://raw.githubusercontent.com/joancipria/VihrtualApp-app/master/screenshot.png">

## 📦 Instalación
Testeado con `Python 3.7.10` y `pip 20.1.1`.
Versión de Rasa: `Rasa: 2.5.1` y `Rasa X: 0.39.2`

Clona el repositorio
```
git clone https://github.com/joancipria/VihrtualApp.git
cd VihrtualApp
```
Crea un entorno virtual de Python 3.7
```
python3.7 -m venv ./venv
source ./venv/bin/activate
```

Descarga e instala los requisitos
```
pip3 install rasa-x --extra-index-url https://pypi.rasa.com/simple
pip3 install rasa[spacy]
pip install pyspellchecker
python3 -m spacy download es_core_news_md
```

## 🤖 Ejecución

Ejecuta `rasa train` para entrenar un modelo.

Ejecuta `rasa shell` si deseas hablar con el asistente a través de la terminal

Ejecuta `rasa x --rasa-x-port 8080` para arrancar el servidor (con Rasa X)

Ejecuta `rasa run -m models --enable-api --cors "*" --debug` para arrancar el servidor (sin Rasa X)

Ejecuta `rasa run actions --cors "*"` para arrancar el servidor de acciones

## 🤔 Resumen

`data/` - Contiene los datos de entrenamiento de NLU agrupados por temática. Cada carpeta puede contener los siguientes archivos:

`*_intents.yml` - Contiene `intents`.

`*_stories.yml` - Contiene historias

`*_rules.yml` - Contiene reglas

`actions/actions.py` - Contiene el código de las acciones personalizadas

`domain.yml` - El archivo de dominio. Entre otros, contiene el registro de `intents`, `slots` y `entities`

`config.yml` - Configuración del entrenamiento para `NLU pipeline` y `Policy` 

## 👨‍💻 Contribuciones
Siéntete libre de enviar una `pull request` a este repositorio con tus contribuciones.

## 📜 Licencia
Licenciado bajo GNU General Public License v3.