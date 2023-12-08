puzzle_input = open("input.txt").read().strip().split("\n")
sample_a = open("sample_a.txt").read().strip().split("\n")
sample_b = open("sample_b.txt").read().strip().split("\n")

def solve_a(file):
  total = 0

  for line in file:
    numbers = [character for character in line if character in '0123456789']

    total += int(numbers[0] + numbers[-1])
  
  return total

assert solve_a(sample_a) == 142

print(f'Part A: {solve_a(puzzle_input)}')

def solve_b(file):
  total = 0

  words = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
  }

  for line in file:
    digits = []
    for index, character in enumerate(line):
      if character in '0123456789':
        digits.append(character)
      else:
        for word in words:
          if line[index:index+len(word)] == word:
            digits.append(words[word])


    total += int(digits[0] + digits[-1])
  
  return total

assert solve_b(sample_b) == 281

print(f'Part B: {solve_b(puzzle_input)}')
