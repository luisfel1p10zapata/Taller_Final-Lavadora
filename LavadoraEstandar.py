from LavadoraBase import LavadoraBase
import pygame
import time

class LavadoraEstandar(LavadoraBase):

    def __init__(self, kilos, tipo_ropa, tiempo_lavado, potencia_kw, estrato,nombre):
        super().__init__(kilos, tipo_ropa, tiempo_lavado, potencia_kw, estrato,nombre)

    # ====== POLIMORFISMO ======
    def lavar(self):
        if not self._validar_kilos():
            print("❌ ERROR: La lavadora solo permite entre 5 y 40 kilos.")
            return
        
        print("\n🌀 Lavando en modo ESTÁNDAR …")
        
        pygame.mixer.music.load("lavar.mp3")  # puedes usar el mismo lavar.mp3 si no tienes este
        pygame.mixer.music.play()

        pygame.time.delay(5000)
        pygame.mixer.music.stop()
        time.sleep(5)

        print("✔ Lavado estándar completado.")
