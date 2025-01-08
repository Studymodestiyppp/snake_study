# snake_study
1.运动学
matlab_simulation运行结果

![image](https://github.com/user-attachments/assets/b98af6c9-def2-444d-8267-3ecdb19cba53)

可与看出，蠕动步态每个关节虽然幅度不同但相位差都为T/4个周期  
蠕动代码
![image](https://github.com/user-attachments/assets/57774a68-9f27-4cc2-9e13-fc40725db4fa)
s=150 *(math.sin( math.pi*self.t/25 + math.pi *i /4))+ 400+50  
就是sin函数跟仿真图对应  
150是震幅(上下震动幅度)想改幅度就改这个值  
math.pi*self.t/25 中math.pi/25 控制震动频率  
2.通讯  
  基于TCP通讯  
自己去看python教程  


3.多线程  
  多任务同时进行的意义  
  看Snake_Control和Snake_Clinet代码注释
