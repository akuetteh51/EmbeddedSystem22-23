from machine import Pin
from math import floor
from time import sleep_ms
import _thread

class Stepper:
    def __doc__(self):
        return """
            Mode:
                0 - Full Mode
                1 - Half Mode
            
        """
    def __init__(self, in1=0, in2=0, in3=0, in4=0, mode=0): 
        self.in1 = Pin(in1, Pin.OUT)
        self.in2 = Pin(in2, Pin.OUT)
        self.in3 = Pin(in3, Pin.OUT)
        self.in4 = Pin(in4, Pin.OUT)
        self.isMoving = False
        self.mode = mode
    
    def setMode(self, mode):
        if(mode==0 or mode ==1):
            self.mode = mode

    def move(self, steps, forward=1):
        self.isMoving = True
        for i in range(steps):
            if(self.mode == 0):
                self._fullPhase(i, forward)
            elif(self.mode == 1):
                self._halfPhase(i, forward)
        self.isMoving = False
            
    def getMode(self):
        return self.mode
    
    def _setPosition(self, out):
        self.in1.value(out[0])
        self.in2.value(out[1])
        self.in3.value(out[2])
        self.in4.value(out[3])
        
    def _fullPhase(self, stage, forward=1):
        sequence = [
                [1,0,0,0],
                [0,1,0,0],
                [0,0,1,0],
                [0,0,0,1],
            ]
        self._step(sequence, stage, forward)
    
    def _halfPhase(self, stage, forward=1):
        sequence = [
                [1,0,0,0],
                [1,1,0,0],
                [0,1,0,0],
                [0,1,1,0],
                [0,0,1,0],
                [0,0,1,1],
                [0,0,0,1],
                [1,0,0,1],
            ]
        self._step(sequence, stage, forward)
        
    def _step(self, sequence, stage, forward=1):
        actual_sequence = sequence
        if(forward == -1):
            actual_sequence.reverse()
        combination = stage % len(actual_sequence)
        self._setPosition(actual_sequence[combination])
        sleep_ms(10)
    
    def angle(self, angle, forward=1):
        steps = floor((angle*2048)/360)
        if(self.mode==1):
            steps *= 2
        self.move(steps, forward)

    def asyncAngle(self, angle, forward=1):
        _thread.start_new_thread(self.move, (angle, forward))

    def asyncMove(self, steps, forward=1):
        _thread.start_new_thread(self.move, (steps, forward))