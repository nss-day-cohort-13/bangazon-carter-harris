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
    except EOFError:
      self.all_users = {}
    try:
      self.all_chirps = self.deserialize_data(self.chirps_filename)
    except EOFError:
      self.all_chirps = {}
    try:
      self.all_conversations = self.deserialize_data(self.conversations_filename)
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
      self.current_user
      print('{}. {}'.format(counter, value.full_name))
      temp_user_dict[counter] = value
      counter += 1

    selected_user = int(input('> ')) # users input for running the for loop below
    for key, value in temp_user_dict.items():
      if key == selected_user:
        self.current_user = value

    self.start_main_menu()







# ----------------------------------------#
# ------------- View Chirps --------------#
# ----------------------------------------#
  def view_chirps(self):
    '''
      This menu will show the user all the chirps, public and private. The user will then
      pick which chirp thread they want to chirp at.
    '''
    self.clear_the_page()


    # make a temp dict to store print conversations first index
    temp_convo_dict = dict()
    counter = 1
    for key, conversation in self.all_conversations.items():
      print('{}. {}: {}'.format(counter, self.all_users[self.all_chirps[conversation.chirp_list[0]].author].full_name, self.all_chirps[conversation.chirp_list[0]].message))
      temp_convo_dict[counter] = conversation # converstation
      counter += 1


    # take user selection and loop over temp convo dict to grab their choice
    selected_convo = int(input('Select a chirp > ')) # users input for running the for loop below
    for key, value in temp_convo_dict.items():
      if key == selected_convo:
        for chirp_key_id in value.chirp_list:
          print('{}: {}'.format(self.all_users[self.all_chirps[chirp_key_id].author].full_name, self.all_chirps[chirp_key_id].message))


    # user selects to reply to a chirp from the
    print('1. Reply')
    # user selects to view chirps again
    print('2. Back')
    # send user back to main menu
    print('3. Main Menu')

    choice = input('> ')
    if choice == '1':
      self.reply_to_chirp()
    elif choice == '2':
      self.view_chirps()
    elif choice == '3':
      self.start_main_menu()
    else:
      print('Please select one of the three choices')






# ----------------------------------------#
# ---------- Create Public Chirp ---------#
# ----------------------------------------#
  def create_public_chirp(self):
    '''
      This menu will show the user all the chirps, public and private. The user will then
      pick which chirp thread they want to chirp at.

    '''
    self.clear_the_page()
    print('{}'.format(self.current_user.full_name)) # show users name

    message = input('Public Chirp > ')

    public_chirp = Chirp(message, self.current_user.user_id)
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
    self.clear_the_page()
    print('{}'.format(self.current_user.full_name)) # show users name

    message = input('Private Chirp > ')

    receiver = self.select_users();

    private_chirp = Chirp(message, self.current_user.user_id, private=True, receiver_id=None)
    self.all_chirps[private_chirp.chirp_id] = private_chirp
    self.serialize_data(self.all_chirps, self.chirps_filename)

    print('Chirp id being passed into Convo private', private_chirp.chirp_id)
    new_conversation = Conversation(private_chirp.chirp_id)
    self.all_conversations[new_conversation.conversation_id] = new_conversation
    self.serialize_data(self.all_conversations, self.conversations_filename)
    time.sleep(1)

    self.start_main_menu() # send the user back to the main menu






# ----------------------------------------#
# ----------- Reply to a chirp -----------#
# ----------------------------------------#
  def reply_to_chirp(self):
    reply = input('Your reply > ')
    pass

    # add the reply to the chirp list that corresponds to the converstation
    # and dont








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
