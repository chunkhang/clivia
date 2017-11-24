# Clivia [![PyPI](https://img.shields.io/pypi/v/clivia.svg)](https://pypi.python.org/pypi/clivia) [![Travis](https://img.shields.io/travis/chunkhang/clivia.svg)](https://travis-ci.org/chunkhang/clivia)

> A library for simple CLI development in Python

<img src="https://user-images.githubusercontent.com/12708862/33216248-0921be20-d16e-11e7-8b29-77b90170c8ce.jpg" alt="Hourglass" width=400/><br/>

## Installation

```
$ pip install clivia
```
**Python Versions** <br/>
3.3 | 3.4 | 3.5 | 3.6

## Usage

### clivia.text
#### Printing
```python
from clivia.text import puts

# puts(string='', newline=True)
puts('Hello world')
puts()
puts('Bye ', newline=False)
puts('world')
```
```
Hello world

Bye world
```
#### Aligning
```python
from clivia.text import puts, align

string = 'What a wonderful world!'

# align.left(string=None, indent=0, hanging=False, within=80)
puts('+'+'-'*9+'+'+'-'*68+'+')
puts(align.left(string))
puts()
puts(align.left(string, within=10)) 
puts()
puts(align.left(string, indent=3))
puts()
puts(align.left(string, indent=1, hanging=True, within=10))
puts()
# Alternatively, use 'with' for multiple puts
with align.left(indent=3):
   puts(string)
   puts(string)

# align.center(string=None, within=80)
puts('+'+'-'*9+'+'+'-'*68+'+')
puts(align.center(string))
puts()
puts(align.center(string, within=10))
puts()
# Alternatively, use 'with' for multiple puts
with align.center():
   puts(string)
   puts(string)

# align.split(left_string, right_string, within=80)
puts('+'+'-'*9+'+'+'-'*68+'+')
puts(align.split('apple', 'pie'))
puts()
puts(align.split('apple', 'pie', within=10))

```
```
+---------+--------------------------------------------------------------------+
What a wonderful world!

What a
wonderful
world!

   What a wonderful world!

What a
 wonderful
 world!

   What a wonderful world!
   What a wonderful world!
+---------+--------------------------------------------------------------------+
                            What a wonderful world!

  What a
wonderful
  world!

                            What a wonderful world!
                            What a wonderful world!
+---------+--------------------------------------------------------------------+
apple                                                                        pie

apple  pie
```

### clivia.prompt
#### Coming soon

### clivia.terminal
#### Coming soon

### clivia.data
#### Coming soon

### clivia.arguments
#### Coming soon

## Unlicense

```
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org>
```

## Contact

Feel free to report bugs or suggest features <br/>
**[Marcus Mu](http://marcusmu.me)** | chunkhang@gmail.com