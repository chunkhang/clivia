# clivia.data
# Utility functions that deal with data

from . import constants

def load(path=constants.AWAKE_PATH):
   '''
   Read data file to return what is stored
   -> {str: str} - stored key, stored value
   -> {} - no data file / data file corrupted
   '''
   data = {}
   try:
      with open(path, 'r') as file:
         lines = file.readlines()
   # File does not exist
   except FileNotFoundError:
      pass
   else:
      try:
         for line in lines:
            key, value = line.split('=', 1)
            data[key] = value.strip('\n')
      # Invalid data format
      except ValueError:
         data = {}
   return data

def save(new_data, overwrite=False, path=constants.AWAKE_PATH):
   '''
   Overwrite or update what is stored in data file 
   '''
   def _write(data, path):
      with open(path, 'w') as file:  
         for key, value in data.items():
            file.write('{}={}\n'.format(key, value))      
   assert type(new_data) == dict
   existing_data = load(path)
   # Overwrite existing data / Write new data 
   if overwrite or existing_data == {}:
      _write(new_data, path=path)
   # Update existing data
   else:
      for key in new_data.keys():
         existing_data[key] = new_data[key]      
      _write(existing_data, path=path)   