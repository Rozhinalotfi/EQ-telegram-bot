from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from bot.constants.states import AGE

from bot.services.scoring import compute_all
from db.database import save_result
from bot.utils.helpers import level_emoji, pct_bar
from bot.constants.scales import COMPOSITE_SCALES, SUBSCALE_NAMES
from bot.services.scoring import MAX_PER_SUBSCALE, MAX_TOTAL


async def handle_gender(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    if "male" in query.data:
        context.user_data["gender"] = "مرد"
    elif "female" in query.data:
        context.user_data["gender"] = "زن"
        
    await query.edit_message_text(
        "📅 لطفاً سن خود را وارد کنید:",
    )
    return AGE


async def handle_age(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    age = int(update.message.text)
    gender = context.user_data["gender"]
    answers = context.user_data["answers"]

    sub_scores, sub_pcts, total_score, total_pct, comp_pcts = compute_all(answers)

    user = update.effective_user

    save_result(
        user.id,
        user.username or user.full_name,
        gender,
        age,
        total_score,
        total_pct,
        comp_pcts,
        sub_scores,
        sub_pcts
    )

    msg = f"""
📊 نتیجه:
👤 {gender} | {age}
🏆 {total_score}/{MAX_TOTAL} = {total_pct}%
"""

    await update.message.reply_text(msg)

    context.user_data.clear()
    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()
    await update.message.reply_text("لغو شد")
    return ConversationHandler.END