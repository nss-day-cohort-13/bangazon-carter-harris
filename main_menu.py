from user import *

class Main_menu():

  def show_menu(self):
    # list to store user_name and full_name

    # Command line menu for Birdyboard
    print(' ~ Tweet tweet, welcom to BirdyBoard, plz select from the following menu ~ ')
    print('')
    print('1. New User Account')
    print('2. Select User')
    print('')
    print('6. Exit')
    choice = input('> ')

    if int(choice) == 1:

      if choice == '1':
        print('Enter full name')
        full_name = input('> ')

        print('Enter screen name')
        screen_name = input('> ')

        print('Hello {0}, or should I call you by your real name -> {1}'.format(screen_name, full_name))

        user = User(full_name, screen_name)


    elif choice == '2':
      pass

    else:
      exit()




if __name__ == "__main__":
  chirp = Main_menu()
  chirp.show_menu()
