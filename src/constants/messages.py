HELP_TEXT = """
Привет! 👋 Это список команд, которые ты можешь использовать:

💵 /get_monthly_payments — Узнать, какие оплаты сделал клиент за 3 месяца.  
🔢 /get_number_of_tennis_training — Посмотреть, сколько тренировок осталось у клиента.  
📆 /get_monthly_visits — Проверить посещения клиента за 3 месяца.  
👤 /add_client — Добавить нового клиента. Просто введи его имя и фамилию!  
💰 /add_payments — Записать платеж (Имя Фамилия Сумма Дата в формате DD.MM.YYYY).  
🎾 /add_visits — Отметить посещение тренировки (Имя Фамилия Дата Время Тип тренировки).  
🧾 /create_report — Создать отчет по клиенту.  
❓ /help — Посмотреть этот список команд еще раз.  

📌 **Важно!** Чтобы избежать ошибок, следуй формату при вводе данных.  
"""

TEXT_OF_MESSAGE_FOR_ADD_CLIENT_REQUEST = (
    "Введите имя и фамилию нового клиента (в формтае Имя Фамилия):"
)

TEXT_OF_MESSAGE_FOR_ADD_PAYMENTS_REQUEST = (
    "Введите данные формата: полное имя сумма дата (в формате DD.MM.YYYY):"
)

TEXT_OF_MESSAGE_FOR_ADD_VISITS_REQUEST = "Введите данные формата: полное имя фамилия дата и время  (в формате DD.MM.YYYY HH:MM) тип тренировки:"

TEXT_OF_MESSAGE_FOR_GET_NUMBER_OF_TENNIS_TRAINING_AVAILABLE_REQUEST = (
    "Введите имя и фамилию клиента (в формате Имя Фамилия):"
)
TEXT_OF_MESSAGE_FOR_GET_MONTHLY_VISITS_REQUEST = "Введите имя и фамилию клиента для получения его посещения (в формате Имя Фамилия):"

TEXT_OF_MESSAGE_FOR_GET_MONTHLY_PAYMENTS_REQUEST = "Введите имя и фамилию клиента для получения его оплаты (в формате Имя Фамилия):"

# todo: get month from this message
TEXT_OF_MESSAGE_FOR_CREATE_REPORT = "Сгенирировать отчет?"
