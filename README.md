# austral-gen-ai

## Creación de Entorno Virtual

Para configurar un entorno virtual, sigue estos pasos:

### 1. Crear el entorno virtual

Ejecuta el siguiente comando en tu terminal para crear un entorno virtual llamado `austral`:

```bash
python3 -m venv austral
```

### 2. Activar el entorno virtual

En la terminal de Windows:

```bash
.\austral\Scripts\activate
```

En la terminal de Mac:

```bash
source austral/bin/activate
```


### 3. Instalar las dependencias

Ejecuta el siguiente comando en tu terminal para instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecutar una App de Streamlit en Localhost

**Asegúrate de estar en el entorno virtual correcto y activo**


Ejecuta la aplicación de Streamlit:

```bash
streamlit run streamlit-chat.py
```

Accede a la aplicación de Streamlit:

```bash
http://localhost:8501
```