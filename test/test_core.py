from clivia.text import puts

def test_puts_newline(capfd):
   string = 'Cat is cute'
   puts(string)
   out, err = capfd.readouterr()
   assert out == string+'\n'

def test_puts_no_newline(capfd):
   string = 'Dogs are evil'
   puts(string, newline=False)
   out, err = capfd.readouterr()
   assert out == string