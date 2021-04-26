def func_user(name, surname, b_year, city, email, tel):
    print(f"Имя - {name}, Фамилия - {surname}, год рождения - {b_year}, город проживания - {city}, email - {email}, телефон - {tel}")
func_user(name=input('Введите ваше имя: '), surname=input('Введите вашу фамилию: '),b_year=input('Введите ваш год рождения: '),city=input('Введите город проживания: '),email=input('Введите адрес вашей электронной почты: '), tel=input('Введите ваш телефон: '))
