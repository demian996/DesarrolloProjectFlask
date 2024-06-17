import pyodbc

def conexionBD():
    try:
        connection = pyodbc.connect(
            "Driver={SQL Server};"
            "Server=DESKTOP-62IIC02\SQLEXPRESS;"
            "Database=DBEmpleadosFlask;"
            "Trusted_Connection=yes;"
        )
        print("Conexión exitosa")
        return connection.cursor()
    except Exception as ex:
        print(ex)
        return None
