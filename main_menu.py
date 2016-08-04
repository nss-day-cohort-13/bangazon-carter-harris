from user import *

class Main_menu():


  def new_user_select_user_menu(self):
    '''
      First Menu the user will see.
      They will be able to make and account or select a user to begin chirpping.

    '''

    # Command line menu for Birdyboard
    print(' ~ Tweet tweet, welcom to BirdyBoard, plz select from the following menu ~ ')
    print('')
    print('1. New User Account')
    print('2. Select User')
    print('')
    print('6. Exit')
    choice = input('> ')

    # New User choice
    if int(choice) == 1:

      # If choice is '1' the user enters full name and screen name
      if choice == '1':
        print('Enter full name')
        full_name = input('> ')

        print('Enter screen name')
        screen_name = input('> ')

        print('Hello {0}, or should I call you by your real name -> {1}'.format(screen_name, full_name))

        # The two user inputs are now passed into the User class to create a User object
        user = User(full_name, screen_name)


    elif choice == '2':
      pass

    else:
      exit()




if __name__ == "__main__":
  chirp = Main_menu()
  chirp.new_user_select_user_menu()
