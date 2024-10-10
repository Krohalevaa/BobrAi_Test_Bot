import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BobrAi_Test_Bot.settings')
django.setup()

from weather.models import RequestLog
from weather.utils import get_weather
from telebot import TeleBot

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = TeleBot(token=TELEGRAM_TOKEN)


@bot.message_handler(commands=['weather'])
def handle_weather(message):
    """
    Обработчик команды /weather.
    Получает название города из сообщения пользователя, запрашивает информацию
    о погоде с использованием функции get_weather, и отправляет ответ.
    """
    try:
        city = message.text.split(' ')[1]
        weather_data = get_weather(city)
        if weather_data:
            temp = weather_data['main']['temp']
            feels_like = weather_data['main']['feels_like']
            description = weather_data['weather'][0]['description']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']
            response = (f"Погода в {city}:\nТемпература: {temp}°C\n"
                        f"Ощущается как: {feels_like}°C\n"
                        f"Описание: {description}\n"
                        f"Влажность: {humidity}%\n"
                        f"Скорость ветра: {wind_speed} м/с")
        else:
            response = (
                "Не удалось получить данные о погоде. Проверьте правильность"
                "названия города.")
    except IndexError:
        response = "Пожалуйста, укажите город. Пример: /weather Москва"
    bot.send_message(message.chat.id, response)
    log = RequestLog(
        user_id=message.from_user.id,
        command=message.text,
        response=response)
    log.save()


bot.polling()
