from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

#Button need
reset_button = KeyboardButton('Сменить группу')
back_btn = KeyboardButton('Назад')
btn_back = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(back_btn)
#Group 1    
student_button = KeyboardButton('Я студент')
teacher_button = KeyboardButton('Я преподаватель')
button_who = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(student_button).add(teacher_button)
#Group 2
register_button = KeyboardButton('Регистрация')
button_register = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(register_button)
#Group 3
profile_button = KeyboardButton('Мой профиль')
help_button = KeyboardButton('Помощь')
setting_button = KeyboardButton('Настройки')
schedule_button = KeyboardButton('Получить расписание')
button_main = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(schedule_button).add(setting_button).add(profile_button).add(help_button)
#Group 4
go_to_main_button = KeyboardButton('Перейти в главное меню')
button_go_main = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(go_to_main_button)
#Group 5
today_button = KeyboardButton('Расписание на сегодня')
next_day_button = KeyboardButton('Расписание на завтра')
button_schedule_choise = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(today_button).add(next_day_button).add(back_btn)
#Group 6
time_set_button = KeyboardButton('Время уведомлений')
notify_switch_button = KeyboardButton('Вкл/Выкл уведомлений')
button_notify = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(time_set_button).add(notify_switch_button).add(reset_button).add(back_btn)
#Group 7

