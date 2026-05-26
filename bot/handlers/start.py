from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

from bot.services.scoring import compute_all
from db.database import save_result
from bot.ui.keyboard import build_answer_keyboard
from bot.constants.questions import QUESTIONS
from bot.constants.states import QUESTION, GENDER, AGE


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data.clear()
    context.user_data["answers"] = []
    context.user_data["q_index"] = 0

    await update.message.reply_text(
        "🧠 *آزمون هوش هیجانی بار-ان*\n\n"
        "این آزمون شامل *90 سوال* است.\n"
        "برای هر سوال یکی از گزینه‌های ۱ تا ۵ را انتخاب کنید:\n\n"
        "🔹 ۱ = هرگز\n🔹 ۲ = به ندرت\n🔹 ۳ = گاهی\n🔹 ۴ = اغلب\n🔹 ۵ = همیشه\n\n"
        "برای شروع روی دکمه زیر بزنید 👇",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("▶️ شروع آزمون", callback_data="start_quiz")]]
        ),
    )
    return QUESTION