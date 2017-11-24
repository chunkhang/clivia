# clivia.arguments
# Utility functions related to arguments

import sys

class Arguments(object):
   '''
   Arguments manager
   '''
   def __init__(self):
      self._all_arguments = sys.argv[1:]

   @property
   def command(self):
      '''
      Return command provided
      '''
      try:         
         return self._all_arguments[0]
      except IndexError:
         return None

   @property
   def args(self):
      '''
      Return list of arguments provided
      '''
      return self._all_arguments[1:]
