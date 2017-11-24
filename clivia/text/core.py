# clivia.text.core
# Core functions for text module

import sys

from .align import _get_align_context, left, center

def puts(string='', newline=True):
   printable = '{}{}'.format(string, '\n' if newline else '')
   align_context = _get_align_context()
   if align_context:
      function = align_context['function']
      parameters = align_context['parameters']
      exec('print({}({}, {}))'.format(
         function,
         'string={}'.format(repr(printable)),
         ', '.join(map(
            lambda x: '{}={}'.format(x, repr(parameters[x])), 
            parameters.keys()))))
   else:
      print(printable, end='')