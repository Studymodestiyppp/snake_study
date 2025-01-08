from servo_driver import ServoDriver
import time
import math
import numpy as np
import threading
import socket

SNAKE_LENGTH = 12###蛇身长度
key = 0###接收客户端键盘信息

class Process(object):
    def __init__(self):
##############################################################
#初始化参数与步态参数（这里只有蠕动）       
##############################################################
        self.servo = ServoDriver()   ### 创建舵机类的对象，才能调用舵机控制代码
        self.enable(1)    ###使能舵机
        self.servo_list = []   ## 舵机id列表
        self.t = 0    # 全局变量，步态时间函数
##############################################################

##############################################################
#舵机函数
##############################################################
    def list_servo(self): 
        for i in range(SNAKE_LENGTH):
            n = self.servo.id_read(i)       
            if n is not None:
                self.servo_list.append(n)
            print(self.servo_list)

    def enable(self, value=1):   ### 舵机上电
        for i in range(SNAKE_LENGTH):
            self.servo.load_or_unload_write(i, value)

    def disable(self, value=0):  #
        for i in range(SNAKE_LENGTH):  # 遍历12个舵机
            self.servo.load_or_unload_write(i, value)  # 0 掉电，1装电，恒为0
##############################################################

##############################################################
#通讯函数
##############################################################
    def start_server(self, host='192.168.60.207', port=8887):
        global key
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen()
            print(f"Server listening on {host}:{port}")
            while True:
                conn, addr = s.accept()
                with conn:
                    print(f"Connected by {addr}")
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        command = data.decode()
                        key=command
                        print(f"K{key}")
                        print(f"Received command: {command}")
##############################################################
#步态函数fuwei(self)、rudong(self)、zuozhuan(self)、youzhuan(self)
##############################################################
    def fuwei(self):       ##复位
        for i in range(0, 12, 1):
            print(i)
            self.servo.move_time_write(i,400,1000)
            if i==1 or i==3:
                self.servo.move_time_write(i,410,1000)
            if i==9 or i==11:
                self.servo.move_time_write(i, 370, 1000)    
        time.sleep(2)
        print("复位")  
        
    def rudong(self):
        global key

        while key=='W'or key=='w': 

            for i in range(0, SNAKE_LENGTH, 2):
                if i==0:
                    s = 150 * (math.sin( math.pi* self.t/25 + math.pi * i /4)) + 400+50
                    self.servo.move_time_write(i, 800-int(s), 4)
                    print (i,800-int(s),self.t)
                    time.sleep(0.004)         
                if i==2:
                    s =  150 * (math.sin( math.pi* self.t/25 + math.pi * i /4)) + 400
                    self.servo.move_time_write(i, 800-int(s), 4)
                    print (i,int(s),self.t)
                    time.sleep(0.004)
                if i==4 :
                    s =  150* (math.sin( math.pi* self.t/25 + math.pi * i /4)) + 400
                    self.servo.move_time_write(i, 800-int(s), 4)
                    print (i,int(s),self.t)
                    time.sleep(0.004)   
                if i==4 or i==6 or i==8:
                    s =  150* (math.sin( math.pi* self.t/25 + math.pi * i /4)) + 400
                    self.servo.move_time_write(i, 800-int(s), 4)
                    print (i,int(s),self.t)
                    time.sleep(0.004)
                if i==10:
                    s = 150 * (math.sin( math.pi* self.t/25 + math.pi * i /4)) + 400-80
                    self.servo.move_time_write(i, 800-int(s), 4)
                    print (i,int(s),self.t)
                    time.sleep(0.004)


            self.t=self.t+1   
            
    def zuozhuan(self):
        global key
        if key=='A'or key=='a':
            self.servo.move_time_write(1,470,20)

            self.servo.move_time_write(5,460,20)

            self.servo.move_time_write(9,430,20)

            self.servo.move_time_write(3,470,20)

            self.servo.move_time_write(7,460,20)

            self.servo.move_time_write(11,430,20)
            time.sleep(0.050) 


        while key=='A'or key=='a': 

            for i in range(0, SNAKE_LENGTH, 2):
                if i==0:
                    s = 150 * (math.sin( math.pi* self.t/25 + math.pi * i /4)) + 400+50
                    self.servo.move_time_write(i, 800-int(s), 4)
                    print (i,800-int(s),self.t)
                    time.sleep(0.004)         
                if i==2:
                    s =  150 * (math.sin( math.pi* self.t/25 + math.pi * i /4)) + 400
                    self.servo.move_time_write(i, 800-int(s), 4)
                    print (i,int(s),self.t)
                    time.sleep(0.004)
                if i==4 :
                    s =  150* (math.sin( math.pi* self.t/25 + math.pi * i /4)) + 400
                    self.servo.move_time_write(i, 800-int(s), 4)
                    print (i,int(s),self.t)
                    time.sleep(0.004)   
                if i==4 or i==6 or i==8:
                    s =  150* (math.sin( math.pi* self.t/25 + math.pi * i /4)) + 400
                    self.servo.move_time_write(i, 800-int(s), 4)
                    print (i,int(s),self.t)
                    time.sleep(0.004)
                if i==10:
                    s = 150 * (math.sin( math.pi* self.t/25 + math.pi * i /4)) + 400-80
                    self.servo.move_time_write(i, 800-int(s), 4)
                    print (i,int(s),self.t)
                    time.sleep(0.004)


            self.t=self.t+1     
            
    def youzhuan(self):
        global key
        if key=='D'or key=='d':
            self.servo.move_time_write(1,350,20)

            self.servo.move_time_write(5,340,20)

            self.servo.move_time_write(9,310,20)

            self.servo.move_time_write(3,350,20)

            self.servo.move_time_write(7,340,20)

            self.servo.move_time_write(11,310,20)
            time.sleep(0.050) 


        while key=='D'or key=='d': 

            for i in range(0, SNAKE_LENGTH, 2):
                if i==0:
                    s = 150 * (math.sin( math.pi* self.t/25 + math.pi * i /4)) + 400+50
                    self.servo.move_time_write(i, 800-int(s), 4)
                    print (i,800-int(s),self.t)
                    time.sleep(0.004)         
                if i==2:
                    s =  150 * (math.sin( math.pi* self.t/25 + math.pi * i /4)) + 400
                    self.servo.move_time_write(i, 800-int(s), 4)
                    print (i,int(s),self.t)
                    time.sleep(0.004)
                if i==4 :
                    s =  150* (math.sin( math.pi* self.t/25 + math.pi * i /4)) + 400
                    self.servo.move_time_write(i, 800-int(s), 4)
                    print (i,int(s),self.t)
                    time.sleep(0.004)   
                if i==4 or i==6 or i==8:
                    s =  150* (math.sin( math.pi* self.t/25 + math.pi * i /4)) + 400
                    self.servo.move_time_write(i, 800-int(s), 4)
                    print (i,int(s),self.t)
                    time.sleep(0.004)
                if i==10:
                    s = 150 * (math.sin( math.pi* self.t/25 + math.pi * i /4)) + 400-80
                    self.servo.move_time_write(i, 800-int(s), 4)
                    print (i,int(s),self.t)
                    time.sleep(0.004)


            self.t=self.t+1
        # 可以在这里添加更多的控制逻辑
##############################################################
#主函数
##############################################################
    def main(self):
        global key
        server_thread = threading.Thread(target=self.start_server)#因为下面有个while循环一直在检测执行什么步态所以接收信息只能另开线程
        server_thread.start()
        while True:
        # 主程序逻辑
            if key=='D'or key=='d':
                self.youzhuan()
            if key=='A'or key=='a':
                self.zuozhuan()
            if key=='W'or key=='w':
                self.rudong()                   
            if key=='B'or key=='b':
                self.fuwei()
##############################################################
#调用类中主函数执行
##############################################################
if __name__ == "__main__":
    demo=Process()
    demo.main()
