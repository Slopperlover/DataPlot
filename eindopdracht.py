from Plot import Plot
from dataformat import Datafromat
import readchar
import os
from gui import Gui


if __name__ == "__main__":
    datanaam = Datafromat.VESC_motor_driver.value
    command = Gui()

    while True:
        command.print_interface()
        message = readchar.read_char()
        
        # Execute incoming commands accordingly
        match message:
            case 'a' | 'A': # Ad a line
                y_as = input("On wich y-as would you like to add a line: ")
                data_colum = input("witch colum would you like to use for data: ")
                command.add_line(y_as, data_colum)
            case 'd' | 'D': # Delete a line
                delete_line = input("wich line would you like to delete: ")
                command.delete_line(delete_line)
            case 'x' | 'X': # Ad x-colum
                x_as = input("What is the new x-as: ")
                command.change_xas(x_as)
            case 'c' | 'C': # Change line attribute
                line_change = input("Wich line would you like to change: ")
                change = input("Would you like to change y-as(1) or data colum(2): ")
                if change == "1":
                        y_as_change = input("What is the new y-as: ")
                        command.change_yas(line_change, y_as_change)
                elif change == "2":
                        data_colum_change = input("What is the new data_colum: ")
                        command.change_data(line_change, data_colum_change)
                else:
                        print("incorect input")
            case 's' | 'S': # Show the plot
                graph = Plot('7_VESC_20_02.csv', command.data, command.own_axes, command.x_collum, datanaam)
                graph.show()
            case 'h' | 'H': # Print all comands
                command.help()
            case 'q' | 'Q': # Exit the program
                exit()
        #clear screen
        os.system('cls')