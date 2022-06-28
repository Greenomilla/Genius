
letter_to_number = {
  "A": 1,
  "B": 3,
  "C": 3,
}

# Calculate value of word by adding digit values
def find_value(input: string) -> int:
  value = 0
  for letter in input:
    value += letter_to_number[letter]
  return value