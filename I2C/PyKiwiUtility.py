import os.path
from pywinio import WinIO
from ctypes import cdll,c_uint,c_int,c_ubyte,c_bool,byref,sizeof


class PyKiwi:
    def __init__(self):
    #    app_path = os.path.dirname(os.path.abspath(__file__))
    #    self.mydll = cdll.LoadLibrary(app_path+"\\KiwiDll\\Kiwi.dll")
    #    app_path = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + dll_name

        dll_name = 'Kiwi.dll'       
        self.mydll = cdll.LoadLibrary(dll_name)
        
    def GetGpioConfig(self,mGPIO):

        Reresult = ( c_uint)()
        self.mydll.GetGpioConfig.restype = c_bool
        Status = self.mydll.GetGpioConfig(mGPIO,byref(Reresult))

        return Status,Reresult.value
    
    def GetGpioMode(self,mGPIO):

        Reresult = ( c_uint)()
        self.mydll.GetGpioMode.restype = c_bool
        Status = self.mydll.GetGpioMode(mGPIO,byref(Reresult))

        return Status,Reresult.value    

    def SetGpioMode(self,mGPIO,mDirection):
       
        self.mydll.SetGpioMode.restype = c_bool
        Status = self.mydll.SetGpioMode(mGPIO,mDirection)

        return Status            
    
    def GetGpioStatus(self,mGPIO):

        Reresult = ( c_uint)()
        self.mydll.GetGpioStatus.restype = c_bool
        Status = self.mydll.GetGpioStatus(mGPIO,byref(Reresult))

        return Status,Reresult  

    def SetGpioStatus(self,mGPIO,mLevle):

        self.mydll.SetGpioStatus.restype = c_bool
        Status = self.mydll.SetGpioStatus(mGPIO,mLevle)

        return Status       
#====================== Not test ===========================================
    def GetPwmConfig(self,mPWM):
        
        Reresult = ( c_uint)()
        self.mydll.GetPwmConfig.restype = c_bool
        Status = self.mydll.GetPwmConfig(mPWM,byref(Reresult))

        return Status,Reresult.value
    
    def SetPwmStatus(self,mPWM,mEnable):

        self.mydll.SetPwmStatus.restype = c_bool
        Status = self.mydll.SetPwmStatus(mPWM,mEnable)

        return Status  

    def SetPwmFrequency(self,mPWM,mFrequency):

        self.mydll.SetPwmFrequency.restype = c_bool
        Status = self.mydll.SetPwmFrequency(mPWM,mFrequency)

        return Status                

    def SetPwmDutyCycle(self,mPWM,mDutyCycle):

        self.mydll.SetPwmDutyCycle.restype = c_bool
        Status = self.mydll.SetPwmDutyCycle(mPWM,mDutyCycle)

        return Status          

    def GetPwmStatus(self,mPWM):
        
        Reresult = ( c_uint)()
        self.mydll.GetPwmStatus.restype = c_bool
        Status = self.mydll.GetPwmStatus(mPWM,byref(Reresult))


    def GetPwmFrequency(self,mPWM):
        
        Reresult = ( c_uint*4)()
        self.mydll.GetPwmFrequency.restype = c_bool
        Status = self.mydll.GetPwmFrequency(mPWM,byref(Reresult))

        return Status,Reresult.value

    def GetPwmDutyCycle(self,mPWM):
          
        Reresult = ( c_uint*4)()
        self.mydll.GetPwmDutyCycle.restype = c_bool
        Status = self.mydll.GetPwmDutyCycle(mPWM,byref(Reresult))

        return Status,Reresult.value    

    def GetI2cConfig(self):
          
        Reresult_Enable = ( c_uint)()
        Reresult_Speed = ( c_uint)()
        Reresult_Rs = ( c_uint)()
        self.mydll.GetI2cConfig.restype = c_bool
        Status = self.mydll.GetI2cConfig(byref(Reresult_Enable,byref(Reresult_Speed),byref(Reresult_Rs)))

        return Status, Reresult_Enable.value, Reresult_Speed.value, Reresult_Rs.value 

    def SetI2cConfig(self,mEnable,mSpeed,mRs):          

        self.mydll.SetI2cConfig.restype = c_bool
        Status = self.mydll.SetI2cConfig(mEnable,mSpeed,mRs)

        return Status

    def GetSPIConfig(self):
          
        Reresult_Enable = ( c_uint)()
        Reresult_Mode = ( c_uint)()
        Reresult_DataOrder = ( c_uint)()
        Reresult_Speed = ( c_uint)()
        self.mydll.GetSPIConfig.restype = c_bool
        Status = self.mydll.GetSPIConfig(byref(Reresult_Enable),byref(Reresult_Mode),byref(Reresult_DataOrder),byref(Reresult_Speed))

        return Status, Reresult_Enable.value, Reresult_Mode.value, Reresult_DataOrder.value, Reresult_Speed.value  

    def SetSPIConfig(self,mEnable,mMode,mDataOreder,mSpeed):          

        self.mydll.SetSPIConfig.restype = c_bool
        Status = self.mydll.SetSPIConfig(mEnable,mMode,mDataOreder,mSpeed)

        return Status

    def AccessI2c(self,mAddress,mWData,mRSize):          

        rData = ( c_ubyte*mRSize)()
        
        wData = (c_ubyte * len(mWData))(*mWData)
        mWSize = len(mWData)   

        self.mydll.AccessI2c.restype = c_bool
        Status = self.mydll.AccessI2c(mAddress,mWSize,byref(wData),mRSize,byref(rData))       
        
        return Status,rData        

