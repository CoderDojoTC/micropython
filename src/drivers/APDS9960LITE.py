"""`APDS9960LITE`
====================================================

Low memory Driver class for the APDS9960 

    Author: Rune Langøy  2019
 
    Licence GNU General Public License v3.0
    https://www.gnu.org/licenses/gpl-3.0.html
"""
from time import sleep
from micropython import const
#APDS9960_ADDR        = const(0x39)

class I2CEX:
    """micropython i2c adds functions for reading / writing byte to a register 

    :param i2c: The I2C driver
    :type i2C: machine.i2c
    """

    def __init__(self,
                 i2c, 
                 address):
        self.__i2c=i2c
        self.__address=address
        
    def __regWriteBit(self,reg,bitPos,bitVal):
        """Reads a I2C register byte changes a bit and writes the new value

            :param reg: The I2C register that is writen to
            :type reg: int

            :param bitPos: The bit position (0 - 7)
            :type bitPos: int        
            
            :param value: True = set-bit / False =clear bit
            :type value: bool        
        """
        val=self.__readByte(reg)   # read reg 
        if bitVal == True:
            val=val | (1<<bitPos)  # set bit
        else:
            val=val & ~(1<<bitPos) # clear bit
        
        self.__writeByte(reg,val) #write reg
  
    
    def __writeByte(self,reg,val):
        """Writes a I2C byte to the address APDS9960_ADDR (0x39)

            :param reg: The I2C register that is writen to
            :type reg: int
            :param val: The I2C value to write in the range (0- 255)
            :type val: int        
        """
        self.__i2c.writeto_mem(self.__address,reg,bytes((val,)))

    def __readByte(self,reg):
        """Reads a I2C byte from the address APDS9960_ADDR (0x39)

        :param reg: The I2C register to read
        :type reg: int

        :returns: a value in the range (0- 255)
        :rtype: int      
        """

        val =self.__i2c.readfrom_mem(self.__address,reg, 1)
        return int.from_bytes(val, 'big', True)

    def __write2Byte(self,reg,val):
        """Writes a I2C byte to the address APDS9960_ADDR (0x39)

            :param reg: The I2C register that is writen to
            :type reg: int
            :param val: The I2C value to write in the range (0- 255)
            :type val: int        
        """
        b = bytearray(2)
        b[0]=val & 0xff
        b[1]=(val>>8) & 0xff
        self.__i2c.writeto_mem(self.__address,reg,b)

    def __read2Byte(self,reg):
        """Reads a I2C byte from the address APDS9960_ADDR (0x39)

        :param reg: The I2C register to read
        :type reg: int

        :returns: a value in the range (0- 65535)
        :rtype: int      
        """
        val =self.__i2c.readfrom_mem(self.__address,reg, 2)
        return int.from_bytes(val, 'little', True)
   
  
    
class ALS(I2CEX):
    """APDS9960 Digital Ambient Light Sense (ALS) and Color Sense (RGBC) functionalities 
    
    :param i2c: The I2C driver
    :type i2C: machine.i2c
    """    
    def __init__(self,
                 i2c):
        super().__init__(i2c,0x39) # initiate I2CEX with APDS9960_ADDR

    def enableSensor(self,on=True):
        """Enable/Disable the Light sensor

        :param on: Enables / Disables the Light sensor
                (Default True)
        :type on: bool
        """
        AEN=1  #ALS enable bit 1 (AEN) in reg APDS9960_REG_ENABLE
        super().__regWriteBit(reg=0x80,bitPos=AEN,bitVal=on)

    @property
    def eLightGain(self):
        """Sets the receiver gain for light measurements.

        :getter: Returns the reciever gain (0 -3)
        :setter: Sets the reciever gain (0 -3)
        :type: int

        ::

            eGain    Gain
              0       1x
              1       2x
              2       16x
              3       64x
        """
        #APDS9960_REG_CONTROL = const(0x8f)
        val=super().__readByte(0x8f)
        val= val  & 0b00000011 
        return val

    @eLightGain.setter
    def eLightGain(self, eGain):
        #APDS9960_REG_CONTROL = const(0x8f)
        val=super().__readByte(0x8f)
        # set bits in register to given value
        eGain &= 0b00000011
        val &= 0b11111100
        val |= eGain

        super().__writeByte(0x8f,val)


    @property
    def ambientLightLevel(self):
        """Reads the APDS9960 ambient light level (apds9960 clear channel data)

            :getter: Returns the ambient light level (0 - 1025 ) 
            :type: int     
        """
        return super().__read2Byte(0x94) #returns CDATAL and CDATAH

    @property
    def redLightLevel(self):
        """Reads the APDS9960 red light level (apds9960 red channel data)

            :getter: Returns the red light level (0 - 1025 ) 
            :type: int     
        """ 
        return super().__read2Byte(0x96) #returns RDATAL and RDATAH
    
    @property
    def greenLightLevel(self):
        """Reads the APDS9960 green light level (apds9960 green channel data)

            :getter: Returns the green light level (0 - 1025 ) 
            :type: int     
        """       
        return super().__read2Byte(0x98) #returns GDATAL and GDATAH
    
    @property
    def blueLightLevel(self):
        """Reads the APDS9960 blue light level (apds9960 blue channel data)

            :getter: Returns the blue light level (0 - 1025 ) 
            :type: int     
        """       
        return super().__read2Byte(0x9A) #returns BDATAL and BDATAH

    def setInterruptThreshold(self,high=0,low=20,persistance=4):
        """Enable/Disable the proimity sensor

        :param high: high level for generating light hardware interrupt (Range 0 - 1025)
        :type high: int 

        :param low: low level for generating light hardware interrupt (Range 0 - 1025)
        :type low: int 

        :param persistance: Number of consecutive reads before IRQ is raised (Range 0 - 7)
        :type persistance: int 

        """
        #ALS low threshold, lower byte
        super().__write2Byte(0x84, low);  #set ALS low threshold
        super().__write2Byte(0x86, high); #set ALS low threshold 
 
 
        if (persistance>7) :
            persistance=7

        val=super().__readByte(0x8C) #APDS9960_PERS 0x8C<3:0>  Proximity Interrupt Persistence 
        val=val & 0b11111000          # Clear APERS
        val=val | persistance         # Set   APERS
        super().__writeByte(0x8C,val) # Update APDS9960_PERS

    def clearInterrupt(self):
        """Crears the proimity interrupt
        IRQ HW output goes low (enables triggering of new IRQ)
        """
        super().__readByte(0xe6)    #All Non-Gesture Interrupt Clear

    def enableInterrupt(self,on=True):
        """Enables/Disables IRQ dependent on limits given by setLightInterruptThreshold()

        :param on: Enable / Disable Hardware IRQ  
        :type on: bool 
        """
        #ENABLE<AIEN> 0x80<4> ALS Interrupt Enable
        AIEN=4    #ALS Interrupt Enable bit 4 (AIEN) in reg APDS9960_REG_ENABLE
        super().__regWriteBit(reg=0x80,bitPos=AIEN,bitVal=on)
        self.clearInterrupt(); 


class PROX(I2CEX):
    """APDS9960 proximity functons

    :param i2c: The I2C driver
    :type i2C: machine.i2c
    """    
    def __init__(self,
                 i2c):
        super().__init__(i2c,0x39) # initiate I2CEX with APDS9960_ADDR
        
    def enableSensor(self,on=True):
        """Enable/Disable the proimity sensor

        :param on: Enables / Disables the proximity sensor
                (Default True)
        :type on: bool
        """
         # PEN - bit 2
        PEN=2  #Proximity enable bit 2 (PEN) in reg APDS9960_REG_ENABLE
        super().__regWriteBit(reg=0x80,bitPos=PEN,bitVal=on)

    def setInterruptThreshold(self,high=0,low=20,persistance=4):
        """Enable/Disable the proimity sensor

        :param high: high level for generating proximity hardware interrupt (Range 0 - 255)
        :type high: int 

        :param low: low level for generating proximity hardware interrupt (Range 0 - 255)
        :type low: int 

        :param persistance: Number of consecutive reads before IRQ is raised (Range 0 - 7)
        :type persistance: int 

        """   
        super().__writeByte(0x89, low);   #set low proximity threshold APDS9960_PILT
        super().__writeByte(0x8B, high);  #set high proximity threshold APDS9960_PIHT
        
        if (persistance>7) :
            persistance=7

        val=super().__readByte(0x8C) #APDS9960_PERS 0x8C<7:4>  Proximity Interrupt Persistence 
        val=val & 0b00011111          # Clear PERS
        val=val | (persistance << 4)  # Set   PERS
        super().__writeByte(0x8C,val) # Update APDS9960_PERS
        
    def clearInterrupt(self):
        """Crears the proimity interrupt
        IRQ HW output goes low (enables triggering of new IRQ)
        """
        super().__writeByte(0xE7,0) #  APDS9960_AICLEAR clear all interrupts
        super().__readByte(0xE5)#(APDS9960_PICLEAR)
     
    def enableInterrupt(self,on=True):
        """Enables/Disables IRQ dependent on limits given by setProximityInterruptThreshold()

        :param on: Enable / Disable Hardware IRQ  
        :type on: bool 
        """
        PIEN=5    #Proximity interrupt enable bit 5 (PIEN) in reg APDS9960_REG_ENABLE
        super().__regWriteBit(reg=0x80,bitPos=PIEN,bitVal=on)
        self.clearInterrupt(); 

    @property
    def eProximityGain(self):
        """Sets the receiver gain for proximity detection.

        :getter: Returns the reciever gain (0 -3)
        :setter: Sets the reciever gain (0 -3)
        :type: int

            ::

                eGain    Gain
                  0       1x
                  1       2x
                  2       4x
                  3       8x
        """
        #APDS9960_REG_CONTROL = const(0x8f)
        val=super().__readByte(0x8f)
        val=((val >>2) & 0b00000011) 
        return val
 
    @eProximityGain.setter
    def eProximityGain(self, eGain):
        #APDS9960_REG_CONTROL = const(0x8f)
        val=super().__readByte(0x8f)
        # set bits in register to given value
        eGain &= 0b00000011
        eGain = eGain << 2
        val &= 0b11110011
        val |= eGain

        #i2c.writeto_mem(APDS9960_ADDR,APDS9960_REG_CONTROL,bytes((val,)))
        super().__writeByte(0x8f,val)

    @property
    def eLEDCurrent(self):
        """
        Sets LED current for proximity and ALS.

        :getter: Returns the LED current (0 -3)
        :setter: Sets the LED current(0 -3)
        :type: int

            ::

              eCurent  LED Current
                0        100 mA
                1         50 mA
                2         25 mA
                3         12.5 mA
        """
        #APDS9960_REG_CONTROL = const(0x8f)
        val=super().__readByte(0x8f)
        val=val >>6
        return val
  
       
    @eLEDCurrent.setter
    def eLEDCurrent(self, eCurent):
        #APDS9960_REG_CONTROL = const(0x8f)
        val=super().__readByte(0x8f)        
        
        # set bits in register to given value
        eCurent &= 0b00000011
        eCurent = eCurent << 6
        val &= 0b00111111
        val |= eCurent

        super().__writeByte(0x8f,val)

    @property
    def proximityLevel(self):
        """Reads the APDS9960 proximity level

            :getter: Returns the proximity level (0 - 255 ) 
            :type: int     
        """        
        return super().__readByte(0x9c)
    

class APDS9960LITE(I2CEX) :
    """APDS9960LITE low memory driver for ASDS9960  

    :param i2c: The I2C driver
    :type i2C: machine.i2c
    
    :example:
      .. code:: python

        import machine 
        from uPy_APDS9960.APDS9960LITE import APDS9960LITE
        
        i2c =  machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))  # Creates I2C Driver on Pin 5 / 6
        adps9960=APDS9960LITE(i2c)                                  # Create APDS9960 Driver
    """
    def __init__(self,
                i2c):      
        """Construct the APDS9960 driver class 

        :param i2c: The I2C driver
        :type i2C: machine.i2c
        """
        super().__init__(i2c,0x39) # initiate I2CEX with APDS9960_ADDR

        self.powerOn(False) # APDS9960_ENABLE PON=0
        sleep(.05)
        self.powerOn(True) # APDS9960_ENABLE PON=1
        self.prox=PROX(i2c)
        self.als=ALS(i2c)
        
    prox = None
    """Prvides APDS9960 Proximity functions.See class: :class:`.PROX`  

    :type PROX: 

    :example:
      .. code:: python

        apds9960=APDS9960LITE(i2c)         # Enable sensor
        apds9960.prox.enableProximity()    # Enable Proximit sensing

    """
    als = None
    """Prvides APDS9960 Light sensor functions.See class: :class:`.ALS`  

    :type PROX: 
    """
    def powerOn(self,on=True):
        """Enable/Disable the apds9960 sensor

        :param on: Enables / Disables the proximity sensor
                (Default True)
        :type on: bool
        """

        PON=0
        super().__regWriteBit(reg=0x80,bitPos=PON,bitVal=on)


    @property
    def statusRegister(self):
            """
            Status Register (0x93)
            The read-only Status Register provides the status of the device. The register is set to 0x04 at power-up.
            Returns the device status.

            :getter: Status register content byte 
  
                ====== ===== =============================
                Field  Bits  Description
                ====== ===== =============================
                CPSAT     7  Clear Photodiode Saturation. 
                PGSAT     6  Analog saturation event.
                PINT      5  Proximity Interrupt. 
                AINT      4  ALS Interrupt. 
                DNC       3  Do not care.
                GINT      2  Gesture Interrupt. 
                PVALID    1  Proximity Valid. 
                AVALID    0  ALS Valid. 
                ====== ===== =============================
 
            :rtype: int      
            """
            return super().__readByte(0x93)