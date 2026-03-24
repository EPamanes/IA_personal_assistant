# IA Personal Assistant 🤖

Asistente personal inteligente con capacidad de procesamiento local e integración en línea, disponible para escritorio y dispositivos móviles.

## Características

- 🧠 **IA Híbrida**: Modelos locales (Ollama/LLaMA) + APIs en línea (OpenAI, Anthropic, Google)
- 💻 **Multiplataforma**: Aplicación de escritorio y móvil
- 🗣️ **Procesamiento de Lenguaje Natural**: Conversación inteligente
- 📅 **Gestión de Tareas**: Recordatorios, calendario, productividad
- 📊 **Análisis de Datos**: Procesamiento y visualización de información
- 🌐 **Conectividad**: Funciona offline con capacidades mejoradas online
- ⚙️ **Configurable**: Personalización completa del asistente

## Estructura del Proyecto

```
IA_personal_assistant/
├── backend/
│   ├── __init__.py
│   ├── main.py
│   ├── ai_engine.py
│   ├── api_handlers.py
│   ├── local_models.py
│   └── models/
├── desktop/
│   ├── __init__.py
│   ├── main.py
│   ├── ui/
│   │   ├── __init__.py
│   │   └── main_window.py
│   └── utils/
├── mobile/
│   ├── __init__.py
│   ├── main.py
│   └── screens/
├── shared/
│   ├── __init__.py
│   ├── database.py
│   ├── logger.py
│   ├── utils.py
│   └── constants.py
├── models/
│   ├── prompts/
│   ├── embeddings/
│   └── fine_tuned/
├── data/
│   ├── tasks/
│   ├── conversations/
│   └── user_data/
├── tests/
│   ├── __init__.py
│   ├── test_ai_engine.py
│   └── test_api_handlers.py
├── config/
│   ├── config.yml
│   └── logging.yml
├── requirements.txt
├── setup.py
├── .env.example
└── .gitignore
```

## Requisitos

- Python 3.9+
- Ollama (para modelos locales)
- PostgreSQL o SQLite (base de datos)
- pip y virtualenv

## Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/EPamanes/IA_personal_assistant.git
cd IA_personal_assistant
```

### 2. Crear entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno
```bash
cp .env.example .env
# Editar .env con tus credenciales
```

### 5. Configurar aplicación
```bash
cp config/config.yml.example config/config.yml
# Personalizar config.yml según necesidades
```

## Uso

### Backend
```bash
python -m backend.main
```

### Aplicación de Escritorio
```bash
python -m desktop.main
```

### Aplicación Móvil
```bash
python -m mobile.main
```

## Arquitectura

### Componentes Principales

1. **AI Engine**: Motor de IA híbrido (local + online)
2. **Backend API**: API REST para comunicación
3. **Desktop UI**: Interfaz gráfica con PyQt6
4. **Mobile UI**: Interfaz móvil con Kivy
5. **Database**: Persistencia de datos
6. **Logger**: Sistema de logs

### Flujo de Datos

```
Aplicación (Desktop/Mobile) → Backend API → AI Engine
                                    ↓
                            Modelo Local (Ollama)
                            API Online (OpenAI, etc)
                                    ↓
                              Database
```

## Tecnologías

- **Backend**: FastAPI, SQLAlchemy
- **Desktop**: PyQt6, Qasync
- **Mobile**: Kivy
- **IA Local**: Ollama, Langchain
- **APIs**: OpenAI, Anthropic, Google
- **Database**: SQLAlchemy + PostgreSQL/SQLite
- **Testing**: Pytest

## Configuración de IA

### Modelos Locales
```bash
ollama pull llama2
ollama pull mistral
```

### APIs Externas
Configurar claves en `.env`:
```
OPENAI_API_KEY=your_key
ANTHROPIC_API_KEY=your_key
GOOGLE_API_KEY=your_key
```

## Desarrollo

### Crear rama para feature
```bash
git checkout -b feature/nombre-feature
```

### Ejecutar tests
```bash
pytest tests/
```

### Estilo de código
```bash
black .
flake8 .
```

## Contribuir

1. Fork el proyecto
2. Crear rama de feature (`git checkout -b feature/AmazingFeature`)
3. Commit cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir Pull Request

## Licencia

Este proyecto está bajo la licencia MIT - ver el archivo LICENSE para detalles.

## Contacto

EPamanes - [@EPamanes](https://github.com/EPamanes)

## Roadmap

- [ ] Backend API completo
- [ ] Interfaz de escritorio funcional
- [ ] Interfaz móvil funcional
- [ ] Integración con Ollama
- [ ] APIs de IA en línea
- [ ] Sistema de tareas avanzado
- [ ] Análisis de datos
- [ ] Sincronización en tiempo real
- [ ] Autenticación y seguridad
- [ ] Tests unitarios completos
- [ ] Documentación API
- [ ] Docker support

---

**Estado**: En desarrollo 🚀