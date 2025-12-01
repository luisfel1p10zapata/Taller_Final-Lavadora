from LavadoraBase import LavadoraBase
import time
import pygame

class LavadoraInteligente(LavadoraBase):

    def __init__(self, kilos, tipo_ropa, tiempo_lavado, potencia_kw, estrato, wifi, sensores,nombre):
        super().__init__(kilos, tipo_ropa, tiempo_lavado, potencia_kw, estrato,nombre)
        self._wifi = wifi
        self._sensores = sensores

    # Metodos nuevos

    def detectar_tipo_ropa(self):
        print("\nDetectando tipo de ropa con sensores...")
        time.sleep(2)

        if "pantalones" in self._tipo_ropa or "toallas" in self._tipo_ropa:
            print("➡ Ropa pesada detectada. Ajustando duración y energía...")
            self._tiempo_lavado += 5
        else:
            print("➡ Ropa liviana detectada. Optimización aplicada.")

    def conectar_wifi(self):
        if self._wifi =='si':
            print("\n📡 Conectando a la red WiFi...")
            time.sleep(1)
            print("✔ Reporte enviado al celular del usuario.")
        else:
            print("❌ No hay WiFi disponible para enviar reportes.")

    # Polimorfismo

    def lavar(self):
        print("\n🤖 Lavado INTELIGENTE optimizado con sensores...")
        pygame.mixer.music.load("lavar.mp3")
        pygame.mixer.music.play()
        pygame.time.delay(5000)
        pygame.mixer.music.stop()
        time.sleep(5)
