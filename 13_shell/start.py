def MySort(numbers: list[int])->list[int]:
  return numbers


if __name__ == '__main__':
  import random
  numbers = [random.randint(1, 1000) for _ in range(10)]

  print(MySort(numbers))