total_seconds = int(input("Введите количество секунд: "))
seconds_in_day = 24 * 60 * 60
seconds_in_hour = 60 * 60
seconds_in_minute = 60
days = total_seconds // seconds_in_day
remaining_seconds = total_seconds % seconds_in_day
hours = remaining_seconds // seconds_in_hour
remaining_seconds = remaining_seconds % seconds_in_hour
minutes = remaining_seconds // seconds_in_minute
seconds = remaining_seconds % seconds_in_minute
if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
    day_word = "дня"
else:
    day_word = "дней"
formatted_time = f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
print(formatted_time)
