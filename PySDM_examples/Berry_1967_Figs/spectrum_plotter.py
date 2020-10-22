"""
Created at 12.08.2019
"""

from matplotlib import pyplot
from PySDM_examples.Shima_et_al_2009_Fig_2.spectrum_plotter import SpectrumPlotter as SuperSpectrumPlotter


class SpectrumPlotter(SuperSpectrumPlotter):
    def __init__(self, setup, title=None, grid=True, legend=False):
        size = 2 * 5.236
        pyplot.figure(num=1, figsize=(size, size * 0.54))
        pyplot.xlabel('particle radius [µm]')
        pyplot.ylabel('dm/dlnr [g/m^3/(unit dr/r)]')
        super().__init__(setup, title=title, grid=grid, legend=legend, log_base=2)
        self.color = None
        self.smooth = True

    def ticks(self):
        xticks = [4, 6.25, 12.5, 25, 50, 100, 200]
        pyplot.xticks(xticks, xticks)
        pyplot.yticks([0.5 * i for i in range(5)], [0, None, 1, None, 2])

    def show(self):
        self.finish()
        self.ticks()
        pyplot.show()

    def plot(self, spectrum, t):
        setup = self.setup
        self.plot_data(setup, t, spectrum)


