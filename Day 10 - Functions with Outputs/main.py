# Function with Outputs

def format_name(f_name, l_name):

    print(f_name.title())
    print(l_name.title())

format_name("KANG", "Chiaw Na")



def format_name(f_name, l_name):

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    print(f"My name is {formated_f_name} {formated_l_name}.")

format_name("KANG", "chiaw na")



def format_name(f_name, l_name):

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"My name is {formated_f_name} {formated_l_name}."

print(format_name("KANG", "chiaw na"))