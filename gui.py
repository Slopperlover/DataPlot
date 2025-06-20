import argparse
import readchar

def parse_argument():
    """
    Make flag to give the path
    flag
    -P: Path of the wanted csv file.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('-P' ,'--Path', dest ='path', type=str,
                        help="Path of the wanted csv file")
    
    return parser.parse_args()

class Gui:
     """
     The gui class is a simple terminal interface dedicated
     to plotting files using the plot class 
     """
     def __init__(self):
          self.x_collum = None
          self.own_axes = {}
          self.data = []

          self.lines_amount = 1

     def print_interface(self):
          """
          Prints the interface
          """
          print("x column:", self.x_collum, "\n"
               "lines with y-axes:", self.own_axes, "\n"
               "Data columns used:", self.data, "\n"
               "Press H for help", "\n"
               )

     def add_line(self, y_as: chr, data_colum: chr):
          """
          Ads line with a chosen y-axis and data column
          """
          self.own_axes.update({self.lines_amount: int(y_as)})
          self.data.append(data_colum)
          self.lines_amount += 1

     def change_xas(self, new_xas: chr):
          """
          Changes the column that is used for the x-axis
          """
          self.x_collum = new_xas

     def delete_line(self, delete_line: chr):
          """
          Deletes chosen line with all its attributes
          """
          flag = False
          position = 0
          for counter in self.own_axes:
               if int(delete_line) == counter:
                    # Delete dictionary and data list
                    self.own_axes.pop(counter)
                    self.data.pop(position)

                    flag = True
                    break

               position += 1

          if flag:
               self.lines_amount -= 1
               
               # Adjust own.axes by recopying the values to new keys
               replacement_dictionary = {}
               counter = 1
               for old_keys in self.own_axes:
                    replacement_dictionary[counter] \
                         = self.own_axes[old_keys]
                    counter += 1
               self.own_axes = replacement_dictionary

          else:
               print("Line", delete_line, "doesn’t exist")
               readchar.read_char()

     def change_yas(self, line: chr, y_as: chr):
          """
          Changes the yas of selected line
          """
          self.own_axes[int(line)] = int(y_as)

     def change_data(self, line: chr, data: chr):
          """
          Changes the data column of selected line
          """
          self.data[int(line) - 1] = data

     def help(self):
          """
          Prints helpful guide 
          """
          print("This program lets you plot graphs with multiple lines and y-axes.\n"\
               "You can plot up to 4 lines on each y-axis with the possibility\n" \
               "of having 6 y-axes simultaneously.\n\n" \
               "On the top of the terminal, you have x column, this let you\n" \
               "choose which data will be used for the x-axis. Lines with y-axes\n" \
               "represent added lines and on which y-axes they will be plotted\n"
               "(e.g., 2:1 means that line 2 will be plotted on y-axis one).\n" \
               "Data columns represent which data column is used for\n" \
               "plotting a line and are set in order of lines.\n\n" \
               "When the graph is plotted, you have to close it manually before\n"
               "changing its attributes.\n\n"
               "All avaible comands are:\n" \
               "A: to add a line\nD: to delete a line\n" \
               "C: to change attribute of a line\n" \
               "X: to change x column\n" \
               "S: to show the graf\n" \
               "Q: to quit the program")
          readchar.read_char()


if __name__ == "__main__":
    args = parse_argument()
    if args.path == None:
        print("Ad a file path with -P")
        exit()
    else:
        print("jup\n")
        print(args)