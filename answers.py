from aiogram.types import InputMediaPhoto

basic_answer1_text = 'BEEL — это гибкая система бронирования, предназначенная для ресторанов,' \
                     ' коворкингов, кинотеатров и других бизнесов. Она позволяет управлять' \
                     ' бронированиями и администрировать Ваше место эффективно. Система BEEL ' \
                     'постоянно поддерживается и развивается, что помогает вам получать самые удобные' \
                     ' и нужные для бизнеса инструменты: промокоды, мероприятия,' \
                     ' бронирование отдельных комнат и мест по времени,' \
                     ' просмотр статистики по посетителям и получение полного ' \
                     'отчета по Вашему бизнесу.'

basic_answer2_text = 'BEEL предоставляет широкий спектр функциональных возможностей,' \
                     ' включая управление бронированиями, настройку доступности мест,' \
                     ' гибкую настройку под нужды бизнеса, создание сценариев промокодов,' \
                     ' управление мероприятиями с местами и без мест и многое другое.' \
                     ' Вы бы хотели получить более подробную информацию о каждой возможности?'

option2p1_answer = 'Эта функция позволяет Вашим клиентам бронировать места в различных местах,' \
                   ' таких как коворкинги, комнаты, столики в ресторанах или записи на прием' \
                   ' к специалисту.\n\nОсновными характеристиками этой функции является:' \
                   '\n\n<b>Гибкость</b>: Клиенты могут выбирать дату, время и продолжительность' \
                   ' бронирования.\n<b>Доступность</b>: Ваши клиенты могут видеть доступные места' \
                   ' и выбирать те, которые соответствуют их предпочтениям. Все места можно' \
                   ' интуитивно понятно найти в помещении, а также клиент сразу будет знать' \
                   ' занято ли место рядом с ним.\n<b>Подтверждение</b>: После выбора места, клиент' \
                   ' получает подтверждение бронирования через SMS, социальную сеть или' \
                   ' электронную почту.'

option2p1_photos = [
    InputMediaPhoto('AgACAgIAAxkBAAIBvmTwv-Mq7YaDY02oaOoigL9TwKjZAAJ3yjEbtEGIS_6aMDnVP1S-AQADAgADeQADMAQ'),
    InputMediaPhoto('AgACAgIAAxkBAAIBv2Twv_7ApjJTAAFAu3WYTcc5fvBGiwACotIxG8kyeEtTCa_8gjvN9AEAAwIAA3kAAzAE'),
]

option2p2_answer = 'Эта функция подходит для бизнесов, организующих мероприятия с определенными' \
                   ' местами, например, кинотеатры, театры, конференции, концертные площадки или' \
                   ' иные мероприятия, где предусматривается строгое распределение клиентов по' \
                   ' местам. Важные особенности:\n\n<b>Интерактивная карта мест</b>: Позволяет клиентам' \
                   ' выбирать конкретные места на карте зала. Показывает структуру зала и' \
                   ' расположение мест для лучшего выбора.\n<b>Гибкая ценовая политика</b>: Позволяет' \
                   ' настроить разные категории мест с разными ценами (например ряды 1-4 с' \
                   ' повышенным тарифом) или ввести особую зону с диванами.\n<b>Напоминания о' \
                   ' мероприятии</b>: За определенное количество дней до мероприятия мы ' \
                   'отправляем напоминание о регистрации на Ваше мероприятие, таким' \
                   ' образом клиент не забудет о Вас.\n\nКаждое мероприятие BEEL имеет' \
                   ' свои поля для заполнения. Для мероприятий с местами это: ' \
                   'локация, название мероприятия, описание, дата и время проведения, ' \
                   'цена за вход, изображение-превью мероприятия.'

option2p2_photos = [
    InputMediaPhoto('AgACAgIAAxkBAANbZO9PnU_FOR69aJuiRUOt84x4iMYAAn_SMRvJMnhLjvHhUkklrd4BAAMCAAN5AAMwBA'),
]

option2p3_answer = 'Эта функция предназначена для мероприятий, на которые можно прийти без' \
                   ' заранее заготовленного числа мест, например на праздник Вашего открытия' \
                   ' или юбилея компании. Такие мероприятия можно организовывать регулярно' \
                   ' (клуб английского языка) или же делать их событиями, которые происходят' \
                   ' только один раз (презентация нового продукта).  Основные характеристики' \
                   ' мероприятий без мест:\n\n' \
                   '<b>Регистрация на мероприятие</b>: Клиенты могут зарегистрироваться на' \
                   ' мероприятие, только указав свои данные, без выбора мест и очень быстро.\n' \
                   '<b>Подтверждение участия</b>: После регистрации клиент получает подтверждение' \
                   ' участия и дополнительные инструкции. А также предусмотрена система' \
                   ' напоминаний о мероприятии, например за день до него.\n\n' \
                   'Каждое мероприятие BEEL имеет свои поля для заполнения. ' \
                   'Для мероприятий без мест это: название мероприятия, описание, дата' \
                   ' и время проведения, цена за вход, изображение-превью мероприятия.'

option2p3_photos = [
    InputMediaPhoto('AgACAgIAAxkBAANdZO9P6pMQta7mdHxDeDXhimiNdu4AAoDSMRvJMnhLrURpQ2UJXr8BAAMCAAN5AAMwBA'),
]

option2p4_answer = 'Эта функция позволяет собирать и анализировать данные о бронированиях' \
                   ' и мероприятиях с целью улучшения бизнес-процессов. Важные аспекты:\n\n' \
                   '<b>Настройка критериев</b>: Вы можете выбирать, какие данные собирать' \
                   ' (например, количество бронирований, популярные услуги, временные ' \
                   'интервалы и т.д.).\n' \
                   '<b>Аналитика</b>: Вы получаете аналитические отчеты и графики для лучшего ' \
                   'понимания тенденций и потребностей клиентов. '

option2p4_photos = [
    InputMediaPhoto('AgACAgIAAxkBAANeZO9QJoHn0jAlbFa7Sw2-oakAATnyAAKB0jEbyTJ4S9VyU4og_WFVAQADAgADeQADMAQ'),
    InputMediaPhoto('AgACAgIAAxkBAANfZO9QXuToMD8gHwF5PrLEFViGUX4AAoXSMRvJMnhLBp-kfQN6px0BAAMCAAN5AAMwBA'),
]

option2p5_answer = 'Эта функция позволяет вам создавать и управлять промокодами и акциями' \
                   ' для привлечения клиентов. Основные возможности:\n\n' \
                   '<b>Скидки и акции</b>: Вы можете создавать временные или постоянные скидки' \
                   ' на услуги и мероприятия, а также на все заказы в BEEL.\n' \
                   '<b>Привлечение клиентов</b>: Промокоды могут стать мощным инструментом для' \
                   ' привлечения новых клиентов или повышения лояльности существующих.\n' \
                   '<b>Отчеты по акциям</b>: Вы можете следить за эффективностью акций и ' \
                   'анализировать, какие промокоды работают лучше всего.'

option2p5_photos = [
    InputMediaPhoto('AgACAgIAAxkBAANhZO9QyFqHK4W8RWpUPPV81VtPP30AAorSMRvJMnhLRQXZyyrXMYsBAAMCAAN5AAMwBA'),
    InputMediaPhoto('AgACAgIAAxkBAANzZO9UHWUYTmTL6u35v0tBkYxXJ94AApvSMRvJMnhLaaC1eN2Qx_4BAAMCAAN5AAMwBA'),
]

basic_answer3_text = 'BEEL подходит для различных типов бизнесов, таких как рестораны,' \
                     ' коворкинги, оздоровительные салоны, салоны красоты, кинотеатры' \
                     ' и многие другие. Систему можно адаптировать под практически любой' \
                     ' вид деятельности. Если Вашего бизнеса не попадает под эти категории,' \
                     ' то Вы можете оставить заявку на консультацию по системе. Какой бизнес' \
                     ' Вас интересует?'

option3p1_answer = 'Оптимизируйте процесс бронирования столов и управления гостями с BEEL.' \
                   ' Настроив доступность столов и предварительные заказы, ' \
                   'Вы сможете обеспечить комфорт и быстрое обслуживание для каждого клиента.' \
                   ' С BEEL Ваш ресторан может обеспечить максимальное удобство для гостей' \
                   ' при бронировании столов.\n\nОсновные моменты для ресторанного ' \
                   'бизнеса:\n\n<b>Гибкая бронь</b>: Гости могут выбирать дату, время и количество' \
                   ' гостей, а также видеть доступные столики.\n<b>Меню и предложения</b>: ' \
                   'Предоставьте гостям информацию о меню и специальных предложениях ' \
                   'при бронировании на сайте. Дополнительно мы также можем разработать ' \
                   'электронное меню и функцию заказа заранее.\n<b>Онлайн-оплата</b>: ' \
                   'Позвольте клиентам оплатить предварительно, что ускорит процесс' \
                   ' в ресторане.\n<b>Уведомления</b>: Гости получают напоминания о предстоящем' \
                   ' бронировании и событии.'

option3p2_answer = 'Привнесите удобство в бронирование номеров и дополнительных услуг' \
                   ' с BEEL. Гости могут выбрать и забронировать номера, а также ' \
                   'заказать дополнительные сервисы, такие как экскурсии или спа-процедуры,' \
                   ' всего в несколько кликов. Система BEEL упрощает управление' \
                   'бронированием номеров и создает лучший опыт для ' \
                   'гостей:\n\n<b>Интерактивные карты</b>: Гости могут выбрать номера на схеме ' \
                   'и увидеть доступные варианты.\n<b>Дополнительные услуги</b>: Предоставьте ' \
                   'возможность бронирования дополнительных услуг, таких как трансфер и ' \
                   'экскурсии.\n<b>Онлайн-регистрация</b>: Гости могут зарегистрироваться онлайн ' \
                   'и ускорить процесс заселения.\n<b>Без комиссий</b>: все заказы осуществляются' \
                   ' без лишней комиссии - бизнес платит только за подписку на сервис. '

option3p3_answer = 'Управляйте рабочими местами и комнатами для совместной работы с' \
                   ' легкостью. Клиенты могут выбрать подходящие места, забронировать' \
                   ' и оплатить их онлайн, а также получить информацию о доступности ' \
                   'и мероприятиях. Для коворкинга BEEL предоставляет инструменты для' \
                   ' эффективного управления рабочими местами и комнатами:\n\n<b>Гибкость ' \
                   'выбора мест</b>: Клиенты могут выбрать оптимальное рабочее место и ' \
                   'оплатить его онлайн или наличными на месте.\n<b>Планирование</b>: ' \
                   'Просматривайте расписание занятости рабочих мест и администрируйте' \
                   ' забронированные комнаты.\n<b>Telegram бот</b>: Интеграция с телеграм ботами' \
                   ' позволяет удобно отслеживать бронь, мероприятия или быстро забронировать' \
                   ' место прямо в телеграме.\n\nУ нас есть стабильно работающий пример ' \
                   'нашего клиента в отрасли коворкингов. Подключение данной системы к ' \
                   'Eneik coworking привело к увеличению продаж мест и мероприятий этому' \
                   ' бизнесу. Вы можете ознакомиться с работой данного сервиса по ' \
                   'ссылке: eneik.ge/booking.'

option3p3_photos = [
    InputMediaPhoto('AgACAgIAAxkBAAN0ZO9UV_WImCGM17-Khj7q-lnJDkgAAp3SMRvJMnhLTMGSyPJtVhQBAAMCAAN5AAMwBA'),
    InputMediaPhoto('AgACAgIAAxkBAAMfZO9HHSvSaaTDxgSFrUER-lpAdBsAAlbSMRvJMnhLCFpk19si5tgBAAMCAAN4AAMwBA'),
    InputMediaPhoto('AgACAgIAAxkBAAN2ZO9VENqMLwKd6ZTPald5GI3Pn6AAAqHSMRvJMnhL46JKn6P0qRwBAAMCAAN5AAMwBA'),
    InputMediaPhoto('AgACAgIAAxkBAAN3ZO9VWFWPY8GczPWf2U-nnK7mMYIAAqLSMRvJMnhLUwmv_II7zfQBAAMCAAN5AAMwBA'),
    InputMediaPhoto('AgACAgIAAxkBAAN4ZO95-gNDUtwE9vsaeQHqy64EQUQAAnnTMRvJMnhLcoHrRty4SfUBAAMCAAN5AAMwBA'),
    InputMediaPhoto('AgACAgIAAxkBAAN5ZO96ErSvOCkLEtB3C2vCIzo11d4AAnrTMRvJMnhL-JzvlOktjjIBAAMCAAN5AAMwBA'),
]

option3p4_answer = 'Улучшите опыт посетителей мероприятий с помощью BEEL.' \
                   ' Он позволяет бронировать места с интерактивной картой зала,' \
                   ' выбирать наилучшие места и получать удобные напоминания о предстоящих' \
                   ' событиях. BEEL улучшает опыт посетителей на мероприятиях, где важна ' \
                   'точная организация:\n\n<b>Интерактивная карта мест</b>: Клиенты могут выбрать ' \
                   'места на схеме зала и увидеть доступные варианты.\n<b>Выбор сеанса</b>: ' \
                   'Покупатели могут выбрать определенное время мероприятия и забронировать' \
                   ' места.\n<b>Электронные билеты</b>: После бронирования клиенты получают ' \
                   'электронные билеты для удобного доступа.'

option3p5_answer = 'Облегчите клиентам запись на процедуры и услуги в Вашем салоне.' \
                   ' С BEEL, клиенты могут выбрать желаемое время и услугу, а также' \
                   ' получить уведомление о ближайших визитах, помогая им поддерживать ' \
                   'заботу о себе. С BEEL, салон может легко организовать запись на услуги' \
                   ' и процедуры:\n\n<b>Онлайн-запись</b>: Клиенты могут выбрать услугу, мастера' \
                   ' и время записи.\n<b>Подтверждение</b>: Система автоматически подтверждает ' \
                   'запись и напоминает клиентам о визите по электронной почте, SMS или' \
                   ' через Telegram бота.\n<b>Отзывы и рейтинги</b>: После визита клиенты могут' \
                   ' оставить отзывы, что поможет улучшить качество обслуживания.'

option3p6_answer = 'Упростите заказ и управление услугами по уборке и ремонту. ' \
                   'С BEEL, клиенты могут выбрать нужный тип услуги, указать дату и ' \
                   'время, а также получить подтверждение заказа и информацию о бригаде ' \
                   'специалистов. BEEL облегчает процесс заказа и координации услуг по ' \
                   'уборке и сантехническим работам:\n\n<b>Выбор услуги</b>: Клиенты могут выбрать' \
                   ' вид услуги, указать детали и удобное время.\n<b>Оценка стоимости</b>: ' \
                   'Система позволяет клиентам видеть ориентировочную стоимость услуги' \
                   ' перед заказом.\n<b>Онлайн-оплата</b>: После заказа клиенты могут оплатить ' \
                   'услугу онлайн, что упрощает процесс.\n\nУ нас есть готовое решение' \
                   ' на сервисы услуг, оказываемых на дому, таких как клининг, сантехники' \
                   ', ремонтные и прочие. Одним из готовых примеров в этой категории ' \
                   'является система BEEL-clean.ge .'

option3p6_photos = [
    InputMediaPhoto('AgACAgIAAxkBAAN6ZO97XmReu166IqbRNv4T-qqx9WUAAoHTMRvJMnhLv4g5kDFypToBAAMCAAN5AAMwBA'),
    InputMediaPhoto('AgACAgIAAxkBAAN7ZO97mFVsU86KK48Oze6UjWC2qSAAAoPTMRvJMnhLphDrwvayOCUBAAMCAAN5AAMwBA'),
    InputMediaPhoto('AgACAgIAAxkBAAN8ZO97xHRZgTBmnfoUjxkTBpAN8HAAAoHSMRvJMnhL1XJTiiD9YVUBAAMCAAN5AAMwBA'),
    InputMediaPhoto('AgACAgIAAxkBAAN9ZO975NK0-brAJbRpYRZQ1GaTJd8AAobTMRvJMnhL3HlxORXF0fYBAAMCAAN5AAMwBA'),
]

option3p7_answer = 'Напишите, пожалуйста, отрасль Вашего бизнеса для улучшения нашего сервиса ' \
                   'в наш чат'

discuss_answer = 'Пора обсуждать!!!'


basic_answer4_text = 'Одним из ключевых преимуществ BEEL является возможность кастомизации' \
                     ' под конкретные потребности Вашего бизнеса. Вы можете настроить систему ' \
                     'так, чтобы она идеально соответствовала Вашим процессам и требованиям. ' \
                     'При первоначальной настройке мы отрисовываем под Ваш бизнес помещения, ' \
                     'чтобы бронирование происходило наиболее удобно и комфортно для Ваших клиентов.' \
                     ' Вы бы хотели узнать индивидуальные предложения под Ваш бизнес?'

another_answer = 'Ваш запрос был принят, наш менеджер свяжется с вами в скором времени'

basic_answer5_text = 'Система BEEL продается по модели подписки. Оплата может ' \
                     'производиться 3 разными вариантами: \n\n1)3% процента от выручки ' \
                     'при любом обороте, годовая. Перейти с этого тарифа можно в любое время.' \
                     '\n2)50€ в месяц. Перейти с этого тарифа можно в любое время.\n3)500€ ' \
                     'годовая, доступна с 2 секциями при единоразовом платеже. \n\nПри настройке' \
                     ' системы под задачи бизнеса необходимо внести единоразовую оплату, сумма' \
                     ' которой обсуждается в личном порядке. В первоначальную настройку входит' \
                     ' :подключение сервера и хостинга, выбор и настройка необходимых ' \
                     'модулей программы, создание индивидуального плана помещений, фирменного' \
                     ' стиля и многие другие опции, которые оговариваются в индивидуальном порядке.'

basic_answer6_text = 'После настройки системы BEEL, Вы получите доступ к нашей ' \
                     'технической поддержке. Мы готовы помочь вам решать любые возникающие ' \
                     'вопросы и проблемы. А также мы периодически обновляем систему, добавляем' \
                     ' в нее новые фичи и модули, чтобы оставаться в бизнесе. Все последующие' \
                     ' обновления будут учитывать Вашу специфику.'


basic_answer7_text = 'Для начала использования BEEL свяжитесь с нашей командой для обсуждения' \
                     ' Ваших требований. Для Вашего удобства мы подготовили' \
                     ' <a href="https://forms.gle/huXvBZufdwRJNy3e7">GoogleForm</a>, заподлнив которую Вы начнете ' \
                     'процесс подключения системы BEEL. Мы поможем вам определиться с планом ' \
                     'и начать процесс внедрения. Мы можем запланировать чатинг, звонок или ' \
                     'личную встречу. Как вам было бы удобнее продолжить диалог?'

chat_answer = "Вы можете использовать этого бота для подачи информации нашей команде. " \
              "Для начала, Вы прошли <a href='https://forms.gle/huXvBZufdwRJNy3e7'>GoogleForm</a>?"

call_answer = 'Хорошо, напишите временные промежутки, когда вам удобнее будет созвониться  и  убедитесь,' \
              ' что у Вас открыт доступ к звонкам в телеграмме. Также, если вам было бы удобнее' \
              ' созвониться в Google Meet, то укажите это в текстовом сообщении'

meeting_answer = 'Хорошо, напишите, где и когда Вы бы хотели встретиться. Встретиться с' \
                 ' командой разработчиков Вы можете в Грузии, г.Кутаиси, ' \
                 '<a href="https://maps.app.goo.gl/JnAmrHsZitRiZ1xR6">Eneik coworking</a>' \
                 '.\n\nТакже Вы можете встретиться' \
                 ' с нашими менеджерами-представителями в следующих городах:\n1)Германии, ' \
                 'Берлин\n2)Лион, Франция\n3)Нью-Йорк, США\n4)Неаполь, Италия\n5)Барселона, ' \
                 'Испания\n6)Дели, Индия\n7)Пхукет, Таиланд\n8)Исламабад, Пакистан'

chat_yes_answer = 'Хорошо, в течение некоторого времени 1-2 рабочих дней мы обработаем Вашу' \
                  ' заявку, после чего продолжим диалог с менеджером в формате чата.'

chat_no_answer = 'Мы не сможем продолжить работу с вами в формате чата, если Вы не прошли форму.' \
                 ' Вы можете изменить формат диалога или вернуться, когда форма будет пройдена.'

