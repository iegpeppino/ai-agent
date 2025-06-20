[lang En](https://github.com/iegpeppino/ai-agent/blob/main/README.md)

# AI AGENT
___


### Descripción 

AI agent es una herramienta CLI construída usando la API de Google Gemini.
Esta, acepta una tarea de código a través de un "prompt" y elige
de una lista de funciones disponibles para cumplir con la tarea.
Se itera sobre estas funciones hasta cumplir con el objetivo o 
hasta llegar a un número máximo (constante predeterminada) de intentos.
___
___
### Funciones

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
___
___
### Requisitos

- Tener Python 3.10+ instalado en tu sistema.
- Acceso a un shell tipo Unix.
- Crear una cuenta en [Google AI Studio](https://aistudio.google.com/) y luego obtener una *API KEY*.


___
___

### Preparación

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
___
___
### Uso

Hay una aplicación de calculadora en Python en el directorio /calculator, para ser utilizado en demostraciones. Por ejemplo, puedes entrar a **/calculator/main.py** y modificar el valor de **precedence** para el operador "**+**" , y usar el agente para que revise y corrija el codigo, de la siguiente manera:

```bash
python3 main.py "fix the bug in calculator, it isn't yielding accurate results in the sum operation"
```

También puedes importar código nuevo y usar el agente para trabajar con él.

Puedes agregar un agumento "--verbose" junto a tu "prompt" y el programa imprimirá información adicional sobre los tokens de solicitud y respuestas. Esta información es útil para llevar cuentas sobre el uso de la API de google y tener en cuenta para los cobros de la misma en tu cuenta.


---
---