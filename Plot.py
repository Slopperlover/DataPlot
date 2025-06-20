import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from enum import Enum


class Layout(Enum):
    LINE_STYLE = ('-', '--', ':', '-.')
    LEGEND_LOCATION = ('upper left', 'upper right', 'center left',
                        'center right', 'lower left', 'lower right')
    COLOR = ('red', 'green', 'blue', 'purple', 'black', 'orange')
    Y_AS_POSITION = (('outward', 60), ('outward', 120),
                      ('outward', 180), ('outward', 240))


class Plot:
    """
    A class for plotting data from a CSV file, with support for multiple
    y-axes and live updates.

    Args:
        file_path (str): Path to the CSV file (e.g., 'C:\\python\\file.csv').
        data (list): Columns for y-axis as a list (e.g., ['1', '2']).
        own_axes (dict): Mapping of lines to y-axes (e.g., {1: 1, 2: 2}).
        x_column (str): Column for the x-axis (e.g., '0').
        data_name (list): Names for data lines (e.g., 'speed', 'distance').
        y_axis_name (list): Names for y-axes (e.g., 'km/h', 'meters').
    """
    def __init__(self, file_path: str, data: list, own_axes: dict = {}, 
                 x_collum: str = '0', data_naam: list = ['x'],
                 yas_naam: list = ['Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6']):
        
        # Variabele toekening
        self.aantal_lijnen = len(own_axes)
        self.data = data
        self.file_path = file_path
        self.own_axes = own_axes
        self.x_collum = x_collum
        self.yas_naam = yas_naam
        self.figure_ax = []
        self.value_y_as = [] 

        # kijk naar hoogste waarde in own_axes
        self.higest_figure_ax = self.own_axes[max(self.own_axes, key = self.own_axes.get)] 
        
        # Maak voor value_y_as list lang genoeg (nodig voor live_data)
        for counter in range(self.aantal_lijnen):
            self.value_y_as += [0]

        # Invoer nacheck
        if self.aantal_lijnen != len(self.data):            
            raise Exception("Ongeldig data aantal")
        
        # Geef toegekende naam door aan de juiste lijn
        if data_naam[0] != 'x':
            self.data_naam = data_naam
        # Als er geen naam gegeven is geef dan standart naam door
        else: 
            standart_naam = []
            for counter in range(int(max(data)) + 1):
                standart_naam += [counter]
            self.data_naam = standart_naam


    def assigning_lines(self):
        """
        Assign data columns from the CSV to x- and y-axes. 
        """
        # Open de csv document
        sorce = pd.read_csv(self.file_path, low_memory = False)

        # kijk of gezochte data in de document te vinden is
        if self.x_collum not in sorce.columns:
            raise Exception(f"Column '{self.x_collum}'not found in the CSV file.")
            
        # Ken toe de x-as
        self.value_xas = sorce[self.x_collum]
        
        # Ken toe de y-assen 
        for counter in range(self.aantal_lijnen):
            self.value_y_as[counter] = sorce[self.data[counter]]


    def make_figure(self):
        """
        Create the figure with all associated value axes
        """
        # Maak subplot object
        figuur, ax = plt.subplots()

        # onthoud het figuur voor live plotten
        self.figuur = figuur 

        # onthoud het ax voor assigning_yas
        self.figure_ax += [ax] 

        for counter in range(self.higest_figure_ax - 1): # min 1 sinds eerste waarde als toegekend is
            self.figure_ax += [ax.twinx()] # Maak nieuwe y-as


    def assigning_figure_axes(self):
        """
        Give each figure_ax correct formatting
        """
        for counter in range(self.higest_figure_ax):
            self.figure_ax[counter].set_ylabel(self.yas_naam[counter], 
                                              color = Layout.COLOR.value[counter]) # Opmaak van label maken
            self.figure_ax[counter].tick_params(axis='y', 
                                               labelcolor= Layout.COLOR.value[counter]) # Voeg ticks toe
            
            if counter > 1:
                # Voeg een nieuwe y-as (werkt niet met live plotten)
                self.figure_ax[counter].spines['right'].set_position(Layout.Y_AS_POSITION.value[counter - 2]) # min 2 sinds eerste 2 niet toegekend worden


    # Werkt nog niet
    def assigning_figure_axes_live(self):
        self.figure_ax[0].set_ylabel(self.yas_naam[0], color = Layout.COLOR.value[0]) # Opmaak van label maken
        self.figure_ax[0].tick_params(axis='y', labelcolor= Layout.COLOR.value[0]) # Voeg ticks toe
        
        self.figure_ax[1].set_ylabel(self.yas_naam[1], color = Layout.COLOR.value[1]) # Opmaak van label maken
        self.figure_ax[1].tick_params(axis='y', labelcolor= Layout.COLOR.value[1]) # Voeg ticks toe
        self.figure_ax[1].yaxis.set_label_coords(1.04, 0.5)

        self.figure_ax[2].set_ylabel(self.yas_naam[2], color = Layout.COLOR.value[2]) # Opmaak van label maken
        self.figure_ax[2].tick_params(axis='y', labelcolor= Layout.COLOR.value[2]) # Voeg ticks toe
        self.figure_ax[2].yaxis.set_label_coords(1.1, 0.5)


    def format_adjustment(self):
        """
        Adjust the figure size (doesn't fully work with live plotting)
        """
        match len(self.figure_ax):
            case 1:
                plt.subplots_adjust(left=0.055, right=0.97, 
                    top=0.95, bottom=0.08)
            case 2:
                plt.subplots_adjust(left=0.055, right=0.94, 
                    top=0.95, bottom=0.08)
            case 3:
                plt.subplots_adjust(left=0.055, right=0.89, 
                    top=0.95, bottom=0.08)
            case 4:
                plt.subplots_adjust(left=0.055, right=0.84, 
                    top=0.95, bottom=0.08)
            case 5:
                plt.subplots_adjust(left=0.055, right=0.78, 
                    top=0.95, bottom=0.08)
            case 6:
                plt.subplots_adjust(left=0.055, right=0.73, 
                    top=0.95, bottom=0.08)


    def legend(self):
        """
        Make legend
        """
        for counter in range(self.higest_figure_ax):
            self.figure_ax[counter].legend(loc = Layout.LEGEND_LOCATION.value[counter]) # Print de legenda
      

    def clear(self):
        """
        Delate last plot (only used in live plot)
        """
        for counter in range(self.higest_figure_ax):
            self.figure_ax[counter].cla() # Clear line
            

    def plot(self):
        """
        Plot data
        """
        # Counter om te zorgen dat lijnen met zelfde value_as ander stijl krijgen 
        style_counter = []

        for counter in range(self.higest_figure_ax):
            style_counter += [0] # Elke value_as krijg ze eigen counter

        # Ga door elke lijn om het bij juiste value_as te plotten
        for counter in self.own_axes:
            self.figure_ax[self.own_axes[counter] - 1].plot(self.value_xas, self.value_y_as[counter - 1],
                        label=self.data_naam[int(self.data[counter - 1])], 
                        color= Layout.COLOR.value[self.own_axes[counter] - 1],
                        linestyle= Layout.LINE_STYLE.value[style_counter[self.own_axes[counter] - 1]]) # Plot de data
            style_counter[self.own_axes[counter] - 1] += 1
                        
        self.legend()


    def plot_live(self, call_back):
        """
        Plot the data live
        """
        self.clear()
        self.assigning_lines()
        self.plot()


    def show(self):
        """
        Show the graph
        """
        self.make_figure()
        self.assigning_figure_axes()
        self.assigning_lines()
        self.plot()

        self.format_adjustment()
        plt.show()


    def show_live(self, intervlas: int= 500):
        """
        Show the graph with live updates
        """
        self.make_figure()
        self.assigning_figure_axes()
        live = FuncAnimation(self.figuur, self.plot_live, interval= intervlas,
                              cache_frame_data= False)

        self.format_adjustment()
        plt.show()        


if __name__ == "__main__":

    datanaam = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    value = ['Hi', 'HELLO', 'HOW', 'Are', 'You', 'Not']

    Graf = Plot('C:\\school\\python\\git\\DataPlot\\7_VESC_20_02.csv', ['3', '4', '5'], {1: 1, 2: 2, 3: 3}, '1', datanaam, value)

    Graf.show()
