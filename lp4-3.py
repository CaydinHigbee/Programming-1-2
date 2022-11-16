def main():
  eggs = int(input("Enter # of eggs purchased: "))
  dozens = eggs // 12
  remainder = eggs % 12
  price = 0.0

  if dozens >= 0 and dozens < 4:
    price = 0.50
  elif dozens >= 4 and dozens < 6:
    price = 0.45
  elif dozens >= 6 and dozens < 11:
    price = 0.40
  elif dozens >= 11:
    price = 0.35
  else:
    print("Invalid number of dozens")
  cost = price * dozens + (remainder * (price * 1.0 * 12))
  print("price per egg is $" + str(price))
  print("Total cost is $" + str(round(cost, 2)))
  pass


if __name__ == "__main__":
  main()