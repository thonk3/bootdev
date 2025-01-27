
file_contents = ""

frankenstein_path = "./books/frankenstein.txt"

alphabet = list("abcdefghijklmnopqrstuvwxyz")

# l9 count words
def count_words(file):
  return len(file.split())

def count_chars(file):
  char_dir = {}
  
  for c in list(file.lower()):
    if c.lower() not in char_dir:
      char_dir[c] = 1
    else:
      char_dir[c] += 1
  return char_dir

def count_alphas(file):
  all_char_dir = count_chars(file)
  char_dir = {}
  
  for c in all_char_dir:
    if c in alphabet:
      char_dir[c] = all_char_dir[c]
  return char_dir

def print_title(file_path):
  print(f"--- Begin report of {file_path[2:]} ---")
  pass

def print_word_count(file):
  print(f"{count_words(file)} words found in the document")
  pass


def print_char_count(file):
  char_counts = count_alphas(file)
  for c in char_counts:
    print(f"The '{c}' character was found {char_counts[c]} times")
    # The 'e' character was found 46043 times
    pass

def print_end():
  print("--- End report ---")

def print_report(file, file_path):
  print_title(file_path)
  print_word_count(file)
  print()
  print_char_count(file)
  print_end()
  pass

def __main__():
  with open(frankenstein_path) as f:
    file_contents = f.read()
  
  print_report(file_contents, frankenstein_path)
  pass


  
__main__()