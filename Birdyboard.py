
class Birdyboard():


  def show_menu(self):
    # Command line menu for Birdyboard
    print(' ~ Tweet tweet, welcom to BirdyBoard, plz select from the following menu ~ ')
    print('')
    print('1. New User Account')
    print('2. Select User')
    print('')
    print('6. Exit')
    choice = input('> ')

    try:
      # Checks to make sure the user does not type in a negaitive or higher than 4 number
      if int(choice) > 0 and int(choice) < 7:


        if choice == '1':
          print('number one')
          print('Enter full name')
          full_name = input('> ')

          print('Enter screen name')
          screen_name = input('> ')

          # user = '{} {}'.format(full_name + screen_name)
          print('Welcome {user}')
          print('3. View Chirps')
          print('4. Public Chirp')
          print('5. Private Chirp')


        if choice == '2':
          print('number two')
          print('3. View Chirps')
          print('4. Public Chirp')
          print('5. Private Chirp')

        if choice == '3':
          print('number three')
          print('3. View Chirps')
          print('4. Public Chirp')
          print('5. Private Chirp')

        if choice == '4':
          print('number four')
          print('3. View Chirps')
          print('4. Public Chirp')
          print('5. Private Chirp')

        if choice == '5':
          print('number five')
          print('3. View Chirps')
          print('4. Public Chirp')
          print('5. Private Chirp')

        if choice == '6':
          print('number six? you wanna quit?')


    except:
      self.show_menu()


if __name__ == "__main__":
  chirp = Birdyboard()
  chirp.show_menu()