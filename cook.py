import threading
import time
import readchar
import os

# def loop():
#         while True:
#             print("loop")
#             time.sleep(1)

# def stop():
#     while True:
#          key = input("enter the key")
#          if key == "q":
#               exit()

# if __name__ =="__main__":
#     t1 = threading.Thread(target=loop)
#     t2 = threading.Thread(target=stop)

#     t1.start()
#     while True:
#          key = input("enter the key")
#          if key == "q":
#               t1.join()
#               exit()


class Gui:
     """
     """
     def __init__(self):
          self.x_collum = None
          self.own_axes = {}
          self.data = []

          self.lines_amount = 1

     def print_interface(self):
          print("x colum:", self.x_collum, "\n"
               "lines with y-axes:", self.own_axes, "\n"
               "Data colums used:", self.data, "\n"
               )

     def add_line(self, y_as: chr, data_colum: chr):
          self.own_axes.update({self.lines_amount: int(y_as)})
          self.data.append(data_colum)
          self.lines_amount += 1

     def change_xas(self, new_xas: chr):
          self.x_collum = new_xas

     def delete_line(self, delete_line: chr):
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
               
               replacement_dictionary = {}
               counter = 1
               for old_keys in self.own_axes:
                    replacement_dictionary[counter] \
                         = self.own_axes[old_keys]
                    counter += 1
               self.own_axes = replacement_dictionary

          else:
               print("Line", delete_line, "doesn’t exist")
               time.sleep(3)

     def prt(self):
          print(self.lines_amount, self.data, self.own_axes)


objec = Gui()


while True:
     objec.print_interface()
     message = readchar.read_char()
     #clear screen
     
     match message:
          case 'a' | 'A':
              y_as = input("On wich y-as would you like to add a line: ")
              data_colum = input("witch colum would you like to use for data: ")

              objec.add_line(y_as, data_colum)
          case 'd' | 'D':
               delete_line = input("wich line would you like to delete: ")
               objec.delete_line(delete_line)
          case 'x' | 'X':
               x_as = input("What is the new x-as: ")
               objec.change_xas(x_as)
          case 'q' | 'Q':
               exit()
     os.system('cls')
     print(message)
