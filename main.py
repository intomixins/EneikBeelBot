import os

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

from answers import (
    another_answer,
    basic_answer1_text,
    basic_answer2_text,
    basic_answer3_text,
    basic_answer4_text,
    basic_answer5_text,
    basic_answer6_text,
    basic_answer7_text,
    call_answer,
    chat_answer,
    chat_no_answer,
    chat_yes_answer,
    discuss_answer,
    meeting_answer,
    option2p1_answer,
    option2p1_photos,
    option2p2_answer,
    option2p2_photos,
    option2p3_answer,
    option2p3_photos,
    option2p4_answer,
    option2p4_photos,
    option2p5_answer,
    option2p5_photos,
    option3p1_answer,
    option3p2_answer,
    option3p3_answer,
    option3p3_photos,
    option3p4_answer,
    option3p5_answer,
    option3p6_answer,
    option3p6_photos,
    option3p7_answer,
)

from buttons import (
    another,
    basic_questions,
    chat_no_options,
    chat_options,
    question_options2,
    question_options3,
    question_options5,
    question_options7,

)

from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.environ.get('BOT_TOKEN'))

dp = Dispatcher(bot)

ADMIN_ID = 826750345


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message) -> None:
    """ приветственное сообщение """
    await bot.send_message(message.chat.id, 'Добро пожаловать! Выберите вопрос или задайте свой.',
                           reply_markup=basic_questions)
    

@dp.message_handler(commands='id')
async def get_user_id(message: types.Message) -> None:
    await bot.send(ADMIN_ID, f'id пользователя {message.from_user.id}')


@dp.callback_query_handler(text='back')
async def back(call: types.CallbackQuery) -> None:
    """ возврат к основным вопросам """
    await call.message.answer('Добро пожаловать! Выберите вопрос или задайте свой.',
                              reply_markup=basic_questions)


@dp.callback_query_handler(text='basic_answer1')
async def basic_answer1(call: types.CallbackQuery) -> None:
    """ ответ на первой вопрос """
    await call.message.answer(text=basic_answer1_text, reply_markup=basic_questions)


@dp.callback_query_handler(text='basic_answer2')
async def basic_answer2(call: types.CallbackQuery) -> None:
    """ ответ на второй вопрос """
    await call.message.answer(text=basic_answer2_text, reply_markup=question_options2)


@dp.callback_query_handler(text='option2p1')
async def option2p1(call: types.CallbackQuery):
    """ ответ на 1 подпункт 2 сообщения """
    await bot.send_media_group(call.message.chat.id, media=option2p1_photos)
    await call.message.answer(text=option2p1_answer, reply_markup=question_options2,
                              parse_mode='html')


@dp.callback_query_handler(text='option2p2')
async def option2p2(call: types.CallbackQuery):
    """ ответ на 2 подпункт 2 сообщения """
    await bot.send_media_group(call.message.chat.id, media=option2p2_photos)
    await call.message.answer(text=option2p2_answer, reply_markup=question_options2,
                              parse_mode='html')


@dp.callback_query_handler(text='option2p3')
async def option2p3(call: types.CallbackQuery):
    """ ответ на 3 подпункт 2 сообщения """
    await bot.send_media_group(call.message.chat.id, media=option2p3_photos)
    await call.message.answer(text=option2p3_answer, reply_markup=question_options2,
                              parse_mode='html')


@dp.callback_query_handler(text='option2p4')
async def option2p4(call: types.CallbackQuery):
    """ ответ на 4 подпункт 2 сообщения """
    await bot.send_media_group(call.message.chat.id, media=option2p4_photos)
    await call.message.answer(text=option2p4_answer, reply_markup=question_options2,
                              parse_mode='html')


@dp.callback_query_handler(text='option2p5')
async def option2p5(call: types.CallbackQuery):
    """ ответ на 5 подпункт 2 сообщения """
    await bot.send_media_group(call.message.chat.id, media=option2p5_photos)
    await call.message.answer(text=option2p5_answer, reply_markup=question_options2,
                              parse_mode='html')


@dp.callback_query_handler(text='basic_answer3')
async def basic_answer3(call: types.CallbackQuery) -> None:
    """ ответ на 3 вопрос """
    await call.message.answer(text=basic_answer3_text, reply_markup=question_options3)


@dp.callback_query_handler(text='option3p1')
async def option3p1(call: types.CallbackQuery) -> None:
    """ ответ на 1 подпункт 3 сообщения """
    await call.message.answer(text=option3p1_answer, reply_markup=question_options3,
                              parse_mode='html')


@dp.callback_query_handler(text='option3p2')
async def option3p2(call: types.CallbackQuery) -> None:
    """ ответ на 2 подпункт 3 сообщения """
    await call.message.answer(text=option3p2_answer, reply_markup=question_options3,
                              parse_mode='html')


@dp.callback_query_handler(text='option3p3')
async def option3p3(call: types.CallbackQuery) -> None:
    """ ответ на 3 подпункт 3 сообщения """
    await bot.send_media_group(call.message.chat.id, media=option3p3_photos)
    await call.message.answer(text=option3p3_answer, reply_markup=question_options3,
                              parse_mode='html')


@dp.callback_query_handler(text='option3p4')
async def option3p4(call: types.CallbackQuery) -> None:
    """ ответ на 4 подпункт 3 сообщения """
    await call.message.answer(text=option3p4_answer, reply_markup=question_options3,
                              parse_mode='html')


@dp.callback_query_handler(text='option3p5')
async def option3p5(call: types.CallbackQuery) -> None:
    """ ответ на 5 подпункт 3 сообщения """
    await call.message.answer(text=option3p5_answer, reply_markup=question_options3,
                              parse_mode='html')


@dp.callback_query_handler(text='option3p6')
async def option3p6(call: types.CallbackQuery) -> None:
    """ ответ на 6 подпункт 3 сообщения """
    await bot.send_media_group(call.message.chat.id, media=option3p6_photos)
    await call.message.answer(text=option3p6_answer, reply_markup=question_options3,
                              parse_mode='html')


@dp.callback_query_handler(text='option3p7')
async def option3p7(call: types.CallbackQuery) -> None:
    """ ответ на 7 подпункт 3 сообщения """
    await call.message.answer(text=option3p7_answer, reply_markup=another,
                              parse_mode='html')


@dp.callback_query_handler(text='discuss')
async def discuss(call: types.CallbackQuery) -> None:
    """ отправка сообщения менеждеру, если клиент выбрал другое """
    await bot.send_message(chat_id=ADMIN_ID, text=f'{discuss_answer}, user=@{call.from_user.username}')
    await call.message.answer(text=another_answer, reply_markup=basic_questions)


@dp.message_handler()
async def area(message: types.Message) -> None:
    await bot.send_message(chat_id=ADMIN_ID,
                           text=f'Человечек пообщаться хочет {message.text}, user=@{message.from_user.username}')


@dp.callback_query_handler(text='basic_answer4')
async def basic_answer4(call: types.CallbackQuery) -> None:
    """ ответ на 4 вопрос """
    await call.message.answer(text=basic_answer4_text, reply_markup=question_options3)


@dp.callback_query_handler(text='basic_answer5')
async def basic_answer5(call: types.CallbackQuery) -> None:
    """ ответ на 5 вопрос """
    await call.message.answer(text=basic_answer5_text, reply_markup=question_options5)


@dp.callback_query_handler(text='basic_answer6')
async def basic_answer6(call: types.CallbackQuery) -> None:
    """ ответ на 6 вопрос """
    await call.message.answer(text=basic_answer6_text, reply_markup=another)


@dp.callback_query_handler(text='basic_answer7')
async def basic_answer7(call: types.CallbackQuery) -> None:
    """ ответ на 7 вопрос """
    await call.message.answer(text=basic_answer7_text, reply_markup=question_options7, parse_mode='html')


@dp.callback_query_handler(text='chat')
async def chat(call: types.CallbackQuery) -> None:
    """ выбор варианта чатинг """
    await call.message.answer(text=chat_answer, reply_markup=chat_options,
                              parse_mode='html')


@dp.callback_query_handler(text='call')
async def call(call: types.CallbackQuery) -> None:
    """ выбор варианта звонок """
    await call.message.answer(text=call_answer, reply_markup=another,
                              parse_mode='html')


@dp.callback_query_handler(text='meeting')
async def meeting(call: types.CallbackQuery) -> None:
    """ выбор варианта личная встреча """
    await call.message.answer(text=meeting_answer, reply_markup=another,
                              parse_mode='html')


@dp.callback_query_handler(text='chat_yes')
async def chat_yes(call: types.CallbackQuery) -> None:
    """ заполнил форму """
    await call.message.answer(text=chat_yes_answer, reply_markup=another,
                              parse_mode='html')
    await bot.send_message(chat_id=ADMIN_ID, text=f'{discuss_answer}, user=@{call.from_user.username}')


@dp.callback_query_handler(text='chat_no')
async def chat_no(call: types.CallbackQuery) -> None:
    """ не заполнил форму """
    await call.message.answer(text=chat_no_answer, reply_markup=chat_no_options,
                              parse_mode='html')


@dp.callback_query_handler(text='basic_answer8')
async def basic_answer8(call: types.CallbackQuery) -> None:
    """ ответ на 8 вопрос """
    await call.message.answer(text=basic_answer7_text, reply_markup=question_options7, parse_mode='html')


@dp.message_handler(content_types='photo')
async def get_file_id(message: types.Message) -> None:
    """ получение file_id фотографии """
    print(message.photo)


executor.start_polling(dp, skip_updates=False)
