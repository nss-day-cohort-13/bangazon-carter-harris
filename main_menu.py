import os
import sys
import pickle
import time
import uuid
from user import *
from chirp import *
from conversation import *


class Birdyboard():
  '''
    Main class for the app that holds all the functionality for the app
  '''

  # turn txt files into variables
  users_filename = 'users.txt'
  chirps_filename = 'chirps.txt'
  conversations_filename = 'conversations.txt'

  def __init__(self):
    '''
      Set stuff
    '''

    # default current user to None
    self.current_user = None

    try:
      self.all_users = self.deserialize_data(self.users_filename)
      print(self.all_users)
    except EOFError:
      self.all_users = {}
    try:
      self.all_chirps = self.deserialize_data(self.chirps_filename)
      print(self.all_chirps)
    except EOFError:
      self.all_chirps = {}
    try:
      self.all_conversations = self.deserialize_data(self.conversations_filename)
      print(self.all_conversations)
    except EOFError:
      self.all_conversations = {}



# ----------------------------------------#
# ------------ Clear Function ------------#
# ----------------------------------------#
  def clear_the_page(self):
    ''' Clear the page when called '''
    clear = lambda: os.system('clear')
    clear()



# ----------------------------------------#
# -------------- Start Menu --------------#
# ----------------------------------------#
  def start_main_menu(self):
    '''
      First menu the user will see.
      They will be able to make and account or select a user to begin chirpping.
    '''

    # Command line menu for Birdyboard
    print('''
      *********************************************************
      *************    Welcome to BirdyBoard!     *************
      *********************************************************
    ''')
    print('')
    print('1. New User Account')
    print('2. Select User')
    print('3. View Chirps')
    print('4. Public Chirps')
    print('5. Private Chirp')
    print('6. Exit')
    choice = input('> ')

    # New User choice
    if choice == '1':
      self.create_user()
    elif choice == '2':
      self.select_users()
    elif choice == '3':
      self.view_chirps()
    elif choice == '4':
      self.create_public_chirp()
    elif choice == '5':
      self.create_private_chirp()
    elif choice == '6':
      exit()
    else:
      print('Invalid Input')
      time.sleep(1)



# ----------------------------------------#
# ------------- Create User --------------#
# ----------------------------------------#
  def create_user(self):
    '''
      Create user to be serialized in memory

      Args:
        N/A
    '''

    self.clear_the_page()

    print('Enter your full name')
    full_name = input('> ')
    print('Enter your screen name')
    screen_name = input('> ')

    # The two user inputs are now passed into the User class to create a User object
    new_user = User(full_name, screen_name)

    self.current_user = new_user
    # add new_user to all_users object with the new_user uuid as the key and value of the entire new_user object
    self.all_users[new_user.user_id] =     selected_user = int(input('> ')) # users input for running the for loop below
    for key, value in temp_user_dict.items():
      if key == selected_user:
        self.current_user = value
    self.serialize_data(self.all_users, self.users_filename)
    time.sleep(1)

    self.start_main_menu() # send the user back to the main menu



# ----------------------------------------#
# ------------- Select Users -------------#
# ----------------------------------------#
  def select_users(self):
    '''
      This menu will show the user all the users for them to select which one
      they will chirp from.

      Args:
        N/A
    '''
    self.clear_the_page()

    print('\n')
    print('Select your user')
    print('\n')

    temp_user_dict = dict()
    counter = 1
    for key, value in self.all_users.items():
      print('{}. {}'.format(counter, value.full_name))
      temp_user_dict[counter] = value
      counter += 1

    selected_user = int(input('> ')) # users input for running the for loop below
    for key, value in temp_user_dict.items():
      if key == selected_user:
        self.current_user = value
        print(self.current_user.full_name, self.current_user.user_id, self.current_user.screen_name)

    self.start_main_menu()




# ----------------------------------------#
# ------------- View Chirps --------------#
# ----------------------------------------#
  def view_chirps(self):
    '''
      This menu will show the user all the chirps, public and private. The user will then
      pick which chirp thread they want to chirp at.

    '''
    print('view chirps lol')
    print(self.all_chirps)
    # key of chirp_id, value of message blah blah

    temp_chirp_dict = dict()
    counter = 1
    for key, value in self.all_chirps.items():
      print('{}. {}'.format(counter, value.message))
      temp_chirp_dict[counter] = value
      counter += 1

    selected_chirp = int(input('> ')) # users input for running the for loop below
    for key, value in temp_chirp_dict.items():
      if key == selected_chirp:
        self.current_user = value
        print(self.current_user.full_name, self.current_user.user_id, self.current_user.screen_name)


    pass

    # temp_user_dict = dict()
    # counter = 1
    # for key, value in self.all_users.items():
    #   print('{}. {}'.format(counter, value.full_name))
    #   temp_user_dict[counter] = value
    #   counter += 1



# ----------------------------------------#
# ---------- Create Public Chirp ---------#
# ----------------------------------------#
  def create_public_chirp(self):
    '''
      This menu will show the user all the chirps, public and private. The user will then
      pick which chirp thread they want to chirp at.

    '''
    self.clear_the_page()
    print('{}'.format(self.current_user.full_name))

    print('Enter your full name')
    message = input('Public Chirp > ')

    # pass user_id into Chirp

    public_chirp = Chirp(message, self.current_user.user_id)
    print(public_chirp)
    self.all_chirps[public_chirp.chirp_id] = public_chirp
    self.serialize_data(self.all_chirps, self.chirps_filename)

    new_conversation = Conversation(public_chirp.chirp_id)
    self.all_conversations[new_conversation.conversation_id] = new_conversation
    self.serialize_data(self.all_conversations, self.conversations_filename)
    time.sleep(1)

    self.start_main_menu() # send the user back to the main menu


# ----------------------------------------#
# ---------- Create Private Chirp --------#
# ----------------------------------------#
  def create_private_chirp(self):
    '''
      This menu will show the user all the chirps, public and private. The user will then
      pick which chirp thread they want to chirp at.

    '''
    print('create private chirp lol')
    pass





# ----------------------------------------#
# ---------- Serialization Defs ----------#
# ----------------------------------------#
  def serialize_data(self, data, filename):
    ''' Serialize txt files '''
    # wb+ w/r in binday format
    with open(filename, 'wb+') as file:
      pickle.dump(data, file)


  def deserialize_data(self, filename):
    ''' Deserialize txt files '''
    # filename
    # rb+ r/w in binary format
    try:
      with open(filename, 'rb+') as file:
        data = pickle.load(file)
    except FileNotFoundError:
      data = {}
    return data






if __name__ == '__main__':
  birdyboard = Birdyboard()
  birdyboard.start_main_menu()
