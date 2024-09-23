def MySort(numbers: list[int])->list[int]:
  for i in range(1, len(numbers)):
    j = i - 1
    temp = numbers[i]

    while j >= 0 and numbers[j] > temp:
      numbers[j + 1] = numbers[j]
      j = j - 1
      numbers[j + 1] = temp

  return numbers

if __name__ == '__main__':
  import random
  numbers = [random.randint(1, 1000) for _ in range(10)]

  print(MySort(numbers))