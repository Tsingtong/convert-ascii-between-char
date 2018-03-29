# -*- coding: utf-8 -*-
asc_type = 1
char_type = 2

def asc2Char(num_int):
    return chr(num_int)

def dec2Bin(num):
    return bin(num)[2:]

def dec2Hex(num):
    return hex(num)[2:]

def bin2dec(num):
    return int(str(num),2)

def hex2dec(num):
    return int(str(num),16)

if __name__ == "__main__":
    # input
    print("欢迎使用写ASCII码转换程序\n")
    while(True):
        input_type = int(input("输入ASCII求字符请输入1，输入字符求ASCII请输入2！\n\n"))

        if input_type == 1:     # 输入ASCII求字符
            num_str = input("请输入一个字符:\n ")
            print( num_str + " 的十进制ASCII 码为", ord(num_str))
            print( num_str + " 的二进制ASCII 码为", dec2Bin(ord(num_str)))
            print( num_str + " 的十六进制ASCII 码为", dec2Hex(ord(num_str)))
        elif input_type == 2:   # 输入字符求ASCII
            print("请输入你输入ASCII码所使用的进制（2,10,16）")            
            sys_type = int(input("2进制输入1，,10进制输入2,16进制输入3:\n "))
            num_int = input("请输入该进制的ASCII码:\n ")
            if sys_type == 1:       # 2进制输入1
                print( num_int , " 12进制ASCII对应的字符为", chr(bin2dec(int(num_int))))
            elif sys_type == 2:       # 10进制输入2
                print( num_int , " 10进制ASCII对应的字符为", chr(int(num_int)))
            elif sys_type == 3:       # 16进制输入3
                print( num_int , " 16进制ASCII对应的字符为", chr(hex2dec(num_int)))
            else:
                print("input error...")
                continue
        else:
            print("input error,try again...")
            continue
        print("\nNew round...........\n\n\n")
