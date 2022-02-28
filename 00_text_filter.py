import os


def text_filter(bName):
  with open(f'{bName}', 'r', encoding='utf8') as book :
    btxt = [line.replace('\n', ' ') for line in book]

  t = str()
  for line in btxt:
    for x in line:
      if (2431 < ord(x) < 2559) or ord(x) == 32:
        if (not 2533 < ord(x) < 2544) and (not ord(x) == 2551):
          t = t + x
  t_final = t.replace('   ', ' ').replace('  ', ' ')

  with open(f'text_only/text_only {bName}', 'w', encoding='utf8') as book :
    book.write(t_final)

def main():
  if os.path.isdir('text_only'):
    os.system("rm -fr 'text_only'")
  os.mkdir('text_only')

  for x in os.listdir():
    if x.endswith('.txt'):
      text_filter(x)

if __name__== "__main__":
   main()      
          