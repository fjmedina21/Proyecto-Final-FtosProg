import os, requests
from datetime import date
from peewee import *

db = SqliteDatabase("proyectoFinal.db")

class Ciclista(Model):
    idCiclista = AutoField(primary_key=True)
    cedula = CharField(max_length=11,unique=True)
    nombre = CharField(max_length=30)
    apellido = CharField(max_length=30)
    fNacimiento = DateField()
    tSangre = CharField(max_length=15)
    sizeBici = CharField(max_length=3)
    sizeUniforme = CharField(max_length=3)
    tel = CharField(max_length=15)
    cel = CharField(max_length=15)
    email = CharField(max_length=50,unique=True)
    direccion = TextField()
    persContacto = CharField(max_length=50)
    telContacto = CharField(max_length=15)

    class Meta:
        database = db

class Actividades(Model):
    idActividad = AutoField(primary_key=True)
    nomCiclista = CharField(max_length=30)
    apellCiclista = CharField(max_length=30)
    fecha = DateField()
    distancia = CharField(max_length=25)
    lugar = TextField()
    lat = CharField(max_length=25)
    lng = CharField(max_length=25)
    dificultad = CharField(max_length=10)

    class Meta:
        database = db

db.connect()
db.create_tables([Ciclista, Actividades])

def clean():
    os.system("cls")

def myInput(txt, valor=False):
    entry = input(txt)
    if len(entry)<1:
        if valor == False:
            print("\nDebes ingresar un valor")
            entry = myInput(txt)
        else:
            entry = valor
    return entry

def msj(str):
    print(f"\n{str}")
    input("Pulse 'Enter' para continuar")

hoy = date.today()
def validarFechaNacimiento(entrada):#Validación para la fecha de nacimiento
    cont=0
    for guion in entrada:
        if (guion == "-"):
            cont += 1

    if cont == 2:
        x = entrada.split("-")
        anio = (x[0])
        mes = (x[1])
        dia = (x[2])

        if (anio.isdigit()) and ((int(anio) in range(1910,hoy.year))):
            if (mes.isdigit()) and ((int(mes) in range(1,13))):
                if (dia.isdigit()) and (int(dia) in range(1,32)):
                    edad = hoy.year - int(anio)
                    edad -= ((hoy.month, hoy.day) < (int(mes), int(dia)))
                    if edad in range(15,81):
                        return True
                    else:
                        print(f"\n--Debes tener entre 15 y 80 años para poder registrarse--")
                else:
                    if (dia.isalpha()):
                        print("\n--El Día no puede ser una letra--")
                    else:
                        print("\n--Ingrese un día válido--")
            else:
                if (mes.isalpha()):
                    print("""\n--Aunque el mes puede ser ingresado en forma de texto,
                    aqui debe ser de forma numerica desde el 1 hasta el 12, intente otra vez--""")
                else:
                    print("\n--Ingrese un mes válido--")
        else:
            if (anio.isalnum()):
                if (anio.isalpha()):
                    print("\n--El Año no puede estar compuesto por letras--")
                elif (anio.isdigit()):
                    if int(anio) >= hoy.year:
                        print(f"\n--Estas seguro que naciste en el año {anio}, intenta otra vez--")
                    elif int(anio) < 1910:
                        print("\n--No es posible registrarse--")
                else:
                    print("\n--El Año no puede ser Alfanumerico--")
    else:
        print("\n--Formato Invalido--")

def validarFecha(entrada):#Validación para la fecha
    cont=0
    for guion in entrada:
        if (guion == "-"):
            cont += 1

    if cont == 2:
        x = entrada.split("-")
        anio = (x[0])
        mes = (x[1])
        dia = (x[2])

        if (anio.isdigit()) and ((int(anio) in range((hoy.year),2100))):
            if (mes.isdigit()) and ((int(mes) in range(1,13))):
                if (dia.isdigit()) and (int(dia) in range(1,32)):
                    return True
                else:
                    if (dia.isalpha()):
                        print("\n--El Día no puede ser una letra--")
                    else:
                        print("\n--Ingrese un día válido--")
            else:
                if (mes.isalpha()):
                    print("""\n--Aunque el mes puede ser ingresado en forma de texto, a
                    qui debe ser de forma numerica desde el 1 hasta el 12, intente otra vez--""")
                else:
                    print("\n--Ingrese un mes válido--")
        else:
            if (anio.isalnum()):
                if (anio.isalpha()):
                    print("\n--El Año no puede estar compuesto por letras--")
                elif (anio.isdigit()):
                    if int(anio) < hoy.year:
                        print("\n--No puedes ingresa una actividad con un año menor al actual--")
                else:
                    print("\n--El Año no puede ser Alfanumerico--")
    else:
        print("\n--Formato Invalido--")

def validarCedula(entrada):#Validación de cédula
    if (entrada.isdigit()) and len(entrada) == 11:
        url = 'https://api.adamix.net/apec/cedula/'+entrada
        datos = requests.get(url).json()
        if datos["ok"]:
            return True
        else:
            print("\nCédula not found on the API")
    elif (entrada.isalnum()) and (len(entrada) == 11):
        print("\nCédula can't be alphanumeric")
    elif (len(entrada) != 11):
        if len(entrada) == 0:
            print("\nCédula required")
        elif (entrada.isdigit()):
            print("\nCédula must have eleven digits")
        else:
            print("\nInvalid value")

def validarTelCel(entrada):#Validación de Tel/Cel
    cont=0
    for guion in entrada:
        if (guion == "-"):
            cont += 1

    if cont == 0:
        if (entrada.isdigit()) and len(entrada) == 10:
            return True
        elif (entrada.isalnum()) and (len(entrada) == 10):
            print("\nTel/Cel can't be alphanumeric")
        elif (len(entrada) != 10):
            if len(entrada) == 0:
                print("\nValue required")
            elif (entrada.isdigit()):
                print("Tel/Cel must have ten digits")
            else:
                print("\nIvalid value")
    else:
        print("\nIngrese el numero sin guiones")

def idActividadDisp(entrada):#Validación para los id de actividades exitentes
        listaIdA = []
        for x in Actividades:#Arreglo para validar si el Id esta disponible
            listaIdA.append(x.idActividad)
        count = 0
        for i in listaIdA:
            if entrada == i:
                count += 1
        if count == 0:
            return True
        else:
            return False

def idCiclistaDisp(entrada):#Validación para los id de ciclista exitentes
        listaIdC = []
        for x in Ciclista:#Arreglo para validar si Id esta disponible
            listaIdC.append(x.idCiclista)
        count = 0
        for i in listaIdC:
            if entrada == i:
                count += 1
        if count == 0:
            return True
        else:
            return False

def cedExist(entrada):#Validación para las cédulas existentes
        listaCed = []
        for x in Ciclista:#Arreglo para validar si la cedula ya esta registrada
            listaCed.append(x.cedula)
        count = 0
        for cedula in listaCed:
            if entrada == cedula:
                count += 1
        if count != 0:
            return True
        else:
            return False

def emailExist(entrada):#Validación paro los email existentes
    listaemail = []
    for x in Ciclista:#Arreglo para validar si la cedula ya esta registrada
        listaemail.append(x.email)
    count = 0
    for email in listaemail:
        if entrada == email:
            count += 1
    if count != 0:
        return True
    else:
        return False