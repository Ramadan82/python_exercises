def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return(format_name(input("what is your first name?"), input("what is your last name?")))
    formatted_l_name = l_name.title()
    formatted_f_name = f_name.title()

    return f"{formatted_f_name} {formatted_l_name}"


# formatted_string = format_name("angela", "ANGELA")
# print(formatted_string)
print(format_name(input("what is your first name?"), input("what is your lat name?")))
