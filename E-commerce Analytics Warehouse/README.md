# 🏪 E-commerce Analytics Warehouse

> **📦 Data Engineering Portfolio Project**  
> _Modelo de datos analíticos para e-commerce_

---

## 🚀 Descripción

Diseño e implementación de un **Data Warehouse** con arquitectura en **estrella**, ideal para análisis de ventas, productos y comportamiento de clientes en un entorno simulado de e-commerce.

Este proyecto replica un entorno realista usando herramientas modernas del stack de ingeniería de datos, incluyendo automatización de ETLs y modelado de datos con buenas prácticas.

---

## 🧰 Stack Tecnológico

| Herramienta     | Descripción                              |
|-----------------|------------------------------------------|
| 🐘 **PostgreSQL**      | Almacenamiento de datos (dockerizado)       |
| 🐍 **Python**          | Generación de datos y scripts               |
| 🧪 **SQLAlchemy**      | Conexión ORM entre Python y PostgreSQL      |
| 🔧 **dbt (Data Build Tool)** | Transformación y modelado de datos         |
| 🧬 **Faker**           | Generación de datos sintéticos              |
| 🐳 **Docker**          | Entorno aislado y reproducible              |

---

## 🗃️ Modelo de Datos

Modelo en estrella compuesto por:

- 📊 **sales** → Hechos de ventas  
- 👥 **customers** → Dimensión clientes  
- 📦 **products** → Dimensión productos  
- 🕒 **time** → Dimensión temporal  
- 🏬 **stores** → Dimensión tiendas  

> El modelo permite responder preguntas analíticas clave como:
> - ¿Qué productos se venden más?
> - ¿Qué tiendas tienen mayor rendimiento?
> - ¿Cómo varían las ventas por fecha o categoría?

---

## 📈 Tareas Realizadas

✅ Normalización de datos de clientes y productos  
✅ Diseño de esquema en estrella optimizado para analítica  
✅ Implementación de **Slowly Changing Dimensions (SCD)**  
✅ Automatización de transformaciones con **dbt**  
✅ Simulación de entorno de datos con Python + Faker  
✅ Contenerización del entorno con **Docker**

---

## 💡 ¿Por qué este proyecto?

Este repositorio demuestra habilidades clave de un Ingeniero de Datos:

- Diseño de modelos analíticos eficientes
- Automatización de pipelines de transformación
- Uso de herramientas modernas del ecosistema de datos
- Aplicación de buenas prácticas de documentación y versionado

---

📂 **Explora el código**, revisa el modelo y mira cómo transformar datos en valor.
