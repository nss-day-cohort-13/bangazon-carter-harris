
class Birdyboard():


  def show_menu(self):
    # Command line menu for Birdyboard
    print("~ Select from the following menu ~")
    print('')
    print("1. New User Account")
    print("2. Select User")
    print("3. View Chirps")
    print("4. Public Chirp")
    print("5. Private Chirp")
    print("6. Exit")
    choice = input("> ")

    try:
      # Checks to make sure the user does not type in a negaitive or higher than 4 number
      if int(choice) > 0 and int(choice) < 7:


        if choice == "1":
          print('number one')


        if choice == "2":
          print('number two')


        if choice == "3":
          print('number three')


        if choice == "4":
          print('number four')


        if choice == "5":
          print('number five')


        if choice == "6":
          print('number ')


    except:
      self.show_menu()


if __name__ == "__main__":
  chirp = Birdyboard()
  chirp.show_menu()