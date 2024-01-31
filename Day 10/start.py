def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "Please a enter valid input"  
    
  f_name_formated = f_name.title()
  l_name_formated = l_name.title()
  
  return f"{f_name_formated} {l_name_formated}"

# print(format_name('eRiCK', 'sanChEZ'))
print(format_name(input('Enter your first name: '),input('Enter your last name: ') ))

