# ============================================================
#  TEMPERATURE CONVERTER
#  Converts a temperature across Celsius, Fahrenheit & Kelvin
#  Concepts: variables, int, float, str, list, tuple, bool,
#  print (sep / end), arithmetic, comparison, logical ops
# ============================================================

# ---------- INPUT ----------

celsius = 100.0             # float  — the temperature to convert
scale_input = "Celsius"     # string — the starting scale


# ---------- SCALE INFO (tuple — fixed, never changes) ----------

valid_scales = ("Celsius", "Fahrenheit", "Kelvin")


# ---------- CONVERSION FORMULAS (arithmetic operators) ----------

# From Celsius
fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

# ---------- SCALE SYMBOLS (list — ordered, indexable) ----------

symbols = ["°C", "°F", "K"]

# ---------- BOOLEAN FLAGS (comparison + logical operators) ----------

is_valid_scale = scale_input == "Celsius"           # comparison ==
is_boiling = celsius >= 100                         # comparison >=
is_freezing = celsius <= 0                          # comparison <=
is_body_temp = celsius >= 36 and celsius <= 37      # logical and
is_extreme = celsius > 200 or celsius < -50         # logical or
is_room_temp = not is_boiling and not is_freezing   # logical not


# ---------- OUTPUT ----------

print("=" * 45)
print("       TEMPERATURE CONVERTER")
print("=" * 45)

print("Input     :", celsius, symbols[0], sep=" ")
print("Scale     :", scale_input)
print("Valid     :", is_valid_scale)

print("-" * 45)
print("RESULTS")
print("-" * 45)

# sep= to align scale name and value on one line
print("Celsius    :", celsius, symbols[0], sep=" ")
print("Fahrenheit :", fahrenheit, symbols[1], sep=" ")
print("Kelvin     :", kelvin, symbols[2], sep=" ")

print("-" * 45)
print("ANALYSIS")
print("-" * 45)

# end= to print label and value on the same line
print("Is boiling point  : ", end="")
print(is_boiling)

print("Is freezing point : ", end="")
print(is_freezing)

print("Is body temp      : ", end="")
print(is_body_temp)

print("Is room temp      : ", end="")
print(is_room_temp)

print("Is extreme temp   : ", end="")
print(is_extreme)

print("=" * 45)
print("Scales available  :", valid_scales[0], valid_scales[1], valid_scales[2], sep=" | ")
print("=" * 45)