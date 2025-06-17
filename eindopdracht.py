from Plot import Plot
from dataformat import Datafromat

datanaam = Datafromat.VESC_motor_driver.value

wow = Plot('C:\\school\\python\\live.csv', ['1', '2'], {1: 1, 2: 2}, '0', datanaam)

wow.show_live()
