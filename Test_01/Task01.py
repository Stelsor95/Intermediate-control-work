#Процедура:
def format_seconds(seconds):
    days = seconds // 86400
    seconds -= days * 86400
    hours = seconds // 3600
    seconds -= hours * 3600
    minutes = seconds // 60
    seconds -= minutes * 60
    formatted = f'{days} days {hours} hours {minutes} minutes {seconds} seconds '
    return formatted

#Функция:
def format_seconds(seconds):
    days = seconds // 86400
    seconds -= days * 86400
    hours = seconds // 3600
    seconds -= hours * 3600
    minutes = seconds // 60
    seconds -= minutes * 60
    return f'{days} days {hours} hours {minutes} minutes {seconds} seconds '

seconds = int(input("Введите кол-во секунд: "))
formatted_seconds = format_seconds(seconds)
print(formatted_seconds)  # Output: '1 days 10 hours 17 minutes 36 seconds '