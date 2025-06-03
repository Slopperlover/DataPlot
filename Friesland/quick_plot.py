from Plot import Plot
from dataformat import Datafromat

vesc = Datafromat.VESC_motor_driver.value
accu = Datafromat.ACCU.value
mppt = Datafromat.MPPT.value
master = Datafromat.MASTER.value

# 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100


if __name__ == "__main__":

    # Voorbeeld
    #            Addres van document,                  colum nummers,    , y-axes,         x-as,  data fromat    
    #wow = Plot('D:\\git\\DataPlot\\7_VESC_20_02.csv', ['4', '5', '6'], {1: 1, 2: 2, 3: 3}, '1', datanaam)

    wow = Plot('D:\\git\\DataPlot\\Friesland\\2_MPPT_0_05_07.csv', ['4', '5', '0', '7'], {1: 1, 2: 2, 3: 3, 4: 4}, '3', mppt)

    wow.show()
