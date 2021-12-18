import sys

def check_speed(VEL: int) -> None:
    if(VEL < 10):
        print("Increase speed! Min. 10")
        sys.exit()
    elif(VEL > 20):
        print("Reduce speed! Max. 20")
        sys.exit()