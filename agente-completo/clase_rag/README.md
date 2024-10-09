# Clase: Sumar Tool de RAG al Agente

Sigue estos pasos para agregar una herramienta de Retrieval Augmented Generation (RAG) a tu agente:

1. Instalar librerías necesarias (dentro del venv):
   ```
   pip install langchain-chroma pypdf
   ```

2. Actualizar librerías existentes(dentro del venv):
   ```
   pip install --upgrade langchain-groq langchain pydantic
   ```

3. Crear una carpeta 'docs':
   - Crea una nueva carpeta llamada 'docs' al mismo nivel que los otros archivos del proyecto.
   - Carga en esta carpeta el archivo PDF que tu grupo recibió sobre el caso.

4. Configurar la API Key de OpenAI:
   - Abre el archivo `.env`. 
   - Agrega la siguiente línea con tu API Key de OpenAI:
     ```
     OPENAI_API_KEY=tu_api_key_aqui
     ```
   - Guarda el archivo `.env`.
   - **IMPORTANTE**: No subas (push) este archivo al repositorio para mantener tu API Key segura.

5. Ejecutar test-RAG:
   - Corre el notebook `test-RAG.ipynb` para crear la base de datos vectorial y probar que funcione correctamente.

6. Modificar chat.py:
   - Abre el archivo `chat.py`.
   - Modifica el código para cargar la base de datos vectorial y crear la tool
   - Asegúrate de que el agente se cree con "openai" en lugar de "groq".

7. Probar el agente:
   - Inicia una conversación con el agente (streamlit chat)
   - Intenta formular preguntas que requieran el uso de las herramientas RAG.
   - Verifica en LangSmith cómo se está utilizando la herramienta durante la conversación.

Siguiendo estos pasos, habrás integrado exitosamente una herramienta RAG a tu agente, permitiéndole acceder y utilizar la información del documento PDF en sus respuestas.
