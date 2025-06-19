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
     """
     def __init__(self):
          self.x_collum = None
          self.own_axes = {}
          self.data = []

          self.lines_amount = 1

     def print_interface(self):
          """
          """
          print("x colum:", self.x_collum, "\n"
               "lines with y-axes:", self.own_axes, "\n"
               "Data colums used:", self.data, "\n"
               "Press H for help", "\n"
               )

     def add_line(self, y_as: chr, data_colum: chr):
          self.own_axes.update({self.lines_amount: int(y_as)})
          self.data.append(data_colum)
          self.lines_amount += 1

     def change_xas(self, new_xas: chr):
          """
          """
          self.x_collum = new_xas

     def delete_line(self, delete_line: chr):
          """
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
          """
          self.own_axes[int(line)] = int(y_as)

     def change_data(self, line: chr, data: chr):
          """
          """
          self.data[int(line) - 1] = data

     def help(self):
          """
          Prints list with all commands
          """
          print("All avaible comands are:\n" \
               "A: to add a line\nD: to delete a line\n" \
               "C: to change attribute of a line\n" \
               "Q: to quit the program")
          readchar.read_char()

     def prt(self):
          print(self.lines_amount, self.data, self.own_axes)


if __name__ == "__main__":
    args = parse_argument()
    if args.path == None:
        print("Ad a file path with -P")
        exit()
    else:
        print("jup\n")
        print(args)