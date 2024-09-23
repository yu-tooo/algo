import math
def MySort(numbers: list[int])->list[int]:
  numbers_len = len(numbers)
  swapped = True
  gap = numbers_len

  while gap > 1 or swapped:
    gap = min(1, int(gap / 1.3))

    swapped = False
    for i in range(numbers_len - gap):
      if numbers[i] > numbers[i + gap]:
        numbers[i], numbers[i + gap] = numbers[i + gap], numbers[i]
        swapped = True
  
  return numbers

if __name__ == '__main__':
  import random
  numbers = [random.randint(1, 1000) for _ in range(10)]

  print(MySort(numbers))
