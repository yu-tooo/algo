def MySort(numbers: list[int])->list[int]:
  for i in range(len(numbers) - 1):
    for j in range(len(numbers) - 1 - i):
      if numbers[j] > numbers[j + 1]:
        numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

  return numbers


if __name__ == '__main__':
  import random
  numbers = [random.randint(1, 1000) for _ in range(10)]

  print(MySort(numbers))