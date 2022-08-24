from machine import Pin, ADC, PWM,SPI # Machine kütüphanesinden Pin ve ADC  sınıfını yüklüyoruz.
from time import sleep # Time kütüphanesinden sleep sınıfını yüklüyoruz.
import utime
import time

time.sleep(1.5)


led = Pin(0, Pin.OUT)
ldr_pin = 28 # Ldr'yi GPI26'ya bağlıyoruz.

trig = Pin(9, Pin.OUT)
echo = Pin(8, Pin.IN, Pin.PULL_DOWN)

buzzer = PWM(Pin(2)) # Buzzer'ı GP0'a bağlıyoruz.
buzzer.freq(500) # Buzzer'ın frekans değerini belirliyoruz.

# Birinci dc motoru GP14 ve GP15'e bağlıyoruz.
motor1a = Pin(14, Pin.OUT) 
motor1b = Pin(15, Pin.OUT) 

# Birinci dc motoru GP16 ve GP17'ye bağlıyoruz.
motor2a = Pin(16, Pin.OUT) 
motor2b = Pin(17, Pin.OUT)

# Çizgi izleme
pin1 = Pin(26, Pin.IN)  
pin2 = Pin(27, Pin.IN) 

Speed1 = PWM(Pin(16))
Speed1.freq(50)

Speed2 = PWM(Pin(15))
Speed2.freq(50)

x = 0
started = 0
# Çizgi izleme
def line_track():
    sensor_1 = pin1.value() # Sensör 1'in değeri okunur.
    sensor_2 = pin2.value() # Sensör 2'nin değeri okunur.
    #sleep(1) # 1 saniye bekleme.
    
    # Sesnör 1 ve 2'nin değerleri ekrana yazdırılır.
    print("Sensor1 : ", sensor_1)
    print("Sensor2 : ", sensor_2)
    return sensor_1, sensor_2
  

    
# Buzzer
def check_buzzer(distance):
    
    if (distance < 10):
        buzzer.duty_u16(3000) # Buzzer'ın ses seviyesini belirliyoruz.
        return True
     
    else:
        buzzer.duty_u16(0) # Buzzer'ı susturuyoruz.
        return False
        
    
                
while True:
    
    a, b = line_track()      
    
    motor1a.value(0) # sağ motor
    motor1b.value(1)
    motor2a.value(1) # sol motor
    motor2b.value(0)
    
    if(a==1 and b == 1):
        
        Speed1.duty_u16(int(40/100*65536))
        Speed2.duty_u16(int(40/100*65536))
        
    elif(a==1 and b == 0):
        
        Speed1.duty_u16(int(40/100*65536))
        Speed2.duty_u16(int(0/100*65536))
        x = 1;
            
    elif(a == 0 and b == 1):
        Speed1.duty_u16(int(0/100*65536))
        Speed2.duty_u16(int(40/100*65536))
        x = 2;
            
    elif(a == 0 and b == 0):
        
            Speed1.duty_u16(int(0/100*65536))
            Speed2.duty_u16(int(0/100*65536))
            
            if(x == 1):
                Speed1.duty_u16(int(40/100*65536))
                Speed2.duty_u16(int(0/100*65536))
                
            if(x == 2):
                Speed1.duty_u16(int(0/100*65536))
                Speed2.duty_u16(int(40/100*65536))
        
             
   
























