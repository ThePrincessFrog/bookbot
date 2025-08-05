def get_word_count(text):
  return len(text.split())

def get_character_counts(text):
  letter_obj = {}
  for letter in text.lower():
      letter_obj[letter] = letter_obj.get(letter, 0) + 1
  return letter_obj

def sort_character_counts(chars):
  char_arr = []
  for letter in chars:
    if letter.isalpha():
      char_arr.append({"char": letter, "count": chars[letter]})
  char_arr.sort(key=lambda x: x["char"])
  char_arr.sort(key=lambda x: x["count"], reverse=True)
  return char_arr
