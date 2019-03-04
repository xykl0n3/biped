import dxl2
import time
from dxl2 import register
from read import read_file




conn = dxl2.Connection("/dev/ttyUSB0")
conn.open_port()


###### uncomment to check present position ########
# for i in range (1,11):
#         m = dxl2.Motor(conn, i, dxl2.MotorType.AX)
#         print(m.read(register.Instruction.PRESENT_POSITION))        


####### gait ######




def do(function):
        

        pos = read_file(function)
        for list in pos:
                for i in range (1,11):
                        m = dxl2.Motor(conn, i, dxl2.MotorType.AX)

                        ####### change moving speed #######
                        m.write(register.Instruction.MOVING_SPEED,40)
                        
                        m.write(register.Instruction.GOAL_POSITION, list[i-1])



###### to read present position ######

def read():     
        for i in range (1,11):
                m = dxl2.Motor(conn, i, dxl2.MotorType.AX)
                print(m.read(register.Instruction.PRESENT_POSITION))
        

