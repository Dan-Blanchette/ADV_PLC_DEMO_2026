from pymodbus.server import StartTcpServer
from pymodbus import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusServerContext, ModbusDeviceContext

def run_server():
    # number of register to populate
    num_reg = 200
    # initializate the datastore
    device = ModbusDeviceContext(
        di = ModbusSequentialDataBlock(0, [0,1]*(num_reg//2)),
        co = ModbusSequentialDataBlock(0, [1]*num_reg),
        hr = ModbusSequentialDataBlock(0, [17]*num_reg),
        ir = ModbusSequentialDataBlock(0, [18]*num_reg)
    )

    context = ModbusServerContext(devices=device, single=True)

    identity = ModbusDeviceIdentification()
    identity.VendorName = "Not Allen Bradley"
    identity.ProductCode = "ABS" # A boring simulator
    identity.ProductName = "PyModbus Sim"
    identity.ModelName = "Model_1"

    StartTcpServer(context=context, 
                   identity=identity, 
                   address = ("127.0.0.1", 5020)
                   )
    
def main():
    print("Modbus Server Started at localhost on port 5020")
    run_server()

if __name__ == "__main__":
    main()