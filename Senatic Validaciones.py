import pyodbc
import os
import time
           
server = 'DESKTOP-OJIBABU\\SQLEXPRESS'
bd = 'senatic1'
user = 'sa'
password = 'root'

try:  
    conex = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + bd + ';UID=' + user + ';PWD=' + password)
    print('\n¡Conexión Exitosa!\n')
except Exception as e:
    print('\nError de conexión\n', e)


# MENU PRINCIPAL 
Control=True
while Control:    
    os.system('cls')
    print ("\n############ INSTITUTO EDUCATIVA LOPERA ################")
    print ("\n################### MENU PRINCIPAL ###################")
    print ("\nSelecciona la accion que deseas realizar.\n")
    print ("1. Insertar\n")
    print ("2. Actualizar\n")
    print ("3. Eliminar\n")
    print ("4. Consultar\n")
    print ("5. Salir \n")
    print ("#####################################################\n")    
    opcion = int(input("Elija su opción del 1 al 5:  "))


# INSERTAR
    def segundomenu (): 
        os.system('cls')
        print ("\n================= OPCIONES =====================")
        print ("\nSeleccione la tabla.")
        print ("\n1. Programa")
        print ("\n2. Profesor")
        print ("\n3. Asignatura ")  
        print ("\n4. Alumno")
        print ("\n5. Regresar\n")
        print ("===============================================\n")   

    if opcion == 1:
        segundomenu ()

        insertar = int(input("Elija su opción del 1 al 5: "))
        
        if insertar == 1:
            os.system('cls')
            cur=conex.cursor()
            print("\n========== Insertar nuevo programa en la tabla ==========\n")
            id_prog = input("ID del programa: ")
            nombre = input("\nNombre del programa: ")

            try:
                # Verificar si el ID del profesor ya existe
                cur.execute("SELECT COUNT(*) FROM programa WHERE id_prog = ?", (id_prog,))
                count = cur.fetchone()[0]
                if count > 0:
                        print("\nEl ID del programa ya existe en la base de datos.\n")
                else:
                    # Insertar nuevo registro
                        sql = "INSERT INTO programa (id_prog, nombre) VALUES (?,?)"
                        cur.execute(sql, (id_prog, nombre))
                        conex.commit()
                        if cur.rowcount > 0:
                            print("\n¡El dato se ha insertado exitosamente!\n")
                        else:
                            print("\nNo se pudo insertar el dato.\n")
            except Exception as e:
                print(f"\nError al insertar el dato: {e}\n")
                conex.rollback()
            finally:
                cur.close()
                # conex.close()
            print("=============================================\n")



        elif insertar == 2:
            os.system('cls')
            cur=conex.cursor()
            print("\n========== Insertar nuevo profesor en la tabla ===========\n")
            id_prof= input("ID del profesor: ")
            nombre=input("\nNombre del profesor: ")
            try:
                cur.execute("SELECT COUNT(*) FROM profesor WHERE id_prof = ?", (id_prof,))
                count = cur.fetchone()[0]                
                if count > 0:
                    print("\nEl ID del profesor ya existe en la base de datos.\n")
                else:
                    sql = "INSERT INTO profesor (id_prof, nombre) VALUES (?, ?)"
                    cur.execute(sql, (id_prof, nombre))
                    conex.commit()
                    if cur.rowcount > 0:
                        print("\n¡El dato se ha insertado exitosamente!\n")
                    else:
                        print("\nNo se pudo insertar el dato.\n")
            except Exception as e:
                print(f"\nError al insertar el dato: {e}\n")
                conex.rollback()
            finally:
                cur.close()
            print("==============================================\n")
                    
             


        elif insertar == 3:
            os.system('cls')
            cur = conex.cursor()
            print("\n========== Insertar nueva asignatura en la tabla ===========\n") 

            id_asig = input("ID de la asignatura: ").strip()
            nombre = input("\nNombre de la asignatura: ").strip()
            id_prog = input("\nID del programa: ").strip()
            id_prof = input("\nID del profesor: ").strip()

             # Validar que el ID del programa exista
            cur.execute("SELECT COUNT(*) FROM programa WHERE id_prog = ?", id_prog)
            if cur.fetchone()[0] == 0:
                print("\nError: El ID del programa no existe.\n")
                print("==============================================\n")
                continue  # Regresar al menú de inserción

            # Validar que el ID del profesor exista
            cur.execute("SELECT COUNT(*) FROM profesor WHERE id_prof = ?", id_prof)
            if cur.fetchone()[0] == 0:
                print("\nError: El ID del profesor no existe.\n")
                print("==============================================\n")
                continue  

            try:
                # Intentar ejecutar la inserción
                sql = "Insert into asignatura (id_asig, nombre, id_prog, id_prof) values (?, ?, ?, ?)"
                cur.execute(sql, id_asig, nombre, id_prog, id_prof)
                conex.commit()
                print("\n¡El dato se ha insertado exitosamente!\n")
                print("==============================================\n")
            except Exception as e:
                # Manejar cualquier error durante la ejecución del SQL
                print("\nError al insertar los datos: ", e)
                print("==============================================\n")



        elif insertar == 4:
            os.system('cls')
            cur = conex.cursor()
            print("\n========== Insertar nuevo alumno en la tabla ============\n")

            id_alum = input("ID del alumno: ").strip()
            nombre = input("\nNombre del alumno: ").strip()
            id_prog = input("\nID del programa: ").strip()
            id_asig = input("\nID de la asignatura: ").strip()

            cur.execute("SELECT COUNT(*) FROM programa WHERE id_prog = ?", (id_prog,))
            if cur.fetchone()[0] == 0:
                print("\nError: El ID del programa no existe.\n")
                print("==============================================\n")
                continue  

            cur.execute("SELECT COUNT(*) FROM asignatura WHERE id_asig = ?", (id_asig,))
            if cur.fetchone()[0] == 0:
                print("\nError: El ID de la asignatura no existe.\n")
                print("==============================================\n")
                continue 

            try:
                sql = "INSERT INTO alumno (id_alum, nombre, id_prog, id_asig) VALUES (?, ?, ?, ?)"
                cur.execute(sql, (id_alum, nombre, id_prog, id_asig))
                conex.commit()
                print("\n¡El dato se ha insertado exitosamente!\n")
                print("==============================================\n")
            except Exception as e:
                print("\nError al insertar los datos: ", e)
                print("==============================================\n")


        elif insertar == 5:
            print("\nRegresando al menu principal...")
            time.sleep(3)
        
        else: 
            insertar == ()
            print ("\nHay un error, intentar de nuevo")
            break 



# ACTUALIZAR 
    elif opcion == 2:
        segundomenu ()
        
        actualizar = int(input("Elija su opción del 1 al 5: "))
        
        if actualizar == 1:
            os.system('cls') 
            cur=conex.cursor()
            print ("\n========== Actualizar programa de la tabla ===========\n") 
            id_prog = input("ID del Programa: ")
            nombre = input("\nNombre del programa que desea actualizar: ")

            try:
                # Verificar si el ID del programa existe en la base de datos
                cur.execute("SELECT COUNT(*) FROM programa WHERE id_prog = ?", (id_prog,))
                count = cur.fetchone()[0]
                
                if count == 0:
                    print("\nError: El ID del programa no existe en la base de datos.\n")
                else:
                    # Actualizar el nombre del programa si el ID existe
                    sql = "UPDATE programa SET nombre = ? WHERE id_prog = ?"
                    cur.execute(sql, (nombre, id_prog))
                    conex.commit()
                    if cur.rowcount > 0:
                        print("\n¡El dato de la tabla programa se ha actualizado exitosamente!\n")
                    else:
                        print("\nNo se pudo actualizar el dato. Puede que no haya cambios.\n")
            except Exception as e:
                print(f"\nError al actualizar el dato: {e}\n")
                conex.rollback()
            finally:
                cur.close()
            print ("============================================\n") 


        elif actualizar == 2:
            os.system('cls')
            cur=conex.cursor()
            print ("\n========= Actualizar profesor de la tabla ==========\n") 
            id_prof = input("ID del Profesor: ")
            nombre = input("\nNombre del profesor que desea actualizar: ")

            try:
                # Verificar si el ID del profesor existe en la base de datos
                cur.execute("SELECT COUNT(*) FROM profesor WHERE id_prof = ?", (id_prof,))
                count = cur.fetchone()[0]

                if count == 0:
                    print("\nError: El ID del profesor no existe en la base de datos.\n")
                else:
                    # Actualizar el nombre del profesor si el ID existe
                    sql = "UPDATE profesor SET nombre = ? WHERE id_prof = ?"
                    cur.execute(sql, (nombre, id_prof))
                    conex.commit()
                    if cur.rowcount > 0:
                        print("\n¡El dato de la tabla profesor se ha actualizado exitosamente!\n")
                    else:
                        print("\nError: No se pudo actualizar el dato. Puede que no haya cambios.\n")
            except Exception as e:
                print(f"\nError al actualizar el dato: {e}\n")
                conex.rollback()
            finally:
                cur.close()
            print("============================================\n")

            

        elif actualizar == 3:
            os.system('cls')
            cur=conex.cursor()
            print ("\n========= Actualizar asignatura de la tabla ==========\n")             
            id_asig = input("ID de la asignatura: ")
            nombre = input("\nNombre de la asignatura que desea actualizar: ")
            id_prog = input("\nID del programa: ")
            id_prof = input("\nID del profesor: ")

            try:
                # Verificar si el ID de la asignatura existe en la base de datos
                cur.execute("SELECT COUNT(*) FROM asignatura WHERE id_asig = ?", (id_asig,))
                count_asig = cur.fetchone()[0]

                if count_asig == 0:
                    print("\nError: El ID de la asignatura no existe en la base de datos.\n")
                else:
                    # Verificar si el ID del programa existe en la base de datos
                    cur.execute("SELECT COUNT(*) FROM programa WHERE id_prog = ?", (id_prog,))
                    count_prog = cur.fetchone()[0]

                    if count_prog == 0:
                        print("\nError:  El ID del programa no existe en la base de datos.\n")
                    else:
                        # Verificar si el ID del profesor existe en la base de datos
                        cur.execute("SELECT COUNT(*) FROM profesor WHERE id_prof = ?", (id_prof,))
                        count_prof = cur.fetchone()[0]

                        if count_prof == 0:
                            print("\nError: El ID del profesor no existe en la base de datos.\n")
                        else:
                            # Actualizar los datos de la asignatura si todo es válido
                            sql = "UPDATE asignatura SET nombre = ?, id_prog = ?, id_prof = ? WHERE id_asig = ?"
                            cur.execute(sql, (nombre, id_prog, id_prof, id_asig))
                            conex.commit()
                            if cur.rowcount > 0:
                                print("\n¡El dato de la tabla asignatura se ha actualizado exitosamente!\n")
                            else:
                                print("\nError: No se pudo actualizar el dato. Puede que no haya cambios.\n")
            except Exception as e:
                print(f"\nError al actualizar el dato: {e}\n")
                conex.rollback()
            finally:
                cur.close()
            print("============================================\n")



        elif actualizar == 4:
            os.system('cls')
            cur=conex.cursor()
            print ("\n========= Actualizar alumno de la tabla ==========\n") 
            id_alum = input("ID del alumno: ")
            nombre = input("\nNombre del alumno que desea actualizar: ")
            id_prog = input("\nID del programa: ")
            id_asig = input("\nID de la asignatura: ")

            try:
                # Verificar si el ID del alumno existe en la base de datos
                cur.execute("SELECT COUNT(*) FROM alumno WHERE id_alum = ?", (id_alum,))
                count_alum = cur.fetchone()[0]

                if count_alum == 0:
                    print("\nError: El ID del alumno no existe en la base de datos.\n")
                else:
                    # Verificar si el ID del programa existe en la base de datos
                    cur.execute("SELECT COUNT(*) FROM programa WHERE id_prog = ?", (id_prog,))
                    count_prog = cur.fetchone()[0]

                    if count_prog == 0:
                        print("\nError: El ID del programa no existe en la base de datos.\n")
                    else:
                        # Verificar si el ID de la asignatura existe en la base de datos
                        cur.execute("SELECT COUNT(*) FROM asignatura WHERE id_asig = ?", (id_asig,))
                        count_asig = cur.fetchone()[0]

                        if count_asig == 0:
                            print("\nError:  El ID de la asignatura no existe en la base de datos.\n")
                        else:
                            # Actualizar los datos del alumno si todo es válido
                            sql = "UPDATE alumno SET nombre = ?, id_prog = ?, id_asig = ? WHERE id_alum = ?"
                            cur.execute(sql, (nombre, id_prog, id_asig, id_alum))
                            conex.commit()
                            if cur.rowcount > 0:
                                print("\n¡El dato de la tabla alumno se ha actualizado exitosamente!\n")
                            else:
                                print("\nError:  No se pudo actualizar el dato. Puede que no haya cambios.\n")
            except Exception as e:
                print(f"\nError al actualizar el dato: {e}\n")
                conex.rollback()
            finally:
                cur.close()
            print("============================================\n")            


        elif actualizar == 5:
            print("\nRegresando al menu principal...")
            time.sleep(3)
        
        else:
            actualizar == ()
            print ("\nHay un error, intentar de nuevo")
            break



# ELIMINAR
    elif opcion == 3: 
        segundomenu ()
        
        eliminar =int(input("Elija su opción del 1 al 5:  "))

        if eliminar == 1:
            os.system('cls')
            cur=conex.cursor() 
            print ("\n========= Eliminar programa de la tabla ==========\n") 
            id_prog = input("ID del programa: ")

            try:
                # Verificar si el ID del programa existe en la base de datos
                cur.execute("SELECT COUNT(*) FROM programa WHERE id_prog = ?", (id_prog,))
                count_prog = cur.fetchone()[0]

                if count_prog == 0:
                    print("\nError: El ID del programa no existe en la base de datos.\n")
                else:
                    # Verificar si hay registros en la tabla 'asignatura' que referencian este ID
                    cur.execute("SELECT COUNT(*) FROM asignatura WHERE id_prog = ?", (id_prog,))
                    count_asig = cur.fetchone()[0]

                    if count_asig > 0:
                        print("\nError: El ID del programa no se puede eliminar porque hay asignaturas que lo referencian.\n")
                    else:
                        # Eliminar el programa si no hay referencias
                        sql = "DELETE FROM programa WHERE id_prog = ?"
                        cur.execute(sql, (id_prog,))
                        conex.commit()
                        if cur.rowcount > 0:
                            print("\n¡El dato de la tabla 'programa' se ha eliminado exitosamente!\n")
                        else:
                            print("\nNo se pudo eliminar el dato. Puede que no haya cambios.\n")
            except Exception as e:
                print(f"\nError al eliminar el dato: {e}\n")
                conex.rollback()
            finally:
                cur.close()
            print("============================================\n")

            
        elif eliminar == 2:
            os.system('cls')
            cur=conex.cursor() 
            print ("\n========= Eliminar profesor de la tabla ==========\n") 
            id_prof = input("ID del profesor: ")

            try:
                # Verificar si el ID del profesor existe en la base de datos
                cur.execute("SELECT COUNT(*) FROM profesor WHERE id_prof = ?", (id_prof,))
                count_prof = cur.fetchone()[0]

                if count_prof == 0:
                    print("\nError: El ID del profesor no existe en la base de datos.\n")
                else:
                    # Verificar si hay registros en la tabla 'asignatura' que referencian este ID
                    cur.execute("SELECT COUNT(*) FROM asignatura WHERE id_prof = ?", (id_prof,))
                    count_asig = cur.fetchone()[0]

                    if count_asig > 0:
                        print("\nError: El ID del profesor no se puede eliminar porque está siendo referenciado en la tabla 'asignatura'.\n")
                    else:
                        # Eliminar el profesor si no hay referencias
                        sql = "DELETE FROM profesor WHERE id_prof = ?"
                        cur.execute(sql, (id_prof,))
                        conex.commit()
                        if cur.rowcount > 0:
                            print("\n¡El dato de la tabla 'profesor' se ha eliminado exitosamente!\n")
                        else:
                            print("\nNo se pudo eliminar el dato. Puede que no haya cambios.\n")
            except Exception as e:
                print(f"\nError al eliminar el dato: {e}\n")
                conex.rollback()
            finally:
                cur.close()
            print("============================================\n")
            


        elif eliminar == 3:
            os.system('cls')
            cur=conex.cursor() 
            print ("\n========= Eliminar asignatura de la tabla ==========\n") 
            id_asig = input("ID de la asignatura: ")

            try:
                cur.execute("SELECT COUNT(*) FROM asignatura WHERE id_asig = ?", (id_asig,))
                count_asig = cur.fetchone()[0]

                if count_asig == 0:
                    print("\nEl ID de la asignatura no existe en la base de datos.\n")
                else:
                    sql = "DELETE FROM asignatura WHERE id_asig = ?"
                    cur.execute(sql, (id_asig,))
                    conex.commit()
                    if cur.rowcount > 0:
                        print("\n¡El dato de la tabla 'asignatura' se ha eliminado exitosamente!\n")
                    else:
                        print("\nNo se pudo eliminar el dato. Puede que no haya cambios.\n")
            except Exception as e:
                print(f"\nError al eliminar el dato: {e}\n")
                conex.rollback()
            finally:
                cur.close()
            print("============================================\n")


        
        elif eliminar == 4:                
            os.system('cls')
            cur=conex.cursor() 
            print ("\n========= Eliminar alumno de la tabla ==========\n") 
            id_alum = input("ID del Alumno: ")

            try:
                # Verificar si el ID del alumno existe en la base de datos
                cur.execute("SELECT COUNT(*) FROM alumno WHERE id_alum = ?", (id_alum,))
                count_alum = cur.fetchone()[0]

                if count_alum == 0:
                    print("\nError: El ID del alumno no existe en la base de datos.\n")
                else:
                    # Eliminar el alumno si el ID existe
                    sql = "DELETE FROM alumno WHERE id_alum = ?"
                    cur.execute(sql, (id_alum,))
                    conex.commit()
                    if cur.rowcount > 0:
                        print("\n¡El dato de la tabla 'alumno' se ha eliminado exitosamente!\n")
                    else:
                        print("\nNo se pudo eliminar el dato. Puede que no haya cambios.\n")
            except Exception as e:
                print(f"\nError al eliminar el dato: {e}\n")
                conex.rollback()
            finally:
                cur.close()
            print("============================================\n")        
            
            
        elif eliminar == 5:
            print("\nRegresando al menu principal automaticamente...")
            time.sleep(3)
        
        else: 
            eliminar == ()
            print ("\nHay un error, intentar de nuevo.")
            break



# CONSULTAR
    elif opcion == 4:
        
        os.system('cls')
        print ("\n================ MENU DE CONSULTA ================ ") 
        print ("\nSeleccionar la tabla que deseas ver.")
        print ("\n1. Programa")
        print ("\n2. Profesor")
        print ("\n3. Asignatura ")
        print ("\n4. Alumno")
        print ("\n5. Tabla alumno, asignatura y programa ")                   #INNER JOIN
        print ("\n6. Tabla profesor, asignatura y programa")                  
        print ("\n7. Volver al menu principal")
        print ("\n============================================== ")

        consultar = int(input("\nElija su opción del 1 al 7:  "))
        
        if consultar == 1:
                os.system('cls')
                print("\nTABLA DE PROGRAMA\n")
                cur = conex.cursor()
                cur.execute("select * from programa")
                datos = cur.fetchall()
                
                for fila in datos:
                    print(fila)
                input("\nPresione <Enter> para seguir.")


        elif consultar == 2:
                os.system('cls')
                print("\nTABLA DE PROFESOR\n")
                cur = conex.cursor()
                cur.execute("select * from profesor")
                datos = cur.fetchall()
                
                for fila in datos:
                    print(fila)
                input("\nPresione <Enter> para seguir.")
        

        elif consultar == 3:
                os.system('cls')
                print("\nTABLA DE ASIGNATURA\n")
                cur = conex.cursor()
                cur.execute("select * from asignatura")
                datos = cur.fetchall()
                
                for fila in datos:
                    print(fila)
                input("\nPresione <Enter> para seguir.")
    

        elif consultar == 4:
                os.system('cls')
                print("\nTABLA DE ALUMNO\n")
                cur = conex.cursor()
                cur.execute("select * from alumno")
                datos = cur.fetchall()
                
                for fila in datos:
                    print(fila)
                input("\nPresione <Enter> para seguir.")


        elif consultar == 5:
                os.system('cls')
                print("\nTABLA DE ALUMNO, ASIGNATURA y PROGRAMA\n")
                cur = conex.cursor()
                cur.execute("select alumno.nombre, asignatura.nombre, programa.nombre from alumno inner join asignatura on alumno.id_asig = asignatura.id_asig inner join programa on programa.id_prog = asignatura.id_prog")
                datos = cur.fetchall()

                for fila in datos:
                    print(fila)
                input("\nPresione <Enter> para seguir")

                
        elif consultar == 6:
                os.system('cls')
                print("\nTABLA DE PROFESOR, ASIGNATURA y PROGRAMA\n")
                cur = conex.cursor()
                cur.execute("select profesor.nombre, asignatura.nombre, programa.nombre from profesor inner join asignatura on profesor.id_prof = asignatura.id_prof inner join programa on programa.id_prog = asignatura.id_prog")
                datos = cur.fetchall()
                
                for fila in datos:
                    print(fila)
                input("\nPresione <Enter> para seguir")   


        elif consultar == 7:
                print("\nRegresando al menu principal...")
                time.sleep(3)

        
    elif opcion == 5:
        print("\nSaliendo del programa automaticamente...")
        exit()













