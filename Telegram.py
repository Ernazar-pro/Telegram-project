from aiogram import *


token='6035170185:AAGrTtuX9zLUqi1wffkYxCi9H3vwOzu3X70'

bot=Bot(token)
disp=Dispatcher(bot)

a='photo_2023-03-19_11-52-19'

@disp.message_handler(commands=['start'])
async def start(message):
    name=message['from']['first_name']
    await message.reply(f'Assalawma aleykum {name}')
    print(f'{name} start basti')

@disp.message_handler(commands=['help'])
async def help(message):
    name=message['from']['first_name']
    await message.answer(f"{name}, bul bot Keleshek Akademiyasi niń 'Python pro ' toparinin magliwmatlari saqlanatugin baza")
    await message.answer('Eger magliwmatlar menen tanisiwdi qaleseniz, /baza ni jiberin')
    print(f'{name} help basti')

@disp.message_handler(commands=['baza'])
async def baza(message):
    name=message['from']['first_name']
    await message.answer('Ученик группы Python_pro:\nИмя:ERNAZAR\n\nФамилия:JUMANIYAZOV\n\nКласс:6')
    await message.answer('Ученик группы Python_pro:\nИмя:BEGIS\n\nФамилия:EMBERGENOV\n\nKласс:9')
    await message.answer('Ученик группы Python_pro:\nИмя:YUSUP\n\nФамилия:SALIMOV\n\nКласс:7')
    await message.answer('Ученик группы Python_pro:\nИмя:NURLAN\n\nФамилия:SARSENBAEV\n\nКласс:8')
    await message.answer('Ученик группы Python_pro:\nИмя:ERLAN\n\nФамилия:SARSENBAEV\n\nКласс:8')
    await message.answer('Ученик группы Python_pro:\nИмя:AZIZ\n\nФамилия:DAWLETBAEV\n\nКласс:9')
    await message.answer('Ученик группы Python_pro:\nИмя:ALISHER\n\nФамилия:RUSTAMOV\n\nКласс:6')

if __name__ == '__main__':
    executor.start_polling(disp,skip_updates=True)
