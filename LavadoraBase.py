import time
import pygame

class LavadoraBase:

    def __init__(self, kilos:int, tipo_ropa:str, tiempo_lavado:int, potencia_kw:float, estrato:int,nombre:str):
        self._nombre = nombre
        self._kilos = kilos
        self._tipo_ropa = tipo_ropa              # lista
        self.__estado = "apagada"                # atributo privado
        self._tiempo_lavado = tiempo_lavado      # minutos
        self._precio_kilo = 10000                # $10.000 por kilo
        self._aumento_especial = 0.05            # 5%
        self._iva = 0.19                         # 19%
        self._potencia_kw = potencia_kw          # kW
        self._estrato = estrato                  # 2,3,4,5

        # Inicializar pygame una sola vez
        pygame.mixer.init()

    # Metodos publicos

    def encender(self):
        if not self._validar_kilos():
            print("❌ ERROR: La lavadora solo permite entre 5 y 40 kilos.")
            return
        self.__estado = "encendida"
        pygame.mixer.music.load("encender.mp3")
        pygame.mixer.music.play()
        print("La lavadora está encendida.")
        time.sleep(1)
        
    def nombre(self) -> str:
        return self._nombre
        
    def ciclo_terminado(self):
        if not self._validar_kilos():
            print("❌ ERROR: La lavadora solo permite entre 5 y 40 kilos.")
            return
        
        self.encender()
        print("\n🔵 Iniciando ciclo de lavado...")

        self._llenar()
        self.lavar()            
        self._enjuagar()
        
        respuesta = input("\n¿Desea secar la ropa? (Si/No): ").strip().lower()
        if respuesta =='si':
            self._secar()

        costos = self.__calcular_costos()
        energia = self.__calcular_consumo_energia()

        self._mostrar_reporte_cliente(costos, energia)
        print("\n✔ El ciclo ha terminado correctamente.\n")

    # Metodos Protegidos

    def _validar_kilos(self):
        return 5 <= self._kilos <= 40

    def _llenar(self):
        if not self._validar_kilos():
            print("❌ ERROR: La lavadora solo permite entre 5 y 40 kilos.")
            return
        print("\n⏳ Llenando el tanque")
        pygame.mixer.music.load("llenar.mp3")
        pygame.mixer.music.play()
        pygame.time.delay(5000)   # reproce 
        pygame.mixer.music.stop() # Detiene el audio
        time.sleep(5)
    
        print("✔ Tanque lleno.")

    def lavar(self):
        if not self._validar_kilos():
            print("❌ ERROR: La lavadora solo permite entre 5 y 40 kilos.")
            return
        print("\n🌀 Lavando...")
        pygame.mixer.music.load("lavar.mp3")
        pygame.mixer.music.play()
        pygame.time.delay(5000)   # reproce 
        pygame.mixer.music.stop() # Detiene el audio
        time.sleep(5)

    def _enjuagar(self):
        if not self._validar_kilos():
            print("❌ ERROR: La lavadora solo permite entre 5 y 40 kilos.")
            return
        print("\n💠 Enjuagando...")
        pygame.mixer.music.load("enjuagar.mp3")
        pygame.mixer.music.play()
        pygame.time.delay(5000)   # reproce 
        pygame.mixer.music.stop() # Detiene el audio
        time.sleep(5)

    def _secar(self):
        if not self._validar_kilos():
            print("❌ ERROR: La lavadora solo permite entre 5 y 40 kilos.")
            return
        print("\n🔅 Secando...")
        pygame.mixer.music.load("Secar.mp3")
        pygame.mixer.music.play()
        pygame.time.delay(5000)   # reproce 
        pygame.mixer.music.stop() # Detiene el audio
        time.sleep(5)

    def _mostrar_reporte_cliente(self, costos, energia):
        print("\n <====== REPORTE DEL CLIENTE ======> ")
        print(f'Nombre:{self._nombre}')
        print(f"Kilos: {self._kilos}")
        print(f"Tipo de ropa: {self._tipo_ropa}")
        print(f"Costo total con IVA: ${costos['costo_final']:,}")
        print(f"Consumo energía (kWh): {energia['kwh']:.2f}")
        print(f"Costo energía: ${energia['costo_energia']:,}")
        print(f"Utilidad del empresario: ${costos['utilidad']:,}")
        print('Gracias por usar Lava Smart')

    # Metodos Privados

    def __calcular_costos(self):
        costo_base = self._kilos * self._precio_kilo
        prendas_especiales = {"interior", "pijamas", "vestidos"}
        costo_aumentado = costo_base

        if any(t in prendas_especiales for t in self._tipo_ropa):
            costo_aumentado *= 1 + self._aumento_especial

        costo_final = costo_aumentado * (1 + self._iva)
        utilidad = costo_aumentado * 0.30

        return {
            "costo_base": costo_base,
            "costo_aumentado": costo_aumentado,
            "costo_final": int(costo_final),
            "utilidad": int(utilidad)
        }

    def __calcular_consumo_energia(self):
        kwh = self._potencia_kw * (self._tiempo_lavado / 60)

        tarifa = {
            2: 867.8,
            3: 737.6,
            4: 867.8,
            5: 1041
        }.get(self._estrato, 867.8)

        costo_energia = kwh * tarifa

        return {
            "kwh": kwh,
            "costo_energia": int(costo_energia)
        }
