import pydirectinput
import time

tempo_andando = 1.7
delay_troca = 0

pydirectinput.FAILSAFE = False

print("--- INICIANDO EM 5 SEGUNDOS ---")
print(">> CLIQUE na janela do mGBA agora <<")
time.sleep(5) 
print("Rodando...")

try:
    while True:
        print("Esquerda...")
        pydirectinput.keyDown('left')
        pydirectinput.keyDown('z')
        time.sleep(tempo_andando)
        pydirectinput.keyUp('left')
        
        time.sleep(delay_troca)

        print("Direita...")
        pydirectinput.keyDown('right')
        pydirectinput.keyDown('z')
        time.sleep(tempo_andando)
        pydirectinput.keyUp('right')

        time.sleep(delay_troca)

except KeyboardInterrupt:
    pydirectinput.keyUp('left')
    pydirectinput.keyUp('z')
    pydirectinput.keyUp('right')
    print("\nPrograma encerrado.")