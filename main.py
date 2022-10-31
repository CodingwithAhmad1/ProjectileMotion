# this program is great for working out projectile motion questions
# suvat x terms or suvat →
from dataclasses import dataclass
import math
from pickle import NONE
import numpy as np 

print("Answer below question in lower case")
question = input("Is it launched a 'Suvat' question, or a projectile question from 'ground' level, a 'height' with angle or a 'drop': ")


test1 = "g"
test2 = "h"
test3 = "s"
test4 = "dr"
test_incline = "ye"
test_incline_1 = "no"
g = 9.81
A_x = 0
V_y = 0




    
    



if test1 in question:
        
    Original_velocity = int(input("Enter original velocity as an integer value: "))
    Angle = int(input("Enter the angle as an integer: "))
    Incline = input("Is there an incline('yes' or 'no'): ")
    if  test_incline in Incline:
        incline_1 = input("Enter incline(degrees) as an integer: ")   
    else:
        print(" ")

        U_y_val = round((Original_velocity * math.sin(math.radians(Angle))), 3)
        U_y = (Original_velocity * math.sin(math.radians(Angle)))
    
        U_x_val= round(Original_velocity * math.cos(math.radians(Angle)), 3)
        U_x = Original_velocity * math.cos(math.radians(Angle))
        V_x = U_x_val
    
   
        T_half_val = round(((Original_velocity*math.sin(math.radians(Angle)))/g), 3)
        T_half = ((Original_velocity*math.sin(math.radians(Angle)))/g)
        H_max = round(((Original_velocity)*(math.sin(math.radians(Angle)))*T_half) - ((0.5)*(g)*(T_half**2)), 3)
    
        T_max_val = round((2*(T_half)), 3)
        T_max = (2*(T_half))
        S_x = round((U_x * T_max), 3)

    
        print("Time values are in seconds, distances are in meters. ")
        print(" ")
        @dataclass
        class SUVAT_x_variables:
            __slots__ = ["Sx","Ux", "Vx", "Ax", "Tx"]
            Sx: float
            Ux: float
            Vx: float
            Ax: float
            Tx: float
       
        Data_motion_x = SUVAT_x_variables(S_x , U_x_val, V_x, A_x, T_half_val)
        print(f"These are the {Data_motion_x}. ")
        print(" ")
    
        @dataclass
        class SUVAT_y_variables:
            __slots__ = ["Sy","Uy", "Vy", "Ay", "Ty"]
            Sy: float
            Uy: float
            Vy: float
            Ay: float
            Ty: float
        Data_motion_y = SUVAT_y_variables(H_max, U_y_val, V_y, g, T_half_val)
        print(f"These are the  {Data_motion_y}. ")
        print(" ")
    
        @dataclass
        class Key_values:
            __slots__ = ["Total_time","Max_height", "Horizontal_distance"]
            Total_time: float
            Max_height: float
            Horizontal_distance: float
        Data_motion = Key_values(T_max_val, H_max, S_x)
        print(f"These are all the {Data_motion}. ")     
        print(" ")
elif test2 in question:  # height
        Original_velocity = int(input("Enter original velocity as an integer value: "))
        Angle = int(input("Enter the angle as an integer: "))
        Height = int(input("Enter original height: "))
        Incline = input("Is there an incline('yes' or 'no'): ")
        if Incline == "yes":
            print("testing")
        else:

            U_y_val = round((Original_velocity * math.sin(math.radians(Angle))), 3)
            U_y = (Original_velocity * math.sin(math.radians(Angle)))
    
            U_x_val= round(Original_velocity * math.cos(math.radians(Angle)), 3)
            U_x = Original_velocity * math.cos(math.radians(Angle))
            V_x = U_x_val
    
   
            T_half_val = round(((Original_velocity*math.sin(math.radians(Angle)))/g), 3)
            T_half = ((Original_velocity*math.sin(math.radians(Angle)))/g) + (0.5*(Height/g))
            H_max = round(((Original_velocity)*(math.sin(math.radians(Angle)))*T_half) - ((0.5)*(g)*(T_half**2)), 3)
    
            T_max_val = round((2*(T_half)), 3)
            T_max = (2*(T_half)) 
            S_x = round(((U_x * T_max) + ((U_x) * (10/g))) , 3)
    
    
            print("Time values are in seconds, distances are in meters. ")
            print(" ")
            @dataclass
            class SUVAT_x_variables:
                __slots__ = ["Sx","Ux", "Vx", "Ax", "Tx"]
                Sx: float
                Ux: float
                Vx: float
                Ax: float
                Tx: float
       
            Data_motion_x = SUVAT_x_variables(S_x , U_x_val, V_x, A_x, T_half_val)
            print(f"These are the {Data_motion_x}. ")
            print(" ")
    
            @dataclass
            class SUVAT_y_variables:
                __slots__ = ["Sy","Uy", "Vy", "Ay", "Ty"]
                Sy: float
                Uy: float
                Vy: float
                Ay: float
                Ty: float
            Data_motion_y = SUVAT_y_variables(H_max, U_y_val, V_y, g, T_half_val)
            print(f"These are the  {Data_motion_y}. ")
            print(" ")
    
            @dataclass
            class Key_values:
                __slots__ = ["Total_time","Max_height", "Horizontal_distance"]
                Total_time: float
                Max_height: float
                Horizontal_distance: float
            Data_motion = Key_values(T_max_val, H_max, S_x)
            print(f"These are all the {Data_motion}. ")     
            print(" ")
    
elif test3 in question:  #SUVAT
    SUVAT = input("Enter any suvat letters(lower case only) that you have the value of: ")
    if "s" in SUVAT:
        s = 'defined'
        s_val = int(input("What is the value for s: "))
    else:
        s = 'undefined'
        
    if "u" in SUVAT:
        u = 'defined'
        u_val = int(input("What is the value for u: "))
    else:
        u = 'undefined'
        
    if "v" in SUVAT:
        v = 'defined'
        v_val = int(input("What is the value for v: "))
    else:
        v = 'undefined'
        
    if "a" in SUVAT:
        a = 'defined'
        a_val = int(input("What is the value for a: "))
    else:
        a = 'undefined'
        
    if "t" in SUVAT:
        t = 'defined'
        t_val = int(input("What is the value for t: "))
    else:
        t = 'undefined'
    
        
elif test4 in question:   # drop
    print("ok")
else:
    print("undefined")
        
