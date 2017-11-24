# clivia.text.align
# Utility functions to align text

from contextlib import contextmanager

from .. import constants

TERMINAL_WIDTH = constants.TERMINAL_DEFAULT_SIZE[0]
ALIGN_CONTEXT = None

@contextmanager
def _align_context_manager():
   '''
   Context manager to manage align context
   '''
   try:
      yield
   finally:
      global ALIGN_CONTEXT
      ALIGN_CONTEXT = None

def _get_align_context():
   '''
   For core functions to access align context
   >> # Normal usage
   >> puts(left('abc', indent=3))
   >> # Context usage
   >> with left(indent='3'):
   >>    puts('abc')
   '''
   return ALIGN_CONTEXT

def left(string=None, indent=0, hanging=False, within=TERMINAL_WIDTH):
   '''
   Return a string inserted with appropriate newlines to left-align it
   |string string   |
   |string          |
   '''
   # Normal usage
   if string:
      lines = []
      words = string.split()
      line = ' '*(indent if not hanging else 0) + words[0]
      for i in range(1, len(words)):
         if len(line) + 1 + len(words[i]) <= within:
            line += ' ' + words[i]
         else:
            lines.append(line)
            line = ' '*indent + words[i]
      lines.append(line)
      return '\n'.join(lines)
   # Context usage
   else:
      global ALIGN_CONTEXT
      ALIGN_CONTEXT = {
         'function': 'left',
         'parameters': {'indent': indent, 'hanging': hanging, 'within': within}
      }
      return _align_context_manager()

def center(string=None, within=TERMINAL_WIDTH):
   '''
   Return a string inserted with appropriate newlines to center-align it
   |  string string |
   |     string     |
   '''
   # Normal usage
   if string:
      left_aligned_string = left(string, within=within)
      lines = left_aligned_string.split('\n')
      centered_lines = '\n'.join(map(lambda x: x.center(within), lines))
      return centered_lines
   # Context usage
   else:
      global ALIGN_CONTEXT
      ALIGN_CONTEXT = {
         'function': 'center',
         'parameters': {'within': within}
      }     
      return _align_context_manager()

def split(left_string, right_string, within=TERMINAL_WIDTH):
   '''
   Return a string inserted with the appropriate whitespace to split the two 
   strings given
   |string    string|
   '''
   formatted = ''
   formatted += left_string + right_string.rjust(within-len(left_string))
   return formatted