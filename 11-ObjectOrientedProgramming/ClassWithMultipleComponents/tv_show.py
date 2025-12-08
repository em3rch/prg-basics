# tv_show.py file
# main program
import tv

def main():
   # object creation
   televisor = tv.TV()  # 1

   # object usage
   televisor.show_status()  # 2
   televisor.turn_on()  # 3
   televisor.show_status()  # 4
   televisor.show_channels() # 5
   televisor.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"])  # 6
   televisor.show_channels() # 7
   televisor.show_status()  # 8
   televisor.turn_off()  # 9

if __name__ == "__main__":
   main() 