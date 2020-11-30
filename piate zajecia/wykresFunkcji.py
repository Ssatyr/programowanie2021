import matplotlib
import matplotlib.pyplot as plt

class wykresFunkcji:
    def __init__(self, functions_set):
        self.functions_set = functions_set
        self.x_min = -10
        self.x_max = 10
        self.y_min = None
        self.y_max = None
        self.step = 0.0001

    def set_x_range(self, min, max):
        self.x_min = min
        self.x_max = max

    def set_y_range(self, min, max):
        self.y_min = min
        self.y_max = max

    def set_step(self, step):
        self.step = step

    def _calculate_functions(self):
        for funkcja in self.functions_set.set_of_functions:
            funkcja.set_x_range(self.x_min, self.x_max)
            funkcja.set_step(self.step)
            funkcja.calculate()

    def _add_functions_to_plot(self):
        for funkcja in self.functions_set.set_of_functions:
            plt.plot(funkcja.x, funkcja.y, label=funkcja.info)

    def _set_axes(self):
        axes = plt.gca()
        axes.set_xlim([self.x_min, self.x_max])
        if self.y_min and self.y_max:
            axes.set_ylim([self.y_min, self.y_max])

    def _set_labels(self):
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Wykresy funkcji")

    def _set_layout(self):
        plt.tight_layout()

    def _add_legend(self):
        plt.legend()

    def _show_plot(self):
        plt.show()

    def plot(self):
        self._calculate_functions()
        self._add_functions_to_plot()
        self._set_labels()
        self._set_axes
        self._set_layout
        self._add_legend
        self._show_plot

