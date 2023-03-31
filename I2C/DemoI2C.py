from time import sleep
from PyKiwiUtility import PyKiwi
from PyKiwiSHT21 import SHT21

def main():
    mykiwi = PyKiwi()   
    mySHT21 = SHT21(mykiwi)

    while True:
        print('Please input 1: Get Temperature. other: exit')
        input_a = input()        
        if input_a =='1':
            temperature =round( mySHT21.read_temperature() , 1 )
            print('The temperature is %d degrees'%temperature)
            pass
        else:
            break


if __name__ == "__main__":
    
    main()