# 🏆 API de Donaciones

Esta es una API desarrollada en **Django** que permite registrar y consultar donaciones de usuarios.

## 📌 Características
- 📤 **Registrar donaciones**
- 📊 **Obtener el total donado**
- 🌜 **Consultar las últimas donaciones**
- 🐳 **Desplegable con Docker**

---

## 🛠️ Tecnologías utilizadas
Este proyecto está desarrollado con:
- **🐍 Python con Django** (Django Rest Framework)
- **🐘 PostgreSQL** como base de datos
- **🐳 Docker & Docker Compose** para su ejecución

---

## 🚀 Instalación
### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/tuusuario/tu-repo.git
cd tu-repo
```

### 2️⃣ Configurar el entorno
Crea un archivo `.env` con las credenciales de la base de datos:
```env
DATABASE_URL=postgres://postgres:password@tu-db-host:5432/tu-db-name
```

### 3️⃣ Construir y ejecutar con Docker Compose
```bash
docker-compose up --build
```

---

## 💻 Endpoints

### 1️⃣ Registrar una donación 📝
- **Método:** `POST`
- **URL:** `/api/donate/`
- **Body:**
```json
{
    "name": "John Doe",
    "phone_number": "+123456789",
    "email": "john@example.com",
    "donation_amount": "100.50"
}
```
- **Respuesta:**
```json
{
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "name": "John Doe",
    "phone_number": "+123456789",
    "email": "john@example.com",
    "donation_amount": "100.50",
    "created_at": "2025-03-28T18:43:08.905423Z"
}
```

---

### 2️⃣ Obtener el total donado 💰
- **Método:** `GET`
- **URL:** `/api/total-donations/`
- **Respuesta:**
```json
{
    "total_donation_amount": 300.5
}
```

---

### 3️⃣ Últimas 5 donaciones 🕒
- **Método:** `GET`
- **URL:** `/api/last-donations/`
- **Respuesta:**
```json
[
    {
        "name": "Alejandro",
        "donation_amount": "200.00",
        "created_at": "2025-03-28T18:43:08.905423Z"
    },
    {
        "name": "John Doe",
        "donation_amount": "100.50",
        "created_at": "2025-03-28T18:43:08.905423Z"
    }
]
```

---

## 🔥 Cómo contribuir
Si quieres mejorar esta API:
1. Haz un fork del repositorio
2. Crea una nueva rama (`git checkout -b feature-nueva`)
3. Realiza tus cambios y haz commit (`git commit -m 'Nueva funcionalidad'`)
4. Sube tus cambios (`git push origin feature-nueva`)
5. Abre un Pull Request 🚀

---

## 📞 Contacto
👨‍💻 Desarrollado por [Alejandro Castellanos](https://github.com/alejandrocastellanos) 🚀

