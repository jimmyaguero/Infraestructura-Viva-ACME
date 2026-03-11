import mysql # Librería para conectar con MySQL (RDS)
import os

# Configuración de conexión (Usa los datos de tu instancia de la Lección 2)
DB_HOST = "tu-endpoint-de-rds.amazonaws.com"
DB_USER = "admin_acme"
DB_PASS = "tu_password_seguro"
DB_NAME = "ventas_db"

def registrar_venta(producto, monto):
    try:
        # 1. Establecer conexión
        conexion = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME
        )
        
        with conexion.cursor() as cursor:
            # 2. Insertar una venta (Simulando actividad de la App)
            sql = "INSERT INTO ventas (producto, monto) VALUES (%s, %s)"
            cursor.execute(sql, (producto, monto))
            conexion.commit()
            print(f"✅ Venta de {producto} por ${monto} registrada exitosamente.")

    except Exception as e:
        print(f"❌ Error al conectar a la infraestructura: {e}")
    
    finally:
        if 'conexion' in locals():
            conexion.close()

# Ejecución de prueba
if __name__ == "__main__":
    registrar_venta("Servidor Cloud Nivel 1", 1200.50)
