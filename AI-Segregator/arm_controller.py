import serial.tools.list_ports

class arm_control:

    def __init__(self):
        self.ports = serial.tools.list_ports.comports()
        self.serialInst = serial.Serial()     
        self.serialInst.baudrate = 9600
        self.serialInst.port = 'COM5'
        self.serialInst.open()

    def move_to_shoot_position(self ):
        self.serialInst.write("shoot".encode('utf-8'))
   
    def pick_object(self ):
        self.serialInst.write("pick".encode('utf-8'))

    def drop_object(self, color ):
        self.serialInst.write(color.encode('utf-8'))

    def move_to_rest_position(self ):
        self.serialInst.write("rest".encode('utf-8'))

    def test(self ):
        self.serialInst.write("test".encode('utf-8'))

    
