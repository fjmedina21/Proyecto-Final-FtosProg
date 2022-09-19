from LibProyectoFinal import *
import sys, webbrowser, folium
from prettytable import PrettyTable

def listadoCiclista():
    lc = PrettyTable()
    lc.field_names = ['Id Ciclista','Cédula','Nombre','Apellido','F. Nacimiento','Sangre','S. Bicicleta','S. Uniforme','Teléfono','Celular','E-mail','Dirección','Persona de Contacto','Tel. de Contacto']
    for c in Ciclista.select():
        lc.add_row([c.idCiclista,c.cedula,c.nombre,c.apellido,c.fNacimiento,c.tSangre,c.sizeBici,c.sizeUniforme,c.tel,c.cel,c.email,c.direccion,c.persContacto,c.telContacto])
    print(lc)

def listadoActividades():
    la = PrettyTable()
    la.field_names = ['Id Actividad','Ciclista','Fecha','Distancia Recorrida','Lugar','Latitud','Longitud','Nivel de Dificultad']
    for a in Actividades.select():
        la.add_row([a.idActividad,f"{a.nomCiclista} {a.apellCiclista}",a.fecha,f"{a.distancia} Km",a.lugar,a.lat,a.lng,a.dificultad])
    print(la)

def gestionarCiclistas():#Sección A

    def agregarCiclista():#Sección A.1
        clean()
        c = Ciclista()

        cedula = myInput("Ingrese la Cédula / 'X' para regresar: ")
        if cedula.lower() == "x":
            gestionarCiclistas()

        if validarCedula(cedula):
            if cedExist(cedula):
                msj("Esta cédula ya esta registrada")
                agregarCiclista()
            else:
                c.cedula = cedula
                c.nombre = myInput("Nombre: ").title()
                c.apellido = myInput("Apellido: ").title()
                fNacimiento = myInput("Fecha de Nacimiento (Año-Mes-Dia): ")
                while True:
                    if validarFechaNacimiento(fNacimiento):
                        c.fNacimiento = fNacimiento
                        c.tSangre = myInput("Tipo de Sangre: ").title()
                        c.sizeBici = myInput("Size de su Bicicleta (S,M,L): ").upper()
                        c.sizeUniforme = myInput("Size de su Uniforme (S,M,L): ").upper()
                        tel = myInput("Número de Teléfono (sin guiones): ")
                        while True:
                            if validarTelCel(tel):
                                c.tel = tel
                                break
                            else:
                                msj("")
                                tel = myInput("Número de Teléfono (sin guiones): ")
                        cel = myInput("Número de Celular (sin guiones): ")
                        while True:
                            if validarTelCel(cel):
                                c.cel = cel
                                break
                            else:
                                msj("")
                                cel = myInput("Número de Celular (sin guiones): ")
                        email = myInput("E-mail: ")
                        while True:
                            if emailExist(email):
                                msj("Este email ya esta registrado")
                                email = myInput("E-mail: ")
                            else:
                                c.email = email
                                break
                        c.direccion = myInput("Dirección: ")
                        c.persContacto = myInput("Persona de Contacto: ").title()
                        telContacto = myInput("Teléfono de Contacto (sin guiones): ")
                        while True:
                            if validarTelCel(telContacto):
                                c.telContacto = telContacto
                                break
                            else:
                                msj("")
                                telContacto = myInput("Número de Celular (sin guiones): ")
                        c.save()
                        msj("Nuevo ciclista agregado")
                        break
                    else:
                        msj("Intente otra vez")
                        fNacimiento = myInput("Fecha de Nacimiento (Año-Mes-Dia): ")
        else:
            msj("Intente otra vez")
            agregarCiclista()

    def modificarCiclista():#Sección A.2
        clean()
        listadoCiclista()

        opt = myInput("Seleccione el Id del ciclista que desea modificar los Datos - 'X' para regresar: ")
        if opt.lower() == "x":
            gestionarCiclistas()
        opt = int(opt)

        if idCiclistaDisp(opt):
            msj(f"El ID '{opt}' no esta registrado, intente con otro")
            modificarCiclista()
        else:
            c = Ciclista.get_by_id(opt)
            print(f"\n--No se aceptan cambios en la Cédula: {c.cedula}")
            c.nombre = myInput(c.nombre+", Editar Nombre: ",c.nombre).title()
            c.apellido = myInput(c.apellido+", Editar Apellido: ",c.apellido).title()
            fNacimiento = myInput(str(c.fNacimiento)+", Editar Fecha de Nacimiento (Año-Mes-Día): ",str(c.fNacimiento))
            while True:
                if validarFechaNacimiento(fNacimiento):
                    c.fNacimiento = fNacimiento
                    c.tSangre = myInput(c.tSangre+", Editar Tipo de Sangre: ",c.tSangre).title()
                    c.sizeBici = myInput(c.sizeBici+", Editar Size de la Bicicleta: ",c.sizeBici).upper()
                    c.sizeUniforme = myInput(c.sizeUniforme+", Editar Size del Uniforme: ",c.sizeUniforme).upper()
                    tel = myInput(c.tel+", Editar Teléfono (sin guiones): ",c.tel)
                    while True:
                            if validarTelCel(tel):
                                c.tel = tel
                                break
                            else:
                                msj("")
                                tel = myInput(c.tel+", Editar Teléfono (sin guiones): ",c.tel)
                    cel = myInput(c.cel+", Editar Celular (sin guiones): ",c.cel)
                    while True:
                            if validarTelCel(cel):
                                c.cel = cel
                                break
                            else:
                                msj("")
                                cel = myInput(c.cel+", Editar Celular (sin guiones): ",c.cel)
                    email = myInput(c.email+", Editar E-mail: ",c.email)
                    while True:
                        if emailExist(email):
                            if email == c.email:
                                c.email = email
                                break
                            else:
                                msj("Este email ya esta registrado")
                                email = myInput(c.email+", Editar E-mail: ",c.email)
                        else:
                            c.email = email
                            break
                    c.direccion = myInput(c.direccion+", Editar Dirección: ",c.direccion)
                    c.persContacto = myInput(c.persContacto+", Editar Persona de Contacto: ",c.persContacto).title()
                    telContacto = myInput(c.telContacto+", Editar Teléfon de Contacto (sin guiones): ",c.telContacto)
                    while True:
                            if validarTelCel(telContacto):
                                c.telContacto = telContacto
                                break
                            else:
                                msj("")
                                telContacto = myInput(c.telContacto+", Editar Teléfon de Contacto (sin guiones): ",c.telContacto)
                    c.save()
                    msj("Datos del ciclista actualizados")
                    break
                else:
                    msj("Intente otra vez")
                    fNacimiento = myInput(str(c.fNacimiento)+", Editar Fecha de Nacimiento (Año-Mes-Día): ",str(c.fNacimiento))

    def eliminarCiclista():#Sección A.3
        clean()
        listadoCiclista()

        opt = myInput("Seleccione el Id del ciclista que desea Eliminar - 'X' para regresar: ")
        if opt.lower() == "x":
            gestionarCiclistas()
        opt = int(opt)

        if idCiclistaDisp(opt):
            msj(f"El ID '{opt}' no esta registrado, intente con otro")
            eliminarCiclista()
        else:
            c = Ciclista.get_by_id(opt)
            c.delete_instance()
            msj("Ciclista Eliminado")

    while True:
        clean()
        tmp = PrettyTable()
        column_names = ['Sección A','Gestionar Ciclistas']
        tmp.add_column(column_names[0], ['1','2','3','X'])
        tmp.add_column(column_names[1], ['Agregar Ciclista','Modificar Ciclista','Eliminar', 'Regresar'])
        print(tmp)
        opt = myInput("Eliga una opción: ")

        if opt == "1":
            clean()
            agregarCiclista()
        elif opt == "2":
            clean()
            modificarCiclista()
        elif opt == "3":
            clean()
            eliminarCiclista()
        elif opt.lower() == "x":
            menu()
        else:
            clean()
            msj("Debes de elegir una opción valida")

def gestionarActividades():#Sección B

    def registrarActividad():#Sección B.1
        clean()
        listadoCiclista()

        opt = myInput("Seleccione el Id del ciclista para agregar una actividad - 'X' para regresar: ")
        if opt.lower() == "x":
            gestionarActividades()
        opt = int(opt)

        if idCiclistaDisp(opt):
            msj(f"El ID '{opt}' no esta registrado, intente con otro")
            registrarActividad()
        else:
            c = Ciclista.get_by_id(opt)
            clean()
            a = Actividades()
            a.nomCiclista = c.nombre
            a.apellCiclista = c.apellido
            print(f"Ciclista: {a.nomCiclista} {a.apellCiclista}")
            a.fecha = date.today()
            print(f"Fecha de la actividad: {a.fecha}")
            a.distancia = myInput("Distancia recorrida(en Kilómetros): ")
            a.lugar = myInput("Lugar donde se realizó la actividad: ").title()
            a.lat = myInput("Latitud del lugar donde se realizó la actividad: ")
            a.lng = myInput("Longitud del lugar donde se realizó la actividad: ")
            a.dificultad = myInput("Nivel de dificultad de la actividad(Bajo, Medio, Alto): ").capitalize()
            a.save()
            msj("Actividad registrada")

    def modificarActividad():#Sección B.2
        clean()
        listadoActividades()

        opt = myInput("Seleccione el Id de la actividad que desea modificar - 'X' para regresar: ")
        if opt.lower() == "x":
            gestionarActividades()
        opt = int(opt)

        if idActividadDisp(opt):
            msj(f"El ID '{opt}' no esta registrado, intente con otro")
            modificarActividad()
        else:
            a = Actividades.get_by_id(opt)
            print(f"-Para editar el nombre vaya a la sección A.2 (Modificar Ciclista)-\n\nNombre: {a.nomCiclista} {a.apellCiclista}")
            fecha = myInput(str(a.fecha)+", Editar Fecha: ",str(a.fecha))
            while True:
                if validarFecha(fecha):
                    a.fecha = fecha
                    a.distancia = myInput(f"{a.distancia} km"+", Editar Distancia recorrida: ",a.distancia)
                    a.lugar = myInput(a.lugar+", Editar Lugar de la Actividad: ",a.lugar).title()
                    a.lat = myInput(a.lat+", Editar Latitud: ",a.lat)
                    a.lng = myInput(a.lng+", Editar Longitud: ",a.lng)
                    a.dificultad = myInput( a.dificultad+", Editar Nivel Dificultad: ", a.dificultad).capitalize()
                    a.save()
                    msj("Datos de la actividad actualizados")
                    break
                else:
                    msj("Intente otra vez")
                    fecha = myInput(str(a.fecha)+", Editar Fecha: ",str(a.fecha))

    def eliminarActividad():#Sección B.3
        clean()
        listadoActividades()

        opt = myInput("Seleccione el Id de la actividad que desea Eliminar - 'X' para regresar: ")
        if opt.lower() == "x":
            gestionarActividades()
        opt = int(opt)

        if idActividadDisp(opt):
            msj(f"El ID '{opt}' no esta registrado, intente con otro")
            eliminarActividad()
        else:
            a = Actividades.get_by_id(opt)
            a.delete_instance()
            msj("Actividad Eliminada")

    while True:
        clean()
        tmp = PrettyTable()
        column_names = ['Sección B','Gestionar Actividades']
        tmp.add_column(column_names[0], ['1','2','3','X'])
        tmp.add_column(column_names[1], ['Registrar Actividad','Modificar Actividad','Eliminar Actividad', 'Regresar'])
        print(tmp)
        opt = myInput("Eliga una opción: ")

        if opt == "1":
            clean()
            registrarActividad()
        elif opt == "2":
            clean()
            modificarActividad()
        elif opt == "3":
            clean()
            eliminarActividad()
        elif opt.lower() == "x":
            menu()
        else:
            clean()
            msj("Debes de elegir una opción valida")

def reportes():#Sección C

    def mostrarCiclistas():#Sección C.1
        listadoCiclista()
        msj("Listado de Ciclistas")

    def mostrarActividades():#Sección C.2
        listadoActividades()
        msj("Listado de Actividades")

    def mostrarZodiacoCiclistas():#Sección C.3
        tmp = PrettyTable()
        tmp.field_names = ['Id Ciclista','Ciclista','Signo Zodiacal']
        for c in Ciclista.select():
            x = str(c.fNacimiento).split("-")
            mes = int(x[1])
            dia = int(x[2])

            if mes == 1:
                sz = 'Capricornio' if (dia <= 20) else 'Acuario'
            elif mes == 2:
                sz = 'Acuario' if (dia <= 19) else 'Piscis'
            elif mes == 3:
                sz = 'Piscis' if (dia <= 20) else 'Aries'
            elif mes == 4:
                sz = 'Aries' if (dia <= 20) else 'Tauro'
            elif mes == 5:
                sz = 'Tauro' if (dia <= 20) else 'Géminis'
            elif mes == 6:
                sz = 'Géminis' if (dia <= 21) else 'Cáncer'
            elif mes == 7:
                sz = 'Cáncer' if (dia <= 22) else 'Leo'
            elif mes == 8:
                sz = 'Leo' if (dia <= 22) else 'Virgo'
            elif mes == 9:
                sz = 'Virgo' if (dia <= 22) else 'Libra'
            elif mes == 10:
                sz = 'Libra' if (dia <= 22) else 'Escorpión'
            elif mes == 11:
                sz = 'Escorpión' if (dia <= 22) else 'Sagitario'
            elif mes == 12:
                sz = 'Sagitario' if (dia <= 20) else 'Capricornio'

            tmp.add_row([c.idCiclista,f"{c.nombre} {c.apellido}",sz])
        print(tmp)
        msj("Listado de Ciclista con Signo Zodiacal")

    def exportarHTML():#Sección C.4
        pass

    def mapaActividades():#Sección C.5
        mapa = folium.Map(location=[18.735693, -70.162651], zoom_start=6, titles="Mapa de Actividades")

        for a in Actividades.select():
            folium.Marker(location=[a.lat, a.lng], tooltip="Click para ver más información",
            popup=(f"{a.nomCiclista} {a.apellCiclista}")).add_to(mapa)

        mapa.save("MapaActividadesCiclista.html")
        webbrowser.open("MapaActividadesCiclista.html")

    while True:
        clean()
        tmp = PrettyTable()
        column_names = ['Sección C','Reportes']
        tmp.add_column(column_names[0], ['1','2','3','4','5','X'])
        tmp.add_column(column_names[1], ['Listado de Ciclistas','Listado de Actividades','Listado de Ciclistas con Signo Zodiacal', 'Exportar Ciclista (No Funcional)', 'Mapa de actividades','Regresar'])
        print(tmp)
        opt = myInput("Eliga una opción: ")

        if opt == "1":
            clean()
            mostrarCiclistas()
        elif opt == "2":
            clean()
            mostrarActividades()
        elif opt == "3":
            clean()
            mostrarZodiacoCiclistas()
        elif opt == "4":
            clean()
            exportarHTML()
        elif opt == "5":
            clean()
            mapaActividades()
        elif opt.lower() == "x":
            menu()
        else:
            clean()
            msj("Debes de elegir una opción valida")

def acercaDe():#Sección D
    clean()
    tmp = PrettyTable()
    column_names = ['Sección D','Acerca De']
    tmp.add_column(column_names[0], ["Asignatura:","Estudiante:","Matrícula:","YouTube:"])
    tmp.add_column(column_names[1], ["Fundamentos de Programación","Francisco Javier Medina Matos","2020-9273","https://www.youtube.com/watch?v=bDyisqgIFG0"])
    print(tmp)
    webbrowser.open("https://www.youtube.com/watch?v=bDyisqgIFG0")

def menu():#Menu Principal
    while True:
        clean()
        tmp = PrettyTable()
        column_names = ['Sección','Menu']
        tmp.add_column(column_names[0], ['A','B','C','D','X'])
        tmp.add_column(column_names[1], ['Gestionar Ciclistas','Gestionar Actividades','Reportes','Acerca de','Salir'])
        print(tmp)
        opt = myInput("Eliga una opción: ")

        if opt.lower() == "a":
            clean()
            gestionarCiclistas()
        elif opt.lower() == "b":
            clean()
            gestionarActividades()
        elif opt.lower() == "c":
            clean()
            reportes()
        elif opt.lower() == "d":
            clean()
            acercaDe()
        elif opt.lower() == "x":
            clean()
            sys.exit()
        else:
            clean()
            msj("Debes de elegir una opción valida")
menu()