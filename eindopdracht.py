from Plot import Plot
from dataformat import Datafromat

#C:\\school\\python\\eindopdracht\\7_VESC_20_02.csv

# Geef datanaam door
datanaam = Datafromat.VESC_motor_driver.value

if __name__ == "__main__":
    # Init plot
    wow = Plot('C:\\school\\python\\eindopdracht\\live.csv', ['1', '2', '3'], {1: 1, 2: 2, 3: 1}, '0', datanaam)

    # Laat plot zien
    wow.show_live()