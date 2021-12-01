cliente=[]

def inicio():
    menu="\na_registrar cliente \n"
    menu+="b_actualizar \n"
    menu+="c_ver datos \n"
    menu+="elija una obción: "
    pregunta=input(menu)
    if(pregunta=='a'):
        registrarcliente()

    elif (pregunta=='b'):
        actualizardatos(descuento=0)

    elif (pregunta=='c'):
        verdatos()

def registrarcliente():
    lista=[]
    documento=int(input("\ningrese el docuemento: "))
    validar(documento)
    nombre=input("ingrese su nombre: ")
    telefono=input("ingre su telefono: ")
    saldo=int(input("ingre el saldo: "))
    lista.extend([documento,nombre,telefono,saldo])
    cliente.append(lista)
    inicio()

def actualizardatos(descuento):
    print()
    actualizar=int(input("ingrese el documento de la persona que desea actualizar: "))
    for i in range(len(cliente)):
        c=(cliente[i])
        resultado=actualizar in c

        if (resultado==True):
            print ()
            menu2="1_actualizar nombre\n2_actualizar saldo\n3_actualizar telefono\nque desea hacer: "
            i='si'
            while (i == 'si'):
                adatos=int(input(menu2))
                if(adatos==1):
                    d=(c[1])
                    c.remove(d)
                    nuevo=input("\ningrese el nuevo nombre: ")
                    c.insert(1,nuevo)
                elif (adatos==2):
                    d=(c[3])
                    saldo(d,descuento)
                    c.remove(d)
                    nuevo=descuento
                    c.insert(3,nuevo)
                elif (adatos==3):
                    d=(c[2])
                    c.remove(d)
                    nuevo=input("ingrese el nuevo numero: ")
                    c.insert(2,nuevo)

                i=input("\ningrese si para actualizar otro dato de lo contrario ingrese no: ")
            break
        elif (resultado==False):
            print()   
    inicio()

def verdatos():
    menu3="\n1_ver todos los datos\n2_buscar cliente\nque desea hacer: "
    prg=int(input(menu3))
    if (prg==1):
        datost()
    elif (prg==2):
        vercliente()

def saldo(d,descuento):
    print("el cliente debe",d)
    pago=int(input("ingrese el valor que el cliente desea pagar: "))
    descuento=d-pago
    print("el total es de",descuento)
    return descuento

def validar(documento):
    validar=documento
    for i in range(len(cliente)):
        valida=(cliente[i])
        resultado=validar in valida
        if (resultado==True):
            print("el documento no se puede ingresar ya se encuentra registrado un cliente")
            inicio()
    return

def datost():
    tam=len(cliente)
    for i in range (tam):
        print ("\n",cliente[i])
    inicio()

def vercliente():
    documento=int(input("ingrese el documento de la persona que desea ver: " ))
    for i in range(len(cliente)):
        valida=(cliente[i])
        resultado=documento in valida
        if (resultado==True):
            print()
            print(valida)        
    inicio()
            

inicio=inicio()



