from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os
TOKEN = os.getenv("BOT_TOKEN")
main_menu = ReplyKeyboardMarkup([
    ["Ijara shartnomasi"],
    ["Kontrakt shartnomasi"],
    ["TTJga joylashish"]
], resize_keyboard=True)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalomu alaykum! Talabalar uchun yordamchi botga xush kelibsiz 👋\nQuyidagi menyudan kerakli bo‘limni tanlang:",
        reply_markup=main_menu)
async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Botni to‘xtatdingiz. Yana kerak bo‘lsa /start ni bosing.")
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
   if text == "Ijara shartnomasi":
        await update.message.reply_text(
            "📄 *Ijara shartnomasi tuzish tartibi:*\n\n"
            "1. Soliq ilovasida ijaraga beruvchi tomonidan elektron kalit yaratiladi\n"
            "2. Ijara shartnomasini soliq xizmatlari orqali tuzing\n"
            "3. Shartnoma tuzilgach, https://kontrakt.edu.uz saytidan ariza yuboring\n"
            "4. Institutga quyidagi hujjatlarni olib boring:\n"
            "   - my.gov.uz dan yashash joyi haqida ma’lumotnoma\n"
            "   - kontrakt.edu.uz arizasi\n"
            "   - Pasport nusxasi\n"
            "   - Ijara shartnomasi nusxasi")
   elif text == "Kontrakt shartnomasi":
        await update.message.reply_text(
            "💳 *Kontrakt shartnomasi va to‘lov:*\n\n"
            "1. https://kontrakt.edu.uz saytiga kiring\n"
            "2. Shartnomani yuklab oling\n"
            "3. To‘lov usullari: PayMe, Click, Zoomrad, Upay, Oson, Anorbank\n"
            "4. To‘lov cheki ni yuklab oling yoki chop eting")
 elif text == "TTJga joylashish":
        await update.message.reply_text(
            "🏢 *TTJga joylashish tartibi:*\n\n"
            "1. kontrakt.edu.uz saytidan ariza yuboring\n"
            "2. TTJ bo‘limiga hujjatlarni olib boring\n"
            "3. Narx va muddatni institutdan aniqlashtiring")
  else:
        await update.message.reply_text("Iltimos, menyudan biror bo‘limni tanlang.")
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("stop", stop))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("✅ Bot ishga tushdi...")
    app.run_polling()
if __name__ == "__main__":
    main()
