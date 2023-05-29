# this program is great for working out projectile motion questions - from ground or height
# doesn't take into account air resistance
from dataclasses import dataclass
import math
import pandas as pd

print("Answer the below question in lower case ")
question = input("Is it launched  from 'ground' level, or from a 'height': ")


test1 = "g"
test2 = "h"
g = 9.81
A_x = 0
V_y = 0


if test1 in question:

    Original_velocity = int(
        input("Enter original velocity as an integer value: "))
    Angle = int(input("Enter the angle as an integer: "))
    print(" ") # backslash not avaliable on keyboard

    U_y_val = round((Original_velocity * math.sin(math.radians(Angle))), 3)
    U_y = (Original_velocity * math.sin(math.radians(Angle)))

    U_x_val = round(Original_velocity * math.cos(math.radians(Angle)), 3)
    U_x = Original_velocity * math.cos(math.radians(Angle))
    V_x = U_x_val

    T_half_val = round(
        ((Original_velocity*math.sin(math.radians(Angle)))/g), 3)
    T_half = ((Original_velocity*math.sin(math.radians(Angle)))/g)
    H_max = round(((Original_velocity)*(math.sin(math.radians(Angle)))
                  * T_half) - ((0.5)*(g)*(T_half**2)), 3)

    T_max_val = round((2*(T_half)), 3)
    T_max = (2*(T_half))
    S_x = round((U_x * T_max), 3)

    Data_motion = {
        "Suvat X": [S_x, U_x_val, V_x, A_x, T_half_val],
        "Suvat Y": [H_max, U_y_val, V_y, g, T_half_val]

    }

    Labels = ["S", "U", "V", "A", "T"]

    Data = pd.DataFrame(Data_motion, index=Labels)
    print(Data)

    print(" ")

    Data_motion_1 = {
        "Total time": [T_max_val],
        "Max height": [H_max],
        "Distance": [S_x]

    }

    Labels_1 = [" "]

    Data_key = pd.DataFrame(Data_motion_1, index=Labels_1)
    print(Data_key)

    print(" ")
elif test2 in question:  # height - projectile question

    Angle = int(input("Enter the angle as an integer: "))
    Height = int(input("Enter original height: "))
    print(" ")

    Original_velocity = int(
        input("Enter original velocity as an integer value: "))
    U_y_val = round((Original_velocity * math.sin(math.radians(Angle))), 3)
    U_y = (Original_velocity * math.sin(math.radians(Angle)))

    U_x_val = round(Original_velocity * math.cos(math.radians(Angle)), 3)
    U_x = Original_velocity * math.cos(math.radians(Angle))

    V_x = U_x_val
    T_half = ((Original_velocity*math.sin(math.radians(Angle)))/g)
    H_max_val = round(((Original_velocity)*(math.sin(math.radians(Angle)))
                      * T_half) - ((0.5)*(g)*(T_half**2)), 3)
    H_max = ((Original_velocity)*(math.sin(math.radians(Angle)))
             * T_half) - ((0.5)*(g)*(T_half**2))
    T_remaining = H_max/g
    T_max_val = round(T_half + T_remaining, 3)
    T_max = T_half + T_remaining

    S_x = round((U_x * T_max), 3)

    print("Time values are in seconds, distances are in meters. ")
    print(" ")

    @dataclass
    class SUVAT_x_variables:
        __slots__ = ["Sx", "Ux", "Vx", "Ax"]
        Sx: float
        Ux: float
        Vx: float
        Ax: float

    Data_motion_x = SUVAT_x_variables(S_x, U_x_val, V_x, A_x)
    print(f"These are the {Data_motion_x}. ")

    @dataclass
    class SUVAT_y_variables:
        __slots__ = ["Sy", "Uy", "Vy", "Ay"]
        Sy: float
        Uy: float
        Vy: float
        Ay: float
    Data_motion_y = SUVAT_y_variables(H_max_val, U_y_val, V_y, g)
    print(f"These are the  {Data_motion_y}. ")
    print(" ")

    @dataclass
    class Key_values:
        __slots__ = ["Total_time", "Max_height", "Horizontal_distance"]
        Total_time: float
        Max_height: float
        Horizontal_distance: float
    Data_motion = Key_values(T_max_val, H_max, S_x)
    print(f"These are all the {Data_motion}. ")
    print(" ")
