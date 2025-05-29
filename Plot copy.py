
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


COLOR = ('red', 'blue', 'green', 'purple')

MARKER = ('o', 's', '^', '*')

class Plot:
    def __init__(self, file_path: str ,data: tuple, own_axes: dict={}, x_collum: str= '0'):
        """
        Met deze class plot je data uit het csv-document, tot 4 datalijnen met mogelijkheid voor aparte y-as.

        file_path: Locatie van csv-document in de vorm van str (bv: 'C:\\python\\file.csv')
        
        data: Cel locatie van y-as in de vorm van str in een tuple (bv: ('1', '2'))
        
        own_axes: Lijn en y-as in de vorm van dict (bv: {1: 1, 2: 1, 3: 2})
        
        x_as: Cel locatie van x-as in vorm van str (bv: '0')
        """
        # Variabele toekening
        self.aantal = len(own_axes)
        self.data = data
        self.file_path = file_path
        self.own_axes = own_axes
        self.x_collum = x_collum 
        self.y_as = [0, 0, 0, 0]
        
        # Invoer nacheck
        if self.aantal != len(self.data):            
            raise Exception("Ongeldig data invoer of aantal")

    def assigning_lines(self):
        """
        Assen toekennen uit csv-document 
        """
        # Open de csv document
        sorce = pd.read_csv(self.file_path)

        if self.x_collum not in sorce.columns:
            raise KeyError(f"Column '{self.x_collum}' not found in the CSV file.")

        # Ken toe de x-as
        self.x_as = sorce[self.x_collum]
        
        # Ken toe de y-assen 
        self.y_as[0] = sorce[self.data[0]]
        if self.aantal == 2:
            self.y_as[1] = sorce[self.data[1]]
        elif self.aantal == 3:
            self.y_as[2] = sorce[self.data[2]]
        elif self.aantal == 4:
            self.y_as[3] = sorce[self.data[3]]
        
    def assigning_yas(self):
        # Maak subplot object
        figuur, ax1 = plt.subplots()

        # onthoud het figuur voor live plotten
        self.figuur = figuur

        for counter in self.own_axes:
            if self.own_axes[counter] == 1:
                ax1.set_ylabel('Y1', color= 'red') # Opmaak van label maken
                ax1.tick_params(axis='y', labelcolor= 'red') # Voeg ticks toe
                self.ax1 = ax1 # Ken ax toe
            elif self.own_axes[counter] == 2:
                ax2 = ax1.twinx() # Maak nieuwe y-as
                ax2.set_ylabel('Y2', color= 'blue')
                ax2.tick_params(axis='y', labelcolor= 'blue')
                self.ax2 = ax2
            elif self.own_axes[counter] == 3:
                ax3 = ax1.twinx()
                ax3.spines['right'].set_position(('outward', 60))
                ax3.set_ylabel('Y3', color= 'green')
                ax3.tick_params(axis='y', labelcolor= 'green')
                self.ax3 = ax3
            elif self.own_axes[counter] == 4:
                ax4 = ax1.twinx()
                ax4.set_ylabel('Y4', color= 'purple')
                ax4.tick_params(axis='y', labelcolor= 'purple')
                ax4.spines['right'].set_position(('outward', 120))
                self.ax4 = ax4

    def plot(self):
        """
        Plotten van data 
        """
        # Ga door elke lijn om y-as te plotten
        for counter in self.own_axes: 
            if self.own_axes[counter] == 1:
                self.ax1.plot(self.x_as, self.y_as[counter - 1], label=self.data[counter - 1],
                               color= 'red', marker= MARKER[counter - 1]) # Plot de data
            elif self.own_axes[counter] == 2:
                self.ax2.plot(self.x_as, self.y_as[counter - 1], label=self.data[counter - 1],
                               color= 'blue', marker= MARKER[counter - 1])
            elif self.own_axes[counter] == 3:
                self.ax3.plot(self.x_as, self.y_as[counter - 1], label=self.data[counter - 1],
                               color= 'green', marker= MARKER[counter - 1])
            elif self.own_axes[counter] == 4:
                self.ax4.plot(self.x_as, self.y_as[counter - 1], label=self.data[counter - 1],
                               color= 'purple', marker= MARKER[counter - 1])
                
    def legend(self):
        for counter in self.own_axes:
            if self.own_axes[counter] == 1:
                self.ax1.legend(loc='upper left') # Print legenda
            elif self.own_axes[counter] == 2:
                self.ax2.legend(loc='center left')
            elif self.own_axes[counter] == 3:
                self.ax3.legend(loc='upper right')
            elif self.own_axes[counter] == 4:
                self.ax4.legend(loc='center right')
                
    def plot_live(self, call_back):
        """
        Plot de data live
        """

        self.assigning_lines()
        self.plot()

    def show(self):
        """
        Laat het grafiek zien
        """
        self.assigning_lines()
        self.assigning_yas()
        self.plot()
        self.legend()

        plt.tight_layout()
        plt.show()

    def show_live(self, intervlas: int= 100):
        """
        Plot de data live en laat het zien
        """
        self.assigning_yas()
        live = FuncAnimation(self.figuur, self.plot_live, interval= intervlas, cache_frame_data= False)

        plt.tight_layout()
        plt.show()

    def debug(self):
        self.assigning_lines()
        self.assigning_yas()
        self.plot()
        print(self.y_as[2])
        


Graf = Plot('C:\\school\\python\\live.csv', ('1', '2', '3'), {1: 1, 2: 2, 3: 3})

Graf.show_live()
