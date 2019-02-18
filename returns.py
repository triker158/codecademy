def calculate_age(current_year, birth_year):
  age = current_year - birth_year
  return age


def get_boundaries(target, margin):
  low_limit = target - margin
  high_limit = target + margin
  return low_limit, high_limit


# age calc
my_age = calculate_age(2018, 1993)
dads_age = calculate_age(2018, 1953)

print("I am " + str(my_age) + " years old and my dad is " + str(dads_age) + " years old\n")

# multiple return values
low, high = get_boundaries(100, 20)
print("Low limit: " + str(low) + ", high limit: " + str(high) + "\n")
