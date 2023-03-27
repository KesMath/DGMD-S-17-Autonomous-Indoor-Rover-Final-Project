# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pigpio

WORKING_FREQUENCY = 1000
Forward_multiplier = 1.2
Turn_multiplier = 1.2


class MotorController:
    def __init__(self):
        self.controller = pigpio.pi()
        #put terminals here
        self.lastPWM1 = 0
        self.lastPWM2 = 0
        self.speed_table = [()] * 80
        self.fill_speed_tables()
        #insert access to pi's GPIO in self controller writes
        self.controller.write()
        self.controller.write()
        self.controller.write()
        self.controller.write()
        #replace 0 entry of hardware_PWM to pins being utilized.
        self.controller.hardware_PWM(13, WORKING_FREQUENCY, 0)
        self.controller.hardware_PWM(12, WORKING_FREQUENCY, 0)

    def forward(self):
        if(not self.moving_forward):
            # insert access to pi's GPIO in self controller writes
            self.controller.write()
            self.controller.write()
            self.controller.write()
            self.controller.write()
            # replace 0 entry of hardware_PWM to pins being utilized.
            self.controller.hardware_PWM(13, WORKING_FREQUENCY, 300000*Forward_multiplier)
            self.controller.hardware_PWM(12, WORKING_FREQUENCY, 300000*Forward_multiplier)
            self.lastPWM1 = 300000*Forward_multiplier
            self.lastPWM2 = 300000*Forward_multiplier
        self.moving_forward = True

    def backward(self):
        self.moving_forward = False
        # insert access to pi's GPIO in self controller writes
        self.controller.write()
        self.controller.write()
        self.controller.write()
        self.controller.write()
        # replace 0 entry of hardware_PWM to pins being utilized.
        self.controller.hardware_PWM(13, WORKING_FREQUENCY, 300000 * Forward_multiplier)
        self.controller.hardware_PWM(12, WORKING_FREQUENCY, 300000 * Forward_multiplier)
        self.lastPWM1 = 0
        self.lastPWM2 = 0

    def stop(self):
        self.moving_forward = False
        if(self.lastPWM1 == 0 and self.lastPWM2 == 0):
            return
            # insert access to pi's GPIO in self controller writes
        self.controller.write()
        self.controller.write()
        self.controller.write()
        self.controller.write()
        # replace 0 entry of hardware_PWM to pins being utilized.
        self.controller.hardware_PWM(13, WORKING_FREQUENCY, 0)
        self.controller.hardware_PWM(12, WORKING_FREQUENCY, 0)
        self.lastPWM1 = 0
        self.lastPWM2 = 0

    def turn_left(self, index = None):
        self.moving_forward = False
        # insert access to pi's GPIO in self controller writes
        self.controller.write()
        self.controller.write()
        self.controller.write()
        self.controller.write()
        if not index:
            current_PWM1, current_PWM2 = 600000*Turn_multiplier, 780000*Turn_multiplier
        else:
            current_PWM2, current_PWM1 = self.fill_speed_tables[index]
        if(self.lastPWM1 == current_PWM1 and self.lastPWM2 == current_PWM2):
            return
        self.controller.hardware_PWM(13, WORKING_FREQUENCY, current_PWM1)
        self.controller.hardware_PWM(12, WORKING_FREQUENCY, current_PWM2)
        self.lastPWM1 = current_PWM1
        self.lastPWM2 = current_PWM2

    def turn_right(self, index = None):
        self.moving_forward = False
        # insert access to pi's GPIO in self controller writes
        self.controller.write()
        self.controller.write()
        self.controller.write()
        self.controller.write()
        if not index:
            current_PWM1, current_PWM2 = 780000 * Turn_multiplier, 600000 * Turn_multiplier
        else:
            current_PWM2, current_PWM1 = self.fill_speed_tables[index]
        if (self.lastPWM1 == current_PWM1 and self.lastPWM2 == current_PWM2):
            return
        self.controller.hardware_PWM(13, WORKING_FREQUENCY, current_PWM1)
        self.controller.hardware_PWM(12, WORKING_FREQUENCY, current_PWM2)
        self.lastPWM1 = current_PWM1
        self.lastPWM2 = current_PWM2

    def fill_speed_tables(self):
        for i in range(10):
            self.speed_table[i] = (580000, 360000)
        for i in range(10, 20):
            self.speed_table[i] = (650000, 380000)
        for i in range(20, 30):
            self.speed_table[i] = (670000, 400000)
        for i in range(30, 40):
            self.speed_table[i] = (720000, 420000)
        for i in range(40, 50):
            self.speed_table[i] = (730000, 430000)
        for i in range(50, 60):
            self.speed_table[i] = (735000, 435000)
        for i in range(60, 70):
            self.speed_table[i] = (790000, 490000)
        for i in range(70, 80):
            self.speed_table[i] = (800000, 500000)

    def shutdown(self):
        self.stop()
        # insert access to pi's GPIO in self controller writes
        self.controller.write()
        self.controller.write()
        self.controller.write()
        self.controller.write()
        self.controller.stop()
        

if __name__ == "__main__":
    import time
    Controller = MotorController()
    Controller.forward()
    time.sleep(1)
    Controller.turn_left()
    time.sleep(5)
    Controller.turn_right()
    time.sleep(5)
    Controller.stop()









