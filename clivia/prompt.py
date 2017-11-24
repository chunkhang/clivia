# clivia.prompt
# Utility functions to prompt for responses

from getpass import getpass

def credentials(
   username_prompt='Username: ',
   valid_username=lambda x: x != '',
   invalid_username_message='Invalid username', 
   password_prompt='Password: ', 
   valid_password=lambda x: x != '',
   invalid_password_message='Invalid password', 
   confirm_password=False,
   confirm_password_prompt='Confirm: ',
   confirm_password_invalid_message='Passwords do not match'):
   '''
   -> (str, str) - username, password
   '''
   while True:
      username = input(username_prompt)
      if not valid_username(username):
         print(invalid_username_message)
      else:
         break
   while True:
      password = getpass(password_prompt)
      if not valid_password(password):
         print(invalid_password_message)
      else:
         if confirm_password:
            if password != getpass(confirm_password_prompt):
               print(confirm_password_invalid_message)
            else:
               break
         else:
            break
   return (username, password)

def yes_no(prompt, invalid_message='Invalid response'):
   '''
   -> True - yes
   -> False - no
   '''
   while True:
      response = input('{} [y/n]: '.format(prompt)).lower()
      if response == 'y':
         return True
      elif response == 'n':
         return False
      else:
         print(invalid_message)
         
