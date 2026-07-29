import matplotlib.pyplot as plt 
import math

class SineWave:
    def __init__(self, num_points=500, wcycles=2):
        self.num_points = num_points
        self.wcycles = wcycles
        self.x = []
        self.y = []

    def gen_values(self):
        max_x = self.wcycles * 2 * math.pi

        space = max_x / (self.num_points - 1)
        self.x_value = [i * space for i in range(self.num_points)]
        self.y_value = [math.sin(i) for i in self.x_value]

    def plot(self):
        plt.style.use("seaborn-v0_8")
        fig, ax = plt.subplots()
        ax.plot(self.x_value, self.y_value, color="red", linewidth=3)
        ax.set_title("Sine Wave", fontsize=24)
        ax.set_xlabel("Radians", fontsize=14)
        ax.set_ylabel("Amplitude", fontsize=14)
        plt.show()

if __name__ == "__main__":
    wave = SineWave()
    wave.gen_values()
    wave.plot()