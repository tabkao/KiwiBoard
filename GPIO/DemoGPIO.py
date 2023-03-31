from time import sleep
from PyKiwiUtility import PyKiwi

Output=0
Input =1
High  =1
Low   =0

##############MCU:13pin
GP0 = 0
GP1 = 1
GP4 = 4
GP5 = 5
GP6 = 6
GP16 = 16
GP17 = 17
GP22 = 22
GP23 = 23
GP24 = 24
GP25 = 25
GP26 = 26
GP27 = 27
##############SIO :2pin
GP14 = 14
GP15 = 15
##############SIO
##############PCH :4pin
GP18 = 18
GP19 = 19
GP20 = 20
GP21 = 21
##############PCH


GPIO_OUTPUT_Dict = [GP22,GP23,GP24]
LED_GPIO = {"GREEN":GP22,"YELLOW":GP23,"RED":GP24}
mykiwi = PyKiwi()

def Init_GPIO():
    for gpio in GPIO_OUTPUT_Dict:
        mykiwi.SetGpioMode(gpio,Output)
        mykiwi.SetGpioStatus(gpio,Low)  

def LedControl(mled_On):
    for gpio in GPIO_OUTPUT_Dict:         
        if LED_GPIO[mled_On] == gpio:                          
            mykiwi.SetGpioStatus(gpio,High)        
        else:
            mykiwi.SetGpioStatus(gpio,Low)         

def main():

    Init_GPIO()
    
    while True:
        print('Please input 1: Green. 2:Yellow. 3:Red. other: exit')
        input_a = input()
        if input_a == '1':
            print('GREEN light up!')
            LedControl('GREEN')
        elif input_a == '2':
            print('YELLOW light up!')
            LedControl('YELLOW')
        elif input_a == '3':
            print('RED light up!')
            LedControl('RED')
        else:
            print('Good Bye!')
            break


if __name__ == "__main__":
    
    main()