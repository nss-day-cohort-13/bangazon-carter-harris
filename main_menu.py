from user import *
from serialization import *
from user import *
from chirp import *
from conversation import *

all_users = {}
all_chirps = {}
all_convos = {} # convos aka conversations
all_users = {}

class Main_menu():
  def __init__(self):
    self.selected_user = None
    self.users = list()


  def start_menu(self):
    '''
      First menu the user will see.
      They will be able to make and account or select a user to begin chirpping.
    '''

    # Command line menu for Birdyboard
    print(' ~ Tweet tweet, welcom to BirdyBoard, plz select from the following menu ~ ')
    print('\n')
    print('1. New User Account')
    print('2. Select User')
    print('\n')
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

        # Users name is printed to welcome them
        print('Hello {0}, or should I call you by your real name -> {1}'.format(screen_name, full_name))

        # The two user inputs are now passed into the User class to create a User object
        user = User(full_name, screen_name)

        self.users.append(user)

        serialize_users('users.txt', self.users)
        # for item in self.users:
        #   print(item.full_name, item.screen_name)


    # Direct the user to the View Users Menu
    elif choice == '2':

      self.view_users_menu()

    else:
      exit()




  def view_users_menu(self):
    '''
      This menu will show the user all the users for them to select which one
      they will chirp from.

    '''
    print('\n')
    print('Select your user')
    print('\n')
    # for user in users:

    # print('Users:', print_users())
    print('\n')
    selected_user = input('> ')

    pass




  def view_chirps_menu(self):
    '''
      This menu will show the user all the chirps, public and private. The user will then
      pick which chirp thread they want to chirp at.

    '''
    print('lol')
    pass






if __name__ == "__main__":
  chirp = Main_menu()
  chirp.new_user_select_user_menu()
