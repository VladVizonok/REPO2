from datetime import datetime, date, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    # Перевірка на пустий список
    if not users:
        return {}
    
    # Створюємо словник 
    birthday_list = defaultdict(list)
    interval = timedelta(days=0)

    while interval != timedelta(days=7):
        start_day = date.today() 

        #Якщо день запуску понеділок, скрипт почне працювати на 2 дні раніше, щоб перевірити чи є дні народження на вихідних які минули. 
        if start_day.weekday() == 0:
            start_day -= timedelta(days=2)

            day_number = (start_day + interval).strftime('%m %d')
            day_name = (start_day + interval).strftime('%A')

            for elem in users:
                if elem['birthday'].strftime('%m %d') == day_number:
                    birthday_list[day_name].append(elem['name'])
            interval += timedelta(days=1)
            
        else:
            day_number = (start_day + interval).strftime('%m %d')
            day_name = (start_day + interval).strftime('%A')

            for elem in users:
                if elem['birthday'].strftime('%m %d') == day_number:
                    birthday_list[day_name].append(elem['name'])
            interval += timedelta(days=1)
    
    #Перевірка на дні народження, що пройшли. Якщо так, то словник буде пустий.
    if birthday_list:
        #Переносимо дні народження з вихідних на понеділок та видаляємо пусті дні.
        birthday_list['Monday'].extend(birthday_list['Saturday'])
        birthday_list['Monday'].extend(birthday_list['Sunday'])
        birthday_list['Monday'].reverse() #Розвертаємо значення, щобдні народження понеділка йшли по порядку 
        del birthday_list['Saturday']
        del birthday_list['Sunday']
        if birthday_list['Monday'] == []:
            del birthday_list['Monday']

    return dict(birthday_list)
    
if __name__ == "__main__":
    users = [
    {"name": "Bill Gates", "birthday": datetime(1999, 1, 1).date()},
    {"name": "Steve Jobs", "birthday": datetime(2024, 1, 3).date()},
    {"name": "Mark Zuckerberg", "birthday": datetime(1929, 1, 4).date()},
    {"name": "Elon Musk", "birthday": datetime(1971, 1, 6).date()},
    {"name": "Jeff Bezos", "birthday": datetime(1964, 1, 8).date()},
    {"name": "Tim Cook", "birthday": datetime(1960, 1, 5).date()},
    {"name": "Satya Nadella", "birthday": datetime(1967, 1, 7).date()},
    {"name": "Larry Page", "birthday": datetime(1973, 1, 4).date()},
    {"name": "Sundar Pichai", "birthday": datetime(1972, 12, 31).date()},
    {"name": "Warren Buffett", "birthday": datetime(1930, 12, 30).date()},
]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
