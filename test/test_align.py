from clivia.text import align, puts

TEXT = \
'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quidem, quas ea ' +\
'accusantium esse. Perferendis minus quod unde eum sequi facilis vitae. ' +\
'Excepturi labore consequuntur repellendus cumque ea corporis. Ipsam soluta ' +\
'cumque a magni quas ratione nesciunt repellendus, assumenda temporibus ea ' +\
'inventore, dolores officia iste cupiditate laudantium. Dolorem neque ' +\
'deserunt amet?'
LEFT_REGULAR_TEXT = '''
Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quidem, quas ea
accusantium esse. Perferendis minus quod unde eum sequi facilis vitae. Excepturi
labore consequuntur repellendus cumque ea corporis. Ipsam soluta cumque a magni
quas ratione nesciunt repellendus, assumenda temporibus ea inventore, dolores
officia iste cupiditate laudantium. Dolorem neque deserunt amet?
'''.strip('\n')
LEFT_INDENT_TEXT = '''
   Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quidem, quas ea
   accusantium esse. Perferendis minus quod unde eum sequi facilis vitae.
   Excepturi labore consequuntur repellendus cumque ea corporis. Ipsam soluta
   cumque a magni quas ratione nesciunt repellendus, assumenda temporibus ea
   inventore, dolores officia iste cupiditate laudantium. Dolorem neque deserunt
   amet?
'''.strip('\n')
LEFT_HANGING_TEXT = '''
Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quidem, quas ea
   accusantium esse. Perferendis minus quod unde eum sequi facilis vitae.
   Excepturi labore consequuntur repellendus cumque ea corporis. Ipsam soluta
   cumque a magni quas ratione nesciunt repellendus, assumenda temporibus ea
   inventore, dolores officia iste cupiditate laudantium. Dolorem neque deserunt
   amet?
'''.strip('\n')
CENTER_REGULAR_TEXT = '''
   Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quidem, quas ea    
accusantium esse. Perferendis minus quod unde eum sequi facilis vitae. Excepturi
labore consequuntur repellendus cumque ea corporis. Ipsam soluta cumque a magni 
 quas ratione nesciunt repellendus, assumenda temporibus ea inventore, dolores  
        officia iste cupiditate laudantium. Dolorem neque deserunt amet?        
'''.strip('\n')
SPLIT_LEFT_STRING = 'apple pie'
SPLIT_RIGHT_STRING = 'spam bacon'
SPLIT_REGULAR_STRING = '''
apple pie                                                             spam bacon
'''.strip('\n')

def test_align_left_normal():
   assert align.left(TEXT, within=80) == LEFT_REGULAR_TEXT
   assert align.left(TEXT, indent=3, within=80) == LEFT_INDENT_TEXT
   assert align.left(TEXT, indent=3, hanging=True, within=80) == \
      LEFT_HANGING_TEXT

def test_align_left_context(capfd):
   with align.left(within=80):
      puts(TEXT)
   out, err = capfd.readouterr()
   assert out == LEFT_REGULAR_TEXT+'\n'
   with align.left(indent=3, within=80):
      puts(TEXT)
   out, err = capfd.readouterr()
   assert out == LEFT_INDENT_TEXT+'\n'
   with align.left(indent=3, hanging=True, within=80):
      puts(TEXT)
   out, err = capfd.readouterr()
   assert out == LEFT_HANGING_TEXT+'\n'
   puts(TEXT)
   out, err = capfd.readouterr()
   assert out == TEXT+'\n'

def test_align_center_normal():
   assert align.center(TEXT) == CENTER_REGULAR_TEXT

def test_align_center_context(capfd):
   with align.center(within=80):
      puts(TEXT)
      out, err = capfd.readouterr()
      assert out == CENTER_REGULAR_TEXT+'\n'
   puts(TEXT)
   out, err = capfd.readouterr()
   assert out == TEXT+'\n'

def test_align_split():
   assert align.split(SPLIT_LEFT_STRING, SPLIT_RIGHT_STRING, within=80) == \
      SPLIT_REGULAR_STRING
