# Mi Portafolio — Angelo Navarrete

Portafolio profesional personal, desarrollado con Flask. Muestra mi perfil, formación, experiencia, proyectos y un formulario de contacto funcional.

**Sitio en vivo:** _(https://portafolio-profesional-ks4b.onrender.com)_

---

## Stack técnico

- **Backend:** Flask 3.0 (patrón *app factory* + Blueprints)
- **Frontend:** Bootstrap 5.3, Jinja2
- **Formularios:** Flask-WTF
- **Correo:** Flask-Mail (SMTP de Gmail)
- **Tipografía:** Source Serif 4, Inter, IBM Plex Mono (Google Fonts)
- **Despliegue:** Render (plan gratuito)
- **Sin base de datos** — el sitio no almacena información, es un portafolio estático en contenido

---

## Estructura del proyecto
Portafolio-profesional/
├── main.py # Punto de entrada (desarrollo local y producción)
├── requirements.txt # Dependencias de Python
├── .env.example # Plantilla de variables de entorno (sin datos reales)
└── app/
├── init.py # App factory
├── config.py # Configuración (lee variables de entorno)
├── errores.py # Manejo de errores 404/500
├── blueprints/
│ └── main/ # Rutas: inicio, sobre mí, estudios, experiencia,
│ # proyectos (listado + detalle), contacto
├── templates/
│ ├── base.html
│ ├── partials/ # navbar.html, footer.html
│ ├── main/
│ │ ├── home.html, sobre_mi.html, estudios.html, experiencia.html
│ │ ├── proyectos.html # listado de proyectos
│ │ ├── proyecto_verova.html # detalle — Verova
│ │ ├── proyecto_edificio_sigma.html # detalle — Edificio Sigma
│ │ ├── proyecto_agente_cripto.html # detalle — Agente de Criptomonedas
│ │ └── contacto.html
│ └── errores/
└── static/
├── css/style.css
├── js/main.js
└── img/

---

## Cómo correrlo en tu computadora

### 1. Clona el repositorio

```bash
git clone https://github.com/Navo1804/Portafolio-profesional.git
cd Portafolio-profesional
```

### 2. Crea y activa un entorno virtual

**Windows (CMD o PowerShell):**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

Sabrás que quedó activado porque verás `(venv)` al inicio de la línea de tu terminal.

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configura las variables de entorno

Copia `.env.example` y renombra la copia a `.env`.

- **Windows (CMD):** `copy .env.example .env`
- **macOS / Linux:** `cp .env.example .env`

Abre el nuevo archivo `.env` y completa tus datos reales (correo de Gmail, [contraseña de aplicación](https://myaccount.google.com/apppasswords), teléfono, WhatsApp). Este archivo **nunca se sube a GitHub** (ya está en `.gitignore`).

### 5. Ejecuta el servidor

**Windows:**
```bash
python main.py
```

**macOS / Linux:**
```bash
python3 main.py
```

Abre [http://127.0.0.1:5000](http://127.0.0.1:5000) en tu navegador.

---

## Despliegue en producción (Render)

El sitio está desplegado en [Render](https://render.com), plan gratuito. Pasos para replicarlo:

1. Sube el repositorio a GitHub (verifica que `.env` no esté incluido — solo `.env.example`).
2. En Render: **New + → Web Service** → conecta tu repositorio de GitHub.
3. Configuración del servicio:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn main:app`
   - **Instance Type:** Free
4. En la pestaña **Environment**, agrega manualmente cada variable de tu `.env` local: `SECRET_KEY`, `MAIL_SERVER`, `MAIL_PORT`, `MAIL_USE_TLS`, `MAIL_USERNAME`, `MAIL_PASSWORD`, `MAIL_DESTINO`, `TELEFONO_CONTACTO`, `WHATSAPP_NUMERO`.
5. Al desplegar, Render entrega una URL pública (`https://tu-proyecto.onrender.com`).

**Auto-Deploy:** cada `git push` a la rama `main` vuelve a desplegar el sitio automáticamente.

**Nota:** en el plan gratuito, el servicio "se duerme" tras ~15 minutos sin visitas — la siguiente carga puede tardar 30-60 segundos en responder mientras "despierta".

---

## Notas de seguridad

- Ninguna contraseña o clave está escrita directamente en el código — todo se lee desde variables de entorno (`.env` local, o "Environment" en Render).
- La contraseña de aplicación de Gmail debe rotarse si alguna vez se sospecha que quedó expuesta.

---

## Créditos

- Estructura de proyecto inspirada en [`gabriel-toaquiza/e-shoop`](https://github.com/gabriel-toaquiza/e-shoop).
- El proyecto **Verova**, mostrado en la sección de Proyectos, fue desarrollado en colaboración con [Gabriel Toaquiza y Juan Pacheco](https://github.com/gabriel-toaquiza).
