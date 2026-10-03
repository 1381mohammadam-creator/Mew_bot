from telegram.ext import Application

TOKEN = "8883719665:AAHRtQUmTAu7XSIBLXrRW6HDzxCCja4AqP0"
CHAT_ID = -1004324137498

async def meow(context):
    await context.bot.send_message(chat_id=CHAT_ID, text="میو")

app = Application.builder().token(TOKEN).build()
app.job_queue.run_repeating(meow, interval=300, first=10)
print("ربات روشن شد و هر ۵ دقیقه میو می‌فرسته")
app.run_polling()
