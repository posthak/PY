from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
from bot_commands import *
import emoji

app = ApplicationBuilder().token(
    "5878298085:AAHZHLiKQ6WdvH0TK5NePc-drHjZBW_X_BI").build()

app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("game", crosszero_command))
app.add_handler(MessageHandler(None, gaming_command))
print(emoji.emojize(f'Hi :thumbs_up:'))
print('server start')
app.run_polling()
