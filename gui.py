import argparse

def parse_argument():
    """
    Make flags to give for plotting of graphs
    flags  
    -P: Path of the wanted csv file.

    -D: Colums with wanted data.

    -Y: Assignment of lines to corresponding y-axes.

    -X: X colum.

    -N: Data lines names.

    -A: Axes value
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('-P' ,'--Path', type=str,
                        help="Path of the wanted csv file")
    
    parser.add_argument('-D' ,'--data', type=list,
                        help="Colums with wanted data")
    
    parser.add_argument('-Y' ,'--assignment', type=dict,
                        help="Assignment of lines to " \
                        " corresponding y-axes")
    
    parser.add_argument('-X' ,'--xcolum', type=str,
                        help="Colum with x-as value")
    
    parser.add_argument('-N' ,'--name_l', type=list,
                        help="Name of the lines")
    
    parser.add_argument('-A' ,'--name_a', type=list,
                        help="Name of the y axes")
    
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_argument()
    print(args)