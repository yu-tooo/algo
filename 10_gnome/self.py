def MySort(numbers: list[int])->list[int]:
  numbers_len = len(numbers)
  index = 0
  while index < numbers_len:
    if index == 0:
      index += 1
    if numbers[index - 1] <= numbers[index]:
      index += 1
    else:
      numbers[index - 1], numbers[index] = numbers[index], numbers[index - 1]
      index -= 1
  return numbers

if __name__ == '__main__':
  import random
  numbers = [random.randint(1, 1000) for _ in range(10)]

  
  print(MySort(numbers))