from LavadoraBase import LavadoraBase
from LavadoraEstandar import LavadoraEstandar
from LavadoraInteligente import LavadoraInteligente


def crear_lavadora(tipo):

    # ======================== VALIDACIONES ==========================
    # Nombre (no vacío)
    while True:
        nombre = (input('Ingrese tu nombre completo: ')).strip()
        if nombre:
            break
        print("❌ El nombre no puede estar vacío.")

    # Kilos
    while True:
        try:
            kilos = int(input("Ingrese los kilos de ropa (5 - 40): "))
            if 5 <= kilos <= 40:
                break
            print("❌ ERROR: Debe ser entre 5 y 40 kilos.")
        except ValueError:
            print("❌ Debes ingresar un número entero.")

    # Tipo de ropa
    while True:
        ropa = input("Ingrese algunos de estos tipos de ropa separados por coma:\nCamisetas\nPantalon\nToallas\nCalzoncillos\nMedias\n").lower().strip()

        if not ropa:
            print("❌ Debes ingresar al menos un tipo de ropa.")
            continue

        lista = [r.strip() for r in ropa.split(",")]

        # VALIDACIÓN: cada prenda debe ser solo texto
        valido = True
        for prenda in lista:
            if not prenda.replace(" ", "").isalpha():   # permite espacios pero no números
                print(f"❌ '{prenda}' no es válido. Solo se permiten nombres de ropa en texto.")
                valido = False
                break

        if valido:
            ropa = lista
            break


    # Tiempo de lavado
    while True:
        try:
            tiempo = int(input("Minutos de lavado (mínimo 5): "))
            if tiempo >= 5:
                break
            print("❌ Debe ser un número mayor a 5.")
        except ValueError:
            print("❌ Ingresa un número entero válido.")

    # Potencia
    while True:
        try:
            potencia = float(input("Potencia en kW (ej: 1.5): "))
            if potencia > 0:
                break
            print("❌ La potencia debe ser positiva.")
        except ValueError:
            print("❌ Ingresa un número decimal válido.")

    # Estrato
    while True:
        try:
            estrato = int(input("Estrato (2, 3, 4, 5): "))
            if estrato in (2, 3, 4, 5):
                break
            print("❌ Estrato inválido. Solo 2, 3, 4 o 5.")
        except ValueError:
            print("❌ Ingresa un número entero.")
    # ===============================================================

    if tipo == 1:
        return LavadoraEstandar(kilos, ropa, tiempo, potencia, estrato, nombre)

    elif tipo == 2:
        # ---- VALIDACIONES ADICIONALES SOLO PARA INTELIGENTE ----
        while True:
            wifi = input("¿La lavadora tiene wifi? (si/no): ").lower()
            if wifi in ("si", "no"):
                break
            print("❌ Respuesta inválida. Escribe 'si' o 'no'.")

        while True:
            sensores = input("¿Tiene sensores inteligentes? (si/no): ").lower()
            if sensores in ("si", "no"):
                sensores = (sensores == "si")
                break
            print("❌ Respuesta inválida. Escribe 'si' o 'no'.")
        # ---------------------------------------------------------

        return LavadoraInteligente(kilos, ropa, tiempo, potencia, estrato, wifi, sensores, nombre)

    else:
        return LavadoraBase(kilos, ropa, tiempo, potencia, estrato, nombre)



def menu_individual(lavadora):
    while True:
        print("\n== MENÚ DE ACCIONES INDIVIDUALES ==")
        print("1. Encender")
        print("2. Llenar")
        print("3. Lavar")
        print("4. Enjuagar")
        print("5. Secar")
        print("6. Reporte completo (ciclo terminado)")
        print("7. Volver al menú principal")

        op = input("Seleccione una opción: ")

        match op:
            case "1":
                lavadora.encender()
            case "2":
                lavadora._llenar()
            case "3":
                lavadora.lavar()   # POLIMORFISMO aquí
            case "4":
                lavadora._enjuagar()
            case "5":
                lavadora._secar()
            case "6":
                lavadora.ciclo_terminado()
            case "7":
                break
            case _:
                print("Opción inválida.")


def main():
    while True:
        print("\n=== SISTEMA DE LAVADORAS ===")
        print("1. Crear lavadora ESTÁNDAR")
        print("2. Crear lavadora INTELIGENTE")
        print("3. Crear lavadora BASE (sin sensores)")
        print("4. Salir")

        opcion = input("Seleccione tipo de lavadora: ")

        if opcion == "1":
            lav = crear_lavadora(1)
            print("\nLavadora ESTÁNDAR creada.")

        elif opcion == "2":
            lav = crear_lavadora(2)
            print("\nLavadora INTELIGENTE creada.")

        elif opcion == "3":
            lav = crear_lavadora(3)
            print("\nLavadora BASE creada.")

        elif opcion == "4":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida.")
            continue

        while True:
            print("\n¿Qué desea hacer?")
            print("1. Ciclo completo")
            print("2. Acciones individuales")
            print("3. Elegir otra lavadora")

            sub = input("Seleccione: ")

            if sub == "1":
                lav.ciclo_terminado()
            elif sub == "2":
                menu_individual(lav)
            elif sub == "3":
                break
            else:
                print("Opción inválida.")


if __name__ == "__main__":
    main()
