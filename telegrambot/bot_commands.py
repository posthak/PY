
from telegram import Update
from telegram.ext import ContextTypes
import datetime
from spy import *
from bot_functions import showMatrix, checkWin


def setMatrix():
    global matrix
    matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Выбери команду  - /hi /time /help /game')


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/help\n/game')


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()  # /sum 123 534543
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')


async def crosszero_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    setMatrix()
    update.message.reply_text('Играем в крестики нолики!')
    await update.message.reply_text(showMatrix(matrix))
    await update.message.reply_text('Введите номер ячейки, чтобы поставить X(крестик): ')


async def gaming_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    try:
        number = int(update.message.text)
        if checkWin(matrix) != 1:
            if 0 < number < 10:
                while True:
                    if (matrix[number-1] != 'X') and (matrix[number-1] != 'O'):
                        matrix[number-1] = 'X'
                        break
                    else:
                        await update.message.reply_text('Неверный ввод. Ячейка занята')
                        return
                await update.message.reply_text(showMatrix(matrix))

                if checkWin(matrix) == 1:
                    await update.message.reply_text('УРА!!! Победа Х (крестиков)!!!')
                    gameStatus = False
                    return

                await update.message.reply_text('Ход робота:')
                for i in range(0, len(matrix)):
                    if (matrix[i] != 'X') and matrix[i] != 'O':
                        matrix[i] = 'O'
                        break
                await update.message.reply_text(showMatrix(matrix))
                if checkWin(matrix) == 1:
                    await update.message.reply_text('УРА!!! Победа 0 (ноликов)!!!')
                    return
                await update.message.reply_text('Ваш ход:')
            else:
                await update.message.reply_text('Некорректно, введите номер от 1 до 9')
        else:
            await update.message.reply_text('Игра завершена, можете начать заного - /game')
    except:
        await update.message.reply_text('Некорретный ввод')
