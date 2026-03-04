from pymodbus.client import ModbusTcpClient
import time

client = ModbusTcpClient("127.0.0.1", port=5020)

if not client.connect():
    raise RuntimeError("Connection Failed")

DEVICE_ID = 1   

# read coils
read_co = client.read_coils(0, count=8, device_id=DEVICE_ID)
print("Coils[0..7]", read_co.bits[:8])