from machine import PWM,Pin
import time

class Sdata:
    min_us = 600
    current_us = None
    current_angle = None
    max_us = 2400
    servos = 0
    pins = []
    servo_objs =[]

class Servo:
    def __init__(self):
        self.data = Sdata()
    """"
    def add_servo2(self, pin_number_list:list):
        for pin_number in pin_number_list :
            pwm = PWM(Pin(pin_number))
            pwm.freq(50)
            self.data.servo_objs.append(pwm)
            self.data.pins.append(pin_number)
    """
    def add_servo(self, pin:list):
        for servo in range(len(pin)):
            pwm = PWM(Pin(pin[servo]))
            pwm.freq(50)
            self.data.servo_objs.append(pwm)
            self.data.pins.append(pin[servo])
            self.data.servos += 1
    """
    def write2(self, us_or_degrees_list: list, degrees_true_or_us_false: list):

        for is_degrees, value in zip(degrees_true_or_us_false, us_or_degrees_list) :
            if is_degrees :
                self.data.current_angle = self.data.min_us + (value / 180) * (self.data.max_us - self.data.min_us)
                self.data.servo_objs[i].duty_u16(int(self.data.current_angle * 65535 / 20000))
            else:
                self.data.current_us = us_or_degrees_list[i]
                self.data.servo_objs[i].duty_u16(int(self.data.current_us * 65535 / 20000))
    """
    def write(self,angles:list,micro_us:list):
        for i in range(len(micro_us)):
            if micro_us[i]:
                self.data.current_angle = self.data.min_us + (angles[i] / 180) * (self.data.max_us - self.data.min_us)
                self.data.servo_objs[i].duty_u16(int(self.data.current_angle * 65535 / 20000))
            else:
                self.data.current_us = angles[i]
                self.data.servo_objs[i].duty_u16(int(self.data.current_us * 65535 / 20000))

