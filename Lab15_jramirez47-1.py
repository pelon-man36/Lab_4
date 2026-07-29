"""
Ploting a Sine Wave
Johan D. Ramirez Maldonado
This program creates a sine wave using matplotlib and math module respectively.
07/29/26
"""

import matplotlib.pyplot as plt 
import math

class SineWave:
    """
    Creates a Sine Wave using matplotlib & math module.
    
    Args:
        num_points (default=500)
        wcycles (default=2)
    """
    def __init__(self, num_points=500, wcycles=2):
        """Takes in num_points and wcycles as arguments to create the sine wave."""
        self.num_points = num_points
        self.wcycles = wcycles
        self.x = []
        self.y = []

    def gen_values(self):
        """Generates the x and y values for the sine wave using the math module."""
        max_x = self.wcycles * 2 * math.pi

        space = max_x / (self.num_points - 1)
        self.x_value = [i * space for i in range(self.num_points)]
        self.y_value = [math.sin(i) for i in self.x_value]

    def plot(self):
        """Plots the sine wave using the matplotlib module."""
        plt.style.use("seaborn-v0_8")
        fig, ax = plt.subplots()
        ax.plot(self.x_value, self.y_value, color="red", linewidth=3)
        ax.set_title("Sine Wave", fontsize=24)
        ax.set_xlabel("Radians", fontsize=14)
        ax.set_ylabel("Amplitude", fontsize=14)

        plt.savefig("Sine_Wave.png")
        plt.show()

if __name__ == "__main__":
    wave = SineWave()
    wave.gen_values()
    wave.plot()