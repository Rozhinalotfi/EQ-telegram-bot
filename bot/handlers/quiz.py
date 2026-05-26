from telegram import Update
from telegram.ext import ContextTypes

from bot.services.scoring import compute_all
from db.database import save_result
from bot.ui.keyboard import build_answer_keyboard, build_gender_keyboard
from bot.constants.questions import QUESTIONS
from bot.constants.states import QUESTION, GENDER, AGE


async def send_question(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    qi   = context.user_data["q_index"]
    text = f"📋 سوال *{qi + 1}* از *{len(QUESTIONS)}*\n\n{QUESTIONS[qi]}"
    kb   = build_answer_keyboard()
    if update.callback_query:
        await update.callback_query.edit_message_text(text, parse_mode="Markdown", reply_markup=kb)
    else:
        await update.message.reply_text(text, parse_mode="Markdown", reply_markup=kb)
    return QUESTION


async def handle_start_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.callback_query.answer()
    return await send_question(update, context)


async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    context.user_data["answers"].append(int(query.data.split("_")[1]))
    context.user_data["q_index"] += 1
    if context.user_data["q_index"] < len(QUESTIONS):
        return await send_question(update, context)
    await query.edit_message_text(
        "✅ تمام سوالات پاسخ داده شد!\n\n👤 لطفاً جنسیت خود را انتخاب کنید:",
        reply_markup=build_gender_keyboard(),
    )
    return GENDER