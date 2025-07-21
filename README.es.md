[![Python](https://img.shields.io/badge/code-Python-green?logo=python)](README.md)
[![EN](https://img.shields.io/badge/lang-ES-red?logo=translate)](README.md)

# AI AGENT 🤖


Una herramienta CLI en Python impulsada por IA que ejecuta _prompts_ usando funciones predefinidas.

## Descripción 

AI agent es una herramienta CLI construída usando la API de Google Gemini.
Esta, acepta una tarea de código a través de un _prompt_ y elige
de una lista de funciones disponibles para cumplir con la tarea.


## Por qué?

Estamos en una época de incertumbre gobernada por el concepto de la IA. Esta herramienta, ayuda a mitigar el miedo general que se asocia a la IA (que nos vaya a quitar el trabajo a todos) y ayuda a consolidar un pensamiento inclinado a tomar este recurso, como una herramienta que nos puede servir como ayuda en tareas tediosas del día a día (en este caso, relacionadas con el desarrollo de software).

## Funcionamiento

Este aplicación usa la API de Google Gemini para realizar tareas basadas en _prompts_ escritos en la CLI (interfaz de comando de líneas).

Al agente de IA, se le dá una lista de funciones pre-definidas para que realice estas tareas.
Se itera sobre estas funciones hasta cumplir con el objetivo o 
hasta llegar a un número máximo (constante predeterminada) de intentos.

> El llamado a esta IA está pre-configurado para que se comporte como un ayudante de revisión y corrección de código cada vez que se solicita ejecutar un prompt. La configuración se encuentra en el archivo _config.py_.


Este programa en Python contiene las siguientes funciones:

- __get_file_content__:
    - Devuelve una lista de los contenidos (y su tamaño) de un directorio dado.
    - El directorio debe estar contenido dentro del directorio de trabajo.
    - Si no se pasa ningún argumento de directorio, en su lugar se usa el directorio de trabajo.

- __get_files_info__:
    - Devuelve los contenidos del archivo de una ruta dada.
    - La ruta al archivo debe estar contenida en el directorio de trabajo.
    - El contenido devuelto es truncado si excede un número máximo de caracteres establecido en una constante.

- __write_file__:
    - Escribe los contenidos pasados en un argumento al archivo de una ruta dada.
    - La ruta al archivo debe estar contenida en el directorio de trabajo.
    - Si el archivo no existe, este mismo es creado.

- __run_python_file__:
    - Ejecuta el código de un archivo ".py" en una ruta dada.
    - La ruta al archivo debe estar contenida en el directorio de trabajo.
    - Puede devolver stdout o stderr de archivo ejecutado.


> Funciones adicionales pueden ser creadas para que el programa las use. Tienen que estar alojadas en el directorio **/functions** , y junto a la función, se debe definir un **types.FunctionDeclaration()** y ser agregado a la lista de funciones disponibles (available_functions) dentro de **call_function.py** para que el cliente IA las pueda utilizar. 

## Pre-requisitos

- Tener Python 3.10+ instalado en tu sistema.
- Acceso a un shell tipo Unix.
- Crear una cuenta en [Google AI Studio](https://aistudio.google.com/) y luego obtener una *API KEY*.

## Preparación

- En el directorio base, crear un archivo ".env" y alojar la ApiKey de Gemini:
```bash
GEMINI_API_KEY="your_api_key_here"
```

- Crear y ejecutar un entorno virtual:
```bash
python3 -m venv venv
source venv/bin/activate
```

- Instala los contenidos de requirements.txt:
```bash
pip install -r requirements.txt
```

## Uso

Hay una aplicación de calculadora en Python en el directorio /calculator, para ser utilizado en demostraciones. Por ejemplo, puedes entrar a **/calculator/main.py** y modificar el valor de **precedence** para el operador "**+**" , y usar el agente para que revise y corrija el codigo, de la siguiente manera:

```bash
python3 main.py "arregla el bug en la calculadora, no arroja resultados precisos en la operación de 'sum'"
```

También puedes importar código nuevo y usar el agente para trabajar con él.

Puedes agregar un agumento "--verbose" junto a tu "prompt" y el programa imprimirá información adicional sobre los tokens de solicitud y respuestas. Esta información es útil para llevar cuentas sobre el uso de la API de google y tener en cuenta para los cobros de la misma en tu cuenta.


## 🤝 Contribuciones

Siéntase libre the hacer un fork del repositorio y abrir un pull request de la rama `main`. 
