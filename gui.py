import argparse

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


if __name__ == "__main__":
    args = parse_argument()
    if args.path == None:
        print("Ad a file path with -P")
        exit()
    else:
        print("jup\n")
        print(args)