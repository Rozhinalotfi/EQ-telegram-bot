import sys
from pathlib import Path


if __package__ is None:
    root = Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(root))

from telegram.ext import Application, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, filters

from config import BOT_TOKEN, DB_FILE
from bot.handlers.profile import cancel, handle_age, handle_gender
from bot.handlers.quiz import handle_answer, handle_start_callback
from bot.handlers.start import start
from db.database import init_db
from bot.constants.states import QUESTION, GENDER, AGE

def main():
    init_db()
    app = Application.builder().token(BOT_TOKEN).build()

    conv = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            QUESTION: [
                CallbackQueryHandler(handle_start_callback, pattern="^start_quiz$"),
                CallbackQueryHandler(handle_answer,         pattern="^ans_"),
            ],
            GENDER: [CallbackQueryHandler(handle_gender, pattern="^gender_")],
            AGE:    [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_age)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
        per_user=True,
        per_chat=True,
    )

    app.add_handler(conv)
    print("Bot is running...")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()