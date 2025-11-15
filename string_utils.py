def split_before_each_uppercases(formula):
    pass # Replace the `pass` with your code


def split_at_first_digit(formula):
  count = 0
  for l in formula:
    count += 1
    if l.isdigit():
      letters = formula[:count - 1]
      digits = formula[count - 1:]
      return letters, int(digits_str)
  return formula, 1
