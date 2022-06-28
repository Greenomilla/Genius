
from sqlalchemy import false


letter_to_number = {
  "A": 1,
  "B": 3,
  "C": 3,
}

number_to_word = {
  1: "ONE",
  2: "TWO",
  3: "THREE",
  4: "FOUR",
  5: "FIVE",
  6: "SIX",
  7: "SEVEN",
  8: "EIGHT",
  9: "NINE",
}

# Calculate value of word by adding digit values
def find_value(input: string) -> int:
  value = 0
  for letter in input:
    value += letter_to_number[letter]
  return value

def find_if_number_has_equal_value(number: int) -> bool:
  for i in number_to_word:
    if i == number:
      break
  else: return false
  return True