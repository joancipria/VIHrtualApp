# VIHrtual-App (Servidor)
VIHrtual-App es un chatbot de código libre para la divulgación médica del VIH. Este repositorio contiene el código fuente del servidor. Puedes acceder al repositorio del cliente web desde [aquí](https://github.com/joancipria/VIHrtualApp-app/).

<img style="width: 60%" title="a title" alt="Alt text" src="https://raw.githubusercontent.com/joancipria/VIHrtualApp-app/master/screenshot.png">

## 📦 Instalación
Testeado con `Python 3.7.11` y `pip 20.1.1`. Versión de Rasa: `Rasa: 2.8.10` `Rasa SDK: 2.8.2` y `Rasa X: 0.39.3`. Podría dar problemas en versiones posteriores.

Clona el repositorio
```
git clone https://github.com/joancipria/VIHrtualApp.git
cd VIHrtualApp
```
Crea un entorno virtual de Python 3.7
```
python3.7 -m venv ./venv
source ./venv/bin/activate
```

Descarga e instala los requisitos
```
pip3 install rasa-x==0.39.3 --extra-index-url https://pypi.rasa.com/simple
pip3 install SQLAlchemy==1.3.22
pip3 install rasa[spacy] 
python3 -m spacy download es_core_news_md
```

Si utilizas como terminal `zsh` utiliza `pip install -U "rasa[spacy]"`.

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