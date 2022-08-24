from machine import Pin, ADC, PWM,SPI # Machine kütüphanesinden Pin ve ADC  sınıfını yüklüyoruz.
from time import sleep # Time kütüphanesinden sleep sınıfını yüklüyoruz.
import utime
import time


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


# Çizgi izleme
def line_track():
    sensor_1 = pin1.value() # Sensör 1'in değeri okunur.
    sensor_2 = pin2.value() # Sensör 2'nin değeri okunur.
    #sleep(1) # 1 saniye bekleme.
    
    # Sesnör 1 ve 2'nin değerleri ekrana yazdırılır.
    print("Sensor1 : ", sensor_1)
    print("Sensor2 : ", sensor_2)
    return sensor_1, sensor_2
  


def distance():
    
    trig.value(0)
    time.sleep(0.1)
    trig.value(1)
    time.sleep_us(2)
    trig.value(0)
    while echo.value()==0:
        pulse_start = time.ticks_us()
    while echo.value()==1:
        pulse_end = time.ticks_us()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17165 / 1000000
    distance = round(distance, 0)
    print ('Distance:',"{:.0f}".format(distance),'cm')
    return distance


def forward1(speed):
    
    Speed = PWM(Pin(16))
    Speed.freq(50)
    Speed.duty_u16(int(speed/100*65536))

    motor1a.high()
    motor1b.low()
    
   
def forward2(speed):
    
    Speed = PWM(Pin(14))
    Speed.freq(50)
    Speed.duty_u16(int(speed/100*65536))
    
    motor2a.high()
    motor2b.low()
    

def backward1(speed):
    
    Speed = PWM(Pin(16))
    Speed.freq(50)
    Speed.duty_u16(int(speed/100*65536))

    motor1a.low()
    motor1b.high()
    
    
def backward2(speed):
    
    Speed = PWM(Pin(14))
    Speed.freq(50)
    Speed.duty_u16(int(speed/100*65536))

    motor2a.low()
    motor2b.high()
    
    
# Buzzer
def check_buzzer(distance):
    
    if (distance < 10):
        buzzer.duty_u16(3000) # Buzzer'ın ses seviyesini belirliyoruz.
        return True
     
    else:
        buzzer.duty_u16(0) # Buzzer'ı susturuyoruz.
        return False
        
    
                
while True:
    readLight(ldr_pin)
    a, b = line_track()      
    dist = distance()
    
    if ( a== 0 and b == 0):
        
        forward1(0)
        forward2(0)
        
        
    elif (a == 1 and b == 1):
     
        forward1(70)
        forward2(70)
        
            
    elif ( a == 1 and b == 0 ):
        
        forward2(0)
        forward1(70)
        
    elif ( a == 0 and b == 1 ):
        
        forward2(70)
        forward1(0)
        
          
    if (check_buzzer(dist) is True):
        
            forward1(0)
            forward2(0)
            sleep(2)
            backward1(15)
            backward2(15)
             
   








