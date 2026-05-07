

import json
import os

archivo = "banco_db.json"

def guardar_datos():
    datos_guardar = {
        "id_cuenta": id_cuenta,
        "datos": datos
    }

    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos_guardar, f, indent=4, ensure_ascii=False)


def cargar_datos():
    global id_cuenta, datos

    if not os.path.isfile(archivo):
        return

    with open(archivo, "r", encoding="utf-8") as f:
        datos_guardar = json.load(f)

    id_cuenta = datos_guardar.get("id_cuenta", 1)
    datos = datos_guardar.get("datos", [])









id_cuenta = 1
datos = [{
  "id": 1,
  "nombre": "Hunt",
  "saldo": 1500.0,
  "historial": [
      {"tipo": "deposito", "monto": 500, "fecha": "2026-05-07"},
      {"tipo": "retiro", "monto": 200, "fecha": "2026-05-07"}
  ]
}
]




def ver_cuentas():
    for dato in datos:
        print("---user---")
        print(f"id: {dato['id']}\nNombre: {dato['nombre']}")
        print(f"Saldo: {dato['saldo']}")
        print("---------")
        if not dato['historial']:
            print("No ha habido movimientos")
        else:
            for mov in dato['historial']:
                print(f"tipo: {mov['tipo']}")
                print(f"monto: {mov['monto']}")
                print(f"fecha: {mov['fecha']}")
        print("---------")


def crear_cuenta():
    global id_cuenta
    name = input("Ingrese su nombre: ")
    if not name:
        print("Respuesta invalida")
        return
    saldo = input("Ingrese su saldo: ")
    if not saldo:
        print("respuesta invalida")
        return
    try:
        saldo = float(saldo)
    except ValueError:
        print("respuesta invalida")
        return
    historial_new = []
    id_cuenta += 1
    datos.append({
        "id": id_cuenta,
        "nombre": name,
        "saldo": saldo,
        "historial": historial_new
    })

def depositar_dinero():
    print("Para depositar digame\n(1) El id de la cuenta\n(2)El nombre de quien esta la cuenta")
    option_1 = input("Ingrese la opcion que desea: ")
    if not option_1:
        print("respuesta invalida")
        return
    try:
        option_1 = int(option_1)
        if option_1 < 1 or option_1 > 2:
            print("respuesta invalida")
            return
    except ValueError:
        print("respuesta invalida")
        return
    if option_1 == 1:
        id = input("Ingrese el id de la cuenta: ")
        if not id:
            print("respuesta invalida")
            return
        try:
            id = int(id)
            if id < 1:
                print("respuesta invalida")
                return
        except ValueError:
            print("Respuesta invalida")
            return
        for dato in datos:
            if dato['id'] == id:
                deposito = input("Ingrese la cantidad a ser depositada: ")
                if not deposito:
                    print("Respuesta invalida")
                    return
                try:
                    deposito = float(deposito)
                    if deposito < 0:
                        print("respuesta invalida")
                        return
                except ValueError:
                    print("respuesta invalida")
                    return
                total = dato['saldo'] + deposito
                dato['saldo'] = total
                fecha = input("Ingrese la fecha (dd/mm/aaaa): ")
                if not fecha:
                    print("respuesta invalida")
                    return
                dato['historial'].append({
                    "tipo": "deposito",
                    "monto": deposito,
                    "fecha": fecha
                })



    elif option_1 == 2:
        name_new = input("Ingrese el nombre de la cuenta: ")
        if not name_new:
            print("Respuesta invalida")
            return
        for dato in datos:
            if dato['nombre'] == name_new:
                deposito = input("Ingrese la cantidad a ser depositada: ")
                if not deposito:
                    print("respuesta invalida")
                try:
                    deposito = float(deposito)
                    if deposito < 0:
                        print("respuesta invalida")
                        return
                except ValueError:
                    print("respuesta invalida")
                    return
                total = dato['saldo'] + deposito
                dato['saldo'] = total
                fecha = input("Ingrese la fecha (dd/mm/aaaa): ")
                if not fecha:
                    print("respuesta invalida")
                    return
                dato['historial'].append({
                    "tipo": "deposito",
                     "monto": deposito,
                    "fecha": fecha

                })
            else:
                print("no se encontro la cuenta")
                return


def retirar_dinero():
    global id_cuenta
    cuenta = input("Dame el id de la cuenta de la que quieres retirar dinero: ")
    if not cuenta:
        print("respuesta invalida")
        return
    try:
        cuenta = int(cuenta)
        if cuenta < 1:
            print("respuesta invalida")
            return
    except ValueError:
        print("respuesta invalida")
        return
    for dato in datos:
        if dato['id'] == cuenta:

            retirar = input("Cuanto dinero desea retirar: ")
            dinero = dato['saldo']
            if not retirar:
                print("respuesta invalida")
                return
            try:
                retirar = float(retirar)
                if retirar < 0 or retirar > dinero:
                    print("respuesta invalida")
                    return
            except ValueError:
                print("respuesta invalida")
                return

            dato['saldo'] = dato['saldo'] - retirar
            fecha = input("Ingrese la fecha (dd/mm/aaaa): ")
            if not fecha:
                print("respuesta invalida")
                return
            dato['historial'].append({
                "tipo": "retiro",
                "monto": retirar,
                "fecha": fecha
            })




def transferir_e_cuentas():
    id_1 = input("Ingrese el id de la cuenta que enviará dinero: ")
    if not id_1:
        print("respuesta invalida")
        return

    try:
        id_1 = int(id_1)
    except ValueError:
        print("respuesta invalida")
        return

    id_2 = input("Ingrese el id de la cuenta que recibirá dinero: ")
    if not id_2:
        print("respuesta invalida")
        return

    try:
        id_2 = int(id_2)
    except ValueError:
        print("respuesta invalida")
        return

    cuenta_origen = None
    cuenta_destino = None

    for dato in datos:
        if dato['id'] == id_1:
            cuenta_origen = dato
        if dato['id'] == id_2:
            cuenta_destino = dato

    if cuenta_origen is None:
        print("No se encontró la cuenta origen")
        return

    if cuenta_destino is None:
        print("No se encontró la cuenta destino")
        return

    transferir = input("Cuanto desea transferir: ")
    if not transferir:
        print("respuesta invalida")
        return

    try:
        transferir = float(transferir)
        if transferir <= 0:
            print("respuesta invalida")
            return
    except ValueError:
        print("respuesta invalida")
        return

    if transferir > cuenta_origen['saldo']:
        print("Fondos insuficientes")
        return

    cuenta_origen['saldo'] -= transferir
    cuenta_destino['saldo'] += transferir
    fecha = input("Ingrese la fecha (dd/mm/aaaa): ")
    if not fecha:
        print("respuesta invalida")
        return


    print("Transferencia realizada con éxito")

    cuenta_origen['historial'].append({
        "tipo": "transferencia enviada",
        "monto": transferir,
        "fecha": fecha
    })

    cuenta_destino['historial'].append({
        "tipo": "transferencia recibida",
        "monto": transferir,
        "fecha": fecha
    })



def ver_historial():
    cuenta = input("De que cuenta desea ver su historial (ingrese id): ")
    if not cuenta:
        print("respuesta invalida")
        return
    try:
        cuenta = int(cuenta)
        if cuenta < 1:
            print("respuesta invalida")
            return

    except ValueError:
        print("respuesta invalida")
        return
    for dato in datos:
        if dato['id'] == cuenta:
            for mov in dato['historial']:
                print(f"tipo: {mov['tipo']}")
                print(f"monto: {mov['monto']}")
                print(f"fecha: {mov['fecha']}")
                print("---------")

            return

    print("No se encontró la cuenta")
    return




def eliminar_cuenta():
    global id_cuenta
    cuenta = input("Dame el id de la cuenta que desea eliminar: ")
    if not cuenta:
        print("Respuesta invalida")
        return
    try:
        cuenta = int(cuenta)
        if cuenta < 1:
            print("respuesta invalida")
            return
    except ValueError:
        print("Respuesta invalida")
        return
    for user in datos:
        if user['id'] == cuenta:
            datos.remove(user)
            print("respuesta eliminada")
            return


    print("No se encontró la cuenta")


def salir():
    print("Gracias por usar el programa")


cargar_datos()
while True:
    print("---Programa bancario---")
    print("1. Ver cuentas")
    print("2 Crear cuenta")
    print("3. Depositar diner")
    print("4. Retirar dinero")
    print("5. Transferir dinero entre cuentas")
    print("6. Ver historial de una cuenta")
    print("7. Eliminar una cuenta")
    print("8. Salir")
    option_main = input("Que opcion elige?: ")
    if not option_main:
        print("respuesta invalida")
        continue
    try:
        option_main = int(option_main)
        if option_main < 1 or option_main > 7:
            print("Respuesta invalida")
            continue
    except ValueError:
        print("respuesta invalida")
        continue

    if option_main == 1:
        ver_cuentas()
        guardar_datos()
    elif option_main == 2:
        crear_cuenta()
        guardar_datos()
    elif option_main == 3:
        depositar_dinero()
        guardar_datos()
    elif option_main == 4:
        retirar_dinero()
        guardar_datos()
    elif option_main == 5:
        transferir_e_cuentas()
        guardar_datos()
    elif option_main == 6:
        ver_historial()
        guardar_datos()
    elif option_main == 7:
        eliminar_cuenta()
        guardar_datos()
    elif option_main == 8:
        salir()
        guardar_datos()
        break
