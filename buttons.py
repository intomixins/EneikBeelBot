from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

basic_questions = InlineKeyboardMarkup()
basic_question1 = InlineKeyboardButton(text='Что такое BEEL?', callback_data='basic_answer1')
basic_question2 = InlineKeyboardButton(text='Какие возможности предоставляет BEEL?',
                                       callback_data='basic_answer2')
basic_question3 = InlineKeyboardButton(text='Какие типы бизнесов могут воспользоваться системой BEEL?',
                                       callback_data='basic_answer3')
basic_question4 = InlineKeyboardButton(text='Каково преимущество удобной кастомизации BEEL?',
                                       callback_data='basic_answer4')
basic_question5 = InlineKeyboardButton(text='Каковы условия оплаты за систему BEEL?',
                                       callback_data='basic_answer5')
basic_question6 = InlineKeyboardButton(text='Какая поддержка предоставляется после настройки системы?',
                                       callback_data='basic_answer6')
basic_question7 = InlineKeyboardButton(text='Как я могу начать использовать систему BEEL?',
                                       callback_data='basic_answer7')
basic_question8 = InlineKeyboardButton(text='Заказать BEEL для бизнеса',
                                       callback_data='basic_answer8')
basic_questions.row(basic_question1)
basic_questions.row(basic_question2)
basic_questions.row(basic_question3)
basic_questions.row(basic_question4)
basic_questions.row(basic_question5)
basic_questions.row(basic_question6)
basic_questions.row(basic_question7)
basic_questions.row(basic_question8)

question_options2 = InlineKeyboardMarkup()
option2p1 = InlineKeyboardButton(text='Бронированиe мест', callback_data='option2p1')
option2p2 = InlineKeyboardButton(text='Мероприятия с местами', callback_data='option2p2')
option2p3 = InlineKeyboardButton(text='Мероприятия без мест', callback_data='option2p3')
option2p4 = InlineKeyboardButton(text='Статистика', callback_data='option2p4')
option2p5 = InlineKeyboardButton(text='Промокоды, акции', callback_data='option2p5')
back = InlineKeyboardButton(text='Другие вопросы', callback_data='back')
question_options2.row(option2p1)
question_options2.row(option2p2)
question_options2.row(option2p3)
question_options2.row(option2p4)
question_options2.row(option2p5)
question_options2.row(back)

question_options3 = InlineKeyboardMarkup()
option3p1 = InlineKeyboardButton(text='Ресторан', callback_data='option3p1')
option3p2 = InlineKeyboardButton(text='Отель', callback_data='option3p2')
option3p3 = InlineKeyboardButton(text='Коворкинг', callback_data='option3p3')
option3p4 = InlineKeyboardButton(text='Кинотеатр / театр / концертный зал', callback_data='option3p4')
option3p5 = InlineKeyboardButton(text='Салон красоты / здоровья', callback_data='option3p5')
option3p6 = InlineKeyboardButton(text='Сервисы клининга / сантехнических услуг', callback_data='option3p6')
option3p7 = InlineKeyboardButton(text='Другое', callback_data='option3p7')
back = InlineKeyboardButton(text='Другие вопросы', callback_data='back')
question_options3.row(option3p1)
question_options3.row(option3p2)
question_options3.row(option3p3)
question_options3.row(option3p4)
question_options3.row(option3p5)
question_options3.row(option3p6)
question_options3.row(option3p7)
question_options3.row(back)

another = InlineKeyboardMarkup()
discuss = InlineKeyboardButton(text='Хочу обсудить', callback_data='discuss')
another.row(discuss)
another.row(back)

question_options5 = InlineKeyboardMarkup()
question_options5.row(discuss)
question_options5.row(basic_question7)


question_options7 = InlineKeyboardMarkup()
chat = InlineKeyboardButton(text='Чатинг', callback_data='chat')
call = InlineKeyboardButton(text='Звонок', callback_data='call')
meeting = InlineKeyboardButton(text='Личная встреча в Грузии или встреча с представителями',
                               callback_data='meeting')
question_options7.row(chat)
question_options7.row(call)
question_options7.row(meeting)

chat_options = InlineKeyboardMarkup()
chat_yes = InlineKeyboardButton(text='Да', callback_data='chat_yes')
chat_no = InlineKeyboardButton(text='Нет', callback_data='chat_no')
chat_options.row(chat_yes)
chat_options.row(chat_no)
chat_options.row(back)

chat_no_options = InlineKeyboardMarkup()
chat_no_options.row(basic_question7)
chat_no_options.row(chat_yes)
