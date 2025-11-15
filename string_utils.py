def split_before_each_uppercases(formula):
    upper_index = []
    new_formula = []
    
    # find the index of the upper letters
    for i in range(len(formula)):
      if formula[i].isupper():
        upper_index.append(i)

    # slices
    if upper_index:
      for i in range(len(upper_index) - 1):
        new_word = formula[upper_index[i]:upper_index[i+1]]
        new_formula.append(new_word)

      # add the last one
      last_upper = upper_index[len(upper_index) - 1]
      new_word = formula[last_upper:]
      new_formula.append(new_word)
    elif formula:
      new_formula.append(formula)
    return new_formula


def split_at_first_digit(formula):
  count = 0
  for l in formula:
    count += 1
    if l.isdigit():
      letters = formula[:count - 1]
      digits = formula[count - 1:]
      return letters, int(digits_str)
  return formula, 1
