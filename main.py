import sys
from stats import get_word_count, get_character_counts, sort_character_counts

def get_book_text(filepath):
  return filepath.read()

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  with open(sys.argv[1], "r") as frankenstein:
    text = get_book_text(frankenstein)
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {sys.argv[1]}...")
  print("----------- Word Count ----------")
  print(f"Found {get_word_count(text)} total words")
  print("--------- Character Count -------")
  char_arr = sort_character_counts(get_character_counts(text))
  for char in char_arr:
    print(f"{char['char']}: {char['count']}")
  print("============= END ===============")

main()