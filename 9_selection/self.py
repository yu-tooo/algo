def MySort(numbers: list[int])->list[int]:
  numbers_len = len(numbers)

  for i in range(numbers_len):
    min_index = i
    for j in range(i + 1, numbers_len):
      if numbers[min_index] > numbers[j]:
        min_index = j
      
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    
  return numbers



if __name__ == '__main__':
  import random
  numbers = [random.randint(1, 1000) for _ in range(10)]
  print("変更有り")
  print(MySort(numbers))