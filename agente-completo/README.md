1. Instalar esta nueva libreria en el mismo entorno virtual que la clase pasada:
   ```
   pip install langchain_openai
   ```
   
   Nota: Si aparece un error en rojo durante la instalación, no te preocupes. Continúa con la instalación y verifica después si la librería ya no aparece subrayada en el código. Si es así, la instalación se ha completado correctamente a pesar del mensaje de error.


2. Copiar los archivos `LangGraph.py`, `agent.py`, y `chat.py` a tu repositorio:

   - Copiar los archivos `LangGraph.py`, `agent.py`, y `chat.py` del repositorio del curso.
   - Colocar estos archivos en el mismo directorio donde tienes el notebook de la clase anterior (al mismo nivel que el archivo `mi-primer-agente.ipynb`). **Asegúrate de mantener los mismos nombres de archivo: `LangGraph.py`, `agent.py`, y `chat.py`.**

3. Completar en `chat.py` el prompt de la clase pasada.


4. Guardar todos los cambios:

   Asegúrate de guardar todos los archivos que has modificado o creado:
   
   - `LangGraph.py`
   - `agent.py`
   - `chat.py`

   Es importante guardar los cambios antes de ejecutar la aplicación para asegurarte de que estás utilizando la versión más reciente de tu código.



5. Ejecutar la aplicación Streamlit:
   
   Abre una terminal, navega hasta el directorio donde se encuentra el archivo `chat.py`, y ejecuta el siguiente comando:

   ```
   streamlit run chat.py
   ```

   Esto iniciará la aplicación web de Streamlit y abrirá automáticamente una nueva pestaña en tu navegador predeterminado con la interfaz de chat.




   


