def CocktailSort(numbers: list[int])->list[int]:
  numbers_len = len(numbers)
  start = 0
  end = numbers_len - 1
  swap = True

  while swap:
    swap = False
    for i in range(start, end):
      if numbers[i] > numbers[i + 1]:
        numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
        swap = True
    
    if not swap:
      break
    
    end -= 1
    swap = False

    for j in range(end - 1, start - 1, -1):
      if numbers[j] > numbers[j + 1]:
        numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        swap = True

    start += 1
  
  return numbers

  

if __name__ == "__main__":
  import random
  numbers = [random.randint(1, 1000) for _ in range(1, 10)]

  print(CocktailSort(numbers))