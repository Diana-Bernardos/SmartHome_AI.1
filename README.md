# 🏠 Asistente Domótico Inteligente v2.0 - Full Stack AI

## 📋 Descripción del Proyecto

Este proyecto es un **Sistema de Asistencia Domótica Completo** que combina un cerebro de **Inteligencia Artificial Local (Ollama)** con una interfaz web moderna en **React** y un backend robusto en **Python (FastAPI)**.

Permite controlar dispositivos del hogar mediante lenguaje natural, manteniendo conversaciones fluidas y contextuales.

### 🌟 Características Principales
*   **🧠 IA Local y Privada**: Usa modelos LLM (como Phi-3 o Llama 3) corriendo en tu propio equipo con **Ollama**.
*   **💻 Interfaz Moderna**: Web App reactiva construida con **React, Vite y Tailwind CSS**.
*   **⚡ Backend Rápido**: API REST construida con **FastAPI**.
*   **🗣️ Conversación Natural**: Entiende saludos, contexto y comandos complejos.
*   **🔌 Fallback Mode**: Funciona incluso si la IA no está disponible (modo básico por reglas).

---

## 🚀 Guía de Inicio Rápido

### Requisitos Previos
1.  **Python 3.8+** instalado.
2.  **Node.js y npm** instalados (para el frontend).
3.  **Ollama** instalado y ejecutándose (recomendado para la experiencia completa).

### 🛠️ Instalación (Solo la primera vez)

1.  **Clonar el repositorio**:
    ```bash
    git clone https://github.com/Diana-Bernardos/SmartHome_AI.1.git
    cd SmartHome_AI.1
    ```

2.  **Instalar dependencias del Backend**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Instalar dependencias del Frontend**:
    ```bash
    cd frontend
    npm install
    cd ..
    ```

4.  **(Opcional) Preparar IA**:
    Asegúrate de tener un modelo descargado en Ollama (ej. Phi-3):
    ```bash
    ollama pull phi3
    ```

---

## ▶️ Ejecución del Proyecto

### 🟢 Opción A: Automática (Recomendada)
Simplemente ejecuta el script **`start_app.bat`** haciendo doble clic o desde la terminal:

```powershell
.\start_app.bat
```
*   Esto abrirá automáticamente el servidor Backend (puerto 8000) y el Frontend (puerto 5173).
*   Se abrirá tu navegador en `http://localhost:5173`.

### 🟡 Opción B: Ejecución Manual
Si prefieres tener control total, necesitas dos terminales:

**Terminal 1 (Backend - API):**
```bash
python -m uvicorn api:app --reload --host 0.0.0.0 --port 8000
```
*El backend estará disponible en: http://localhost:8000*

**Terminal 2 (Frontend - Web):**
```bash
cd frontend
npm run dev
```
*El frontend estará disponible en: http://localhost:5173*

---

## 📁 Estructura del Proyecto

```
asistente_domotico/
│
├── 🐍 Backend (Python)
│   ├── api.py               # API FastAPI (Endpoints principales)
│   ├── main.py              # Lógica de conversación y chat
│   ├── parser.py            # Motor de IA (Conexión con Ollama)
│   ├── acciones.py          # Ejecución de comandos domóticos
│   └── requirements.txt     # Dependencias Python
│
├── ⚛️ Frontend (React)
│   ├── frontend/            # Carpeta del proyecto React
│   ├── src/                 # Código fuente React
│   └── start_app.bat        # Script de inicio automático
│
└── 📄 Documentación
    └── README.md
```

## 🛠️ Tecnologías

*   **Frontend**: React, Vite, TailwindCSS.
*   **Backend**: Python, FastAPI, Uvicorn.
*   **IA / NLP**: Ollama (modelos locales), Regex (fallback).

## 🐛 Solución de Problemas

1.  **"Ollama connection refused"**: Asegúrate de que Ollama está ejecutándose en segundo plano (`ollama serve` o icono en barra de tareas).
2.  **Frontend no carga**: Verifica que ejecutaste `npm install` dentro de la carpeta `frontend`.
3.  **Error en puertos**: Asegúrate de que los puertos 8000 y 5173 no estén ocupados por otra aplicación.

---
**Desarrollado por [Diana Bernardos] - Enero 2026**