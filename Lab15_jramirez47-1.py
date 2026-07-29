import matplotlib.pyplot as plt 
import math

class SineWave:
    def __init__(self, num_points=500, wcycles=2):
        self.num_points = num_points
        self.wcycles = wcycles

    def gen_values(self):
        max_x = self.wcycles * 2 * math.pi

        space = max_x / (self.num_points - 1)
        x_value = [i * space for i in range(self.num_points)]
        y_value = [math.sin(i) for i in x_value]

    def plot(self):
        pass