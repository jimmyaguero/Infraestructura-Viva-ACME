# Proyecto: Infraestructura Viva - ACME Solutions 
**Por: Jimmy Agüero - Estudiante Arquitecto Cloud**

##  Descripción del Proyecto
Este proyecto documenta la migración de una infraestructura *on-premise* hacia una arquitectura elástica y segura en **Amazon Web Services (AWS)**. El objetivo es resolver los desafíos de escalabilidad y altos costos operativos de los departamentos de Ventas, Soporte y Finanzas de "Soluciones Digitales ACME".

##  Arquitectura de la Solución
La infraestructura sigue un modelo de **3 capas (3-Tier Architecture)**, garantizando alta disponibilidad y seguridad perimetral.



### Componentes Clave:
* **Networking:** VPC segmentada con subredes públicas (ALB) y privadas (EC2/RDS).
* **Cómputo:** Instancias Amazon EC2 y AWS Lambda para lógica de negocio.
* **Almacenamiento:** Amazon S3 con políticas de Ciclo de Vida hacia S3 Glacier para optimización de costos.
* **Base de Datos:** Amazon RDS (MySQL) con Multi-AZ y Amazon DynamoDB (NoSQL).
* **Entrega:** Amazon CloudFront (CDN) para aceleración de contenido estático.
* **Monitoreo:** Alarmas de CloudWatch integradas con Amazon SNS para notificaciones automáticas.

##  Herramientas Utilizadas
* **AWS Academy:** Entorno de despliegue y validación de infraestructura.
* **Visual Studio Code:** IDE principal para desarrollo de scripts en Python (Boto3).
* **SQLiteOnline:** Prototipado rápido de modelos relacionales y validación de consultas SQL.

##  Estructura del Repositorio
* `/src`: Scripts de automatización en Python para gestión de recursos.
* `/sql`: Definición de tablas y consultas de validación probadas en SQLiteOnline.
* `/web`: Código fuente del `index.html` servido vía S3 + CloudFront.
* `/docs`: Documentación detallada del proyecto y capturas de pantalla de las 8 lecciones.

##  Instrucciones de Despliegue
1.  **Red:** Configurar VPC y Security Groups con el principio de menor privilegio.
2.  **Base de Datos:** Lanzar RDS MySQL en subred privada permitiendo tráfico solo desde la capa de cómputo.
3.  **Cómputo:** Desplegar instancia EC2 t2.micro y configurar el archivo `.env` con las credenciales de base de datos.
4.  **Monitoreo:** Crear alarma en CloudWatch para el umbral de CPU > 80% vinculada a un tópico de SNS.

##  Buenas Prácticas Aplicadas
* **Seguridad:** Aislamiento total de la capa de datos en subredes privadas.
* **Resiliencia:** Uso de SQS para desacoplamiento y Dead Letter Queues (DLQ) para gestión de errores.
* **Optimización:** Uso de niveles de almacenamiento en S3 para reducir el gasto mensual.

---
*Este proyecto es parte del portafolio académico para la certificación de Arquitectura Cloud.*
