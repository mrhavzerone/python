import shutil


class Program():
    user_data = {
        'first_name': 'Abraham',
        'last_name': 'Abramovich',
        'sex': 'male',
        'birth_date': '05.05.1955',
        'phone_number': '+380934353234'
    }

    # this function return your text width space between
    def centred_text(text):
        terminal_width = shutil.get_terminal_size().columns
        padding = (terminal_width - len(text)) // 2
        centred_text = ' ' * padding + text
        return centred_text

    # This function return text in sqare formation by input scale
    def sqare_dot(modifier):
        text = Program.centred_text(('_ '*modifier)+'\n')
        return text*modifier

    # This function print data in dictionary
    def print_user_data():
        for key, value in Program.user_data.items():
            print(Program.centred_text(f"{key}: {value}"))


print(Program.sqare_dot(
      int(
          input(
              Program.centred_text(
                  "Hello, you can type any number: "),
          )
      )
      )
      )
print(Program.centred_text("And now, i have all information abot you"))
print(Program.centred_text("Thank you!"))
Program.print_user_data()
