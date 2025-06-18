from Plot import Plot
from dataformat import Datafromat

datanaam = Datafromat.VESC_motor_driver.value

value = ['Hi', 'HELLO', 'HOW', 'Are', 'You', 'Not']

wow = Plot('D:\\git\\DataPlot\\7_VESC_20_02.csv', ['4', '5'], {1: 1, 2: 2}, '1', datanaam, value)

wow.show_live()
