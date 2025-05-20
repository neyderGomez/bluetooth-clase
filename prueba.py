# import asyncio
# from bleak import BleakScanner

# #para escanear dispositvos
# async def main():
#     print("Escaneando dispositivos BLE...")
#     devices = await BleakScanner.discover()
#     for d in devices:
#         print(d)

# asyncio.run(main())

#A0:B7:65:DC:C9:56: ESP32Neyder
import asyncio
from bleak import BleakClient
import tkinter as tk

#crear la ventana principal
ventana= tk.Tk()
ventana.title("widget button en tkinter")
ventana.geometry("400x200")
boton= tk.Button(ventana, text="haz clic aqui")
boton.pack()

#inciar el bucle principal
ventana.mainloop()
# Reemplaza con la dirección BLE de tu ESP32 (la que viste con el escaneo)
ESP32_ADDRESS = "A0:B7:65:DC:C9:56"

# UUIDs del servicio UART BLE (Nordic UART Service)
UART_SERVICE_UUID = "6e400001-b5a3-f393-e0a9-e50e24dcca9e"
UART_RX_CHAR_UUID = "6e400002-b5a3-f393-e0a9-e50e24dcca9e"  # PC -> ESP32
UART_TX_CHAR_UUID = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"  # ESP32 -> PC (notificaciones)

# Callback para manejar datos entrantes
def handle_rx(_, data):
    print(f"[ESP32 ➡️ PC] {data.decode().strip()}")

async def main():
    async with BleakClient(ESP32_ADDRESS) as client:
        print(f"Conectado: {client.is_connected}")

        # Activar notificaciones (TX)
        await client.start_notify(UART_TX_CHAR_UUID, handle_rx)
        print("Esperando mensajes desde el ESP32...")

        # Enviar datos al ESP32 (RX)
        await client.write_gatt_char(UART_RX_CHAR_UUID, b"Hola desde PC!\n")
        print("[PC ➡️ ESP32] Hola desde PC!")

        # Mantener la conexión abierta para recibir mensajes
        await asyncio.sleep(20)

        await client.stop_notify(UART_TX_CHAR_UUID)
        print("Desconectado")

asyncio.run(main())

#descargar python 3.13.3
#instalar extension : python debugger y python
#se corre con el "run python file" esta en la flecha superior derecha o escribir en la terminal de powershell: py prueba.py
#se escibre en la terminal: py -m pip install bleak