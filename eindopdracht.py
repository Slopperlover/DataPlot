from Plot import Plot
from dataformat import Datafromat

datanaam = Datafromat.VESC_motor_driver.value

value = ['Hi', 'HELLO', 'HOW', 'Are', 'You', 'Not']

wow = Plot('C:\\school\\python\\eindopdracht\\7_VESC_20_02.csv', ['4', '5', '7', '9', '10', '11'], {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}, '1', datanaam, value)

wow.show()
