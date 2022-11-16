def main():
  weight = int(input("Enter weight in kilograms:"))
  length = int(input("Enter length in centimeters:"))
  width = int(input("Enter width in centimeters:"))
  height = int(input("Enter height in centimeters:"))
  dimensions = length * width * height
  if weight >27 and dimensions >100000:
    print("Too heavy and Too large")
  elif weight >27:
    print("Too heavy")
  elif dimensions >100000:
    print("Too large")
  
  pass


if __name__ == "__main__":
  main()