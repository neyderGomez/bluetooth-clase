# main.py -- put your code here!#comunicacion bluetooth
from machine import Pin
from time import sleep
from BLE import BLEUART #bluetooth low energy (celulares, audifonos, parlantes, moviles)
import bluetooth
#bluetooth clasic consume mucho, ahora se usa BLE --> propio para el esp32

nombre ="ESP32Neyder"
ble=bluetooth.BLE()
usart=BLEUART(ble,nombre)

def transmito():
    buffer=usart.read().decode().strip()
    print(buffer)
    usart.write("la entrega Bluetooth es para dentro de 8 dias")

usart.irq(handler=transmito)
#verificar que este prendido el bluetooth del pc