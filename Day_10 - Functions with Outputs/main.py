# # Function with Outputs

# def format_name(f_name, l_name):

#     print(f_name.title())
#     print(l_name.title())

# format_name("KANG", "Chiaw Na")



# def format_name(f_name, l_name):

#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()

#     print(f"My name is {formated_f_name} {formated_l_name}.")

# format_name("KANG", "chiaw na")



# def format_name(f_name, l_name):

#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()

#     return f"My name is {formated_f_name} {formated_l_name}."

# print(format_name("KANG", "chiaw na"))



# # multiple return values

# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs."
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"Result: {formated_f_name} {formated_l_name}"

# print(format_name(input("First name: "), input("Last name: ")))

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
# TODO: Add more code here 👇
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  if month == 2 and is_leap(year):
    return 29
  else:
    return month_days[month-1]

  
#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)
