
from connect import get_db_connection


def view_professors():
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM profesores;")
        professors = cur.fetchall()
        
        if not professors:
            print("No hay profesores registrados.\n")
            return
        
        for professor in professors:
            print(professor)
        print("----------- Total de profesores: ", len(professors), "\n") 
    finally:
         conn.close()
    
def insert_professor():
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        name = input("Ingresa el nombre del nuevo profesor: ")
        cur.execute("INSERT INTO profesores (nombre) VALUES (%s);", (name,))
        conn.commit()
        print(f"Profesor '{name}' insertado correctamente.\n")
        cur.close()
    finally:
        conn.close()

def menu():

    print(" === Menu === ")
    print("1. Mostrar lista de profesores   ")
    print("2. Insertar nuevo profesor")
    print("3. salir")
    choice = input("Seleciona una opcion (1-3): ")
    
    if choice not in ['1', '2', '3']:
        print("Opcion invalida. Por favor, intenta de nuevo.")
        return menu()
    
    if choice == '1':
        view_professors()
    elif choice == '2':
        insert_professor()
    elif choice == '3':
        print("Saliendo del programa. ¡Hasta luego!")
        exit()
    
if  __name__ == "__main__":
    menu()