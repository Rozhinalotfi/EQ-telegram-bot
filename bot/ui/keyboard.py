from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from bot.constants.questions import ANSWER_OPTIONS

def build_answer_keyboard():
    btns = [
        InlineKeyboardButton(t, callback_data=f"ans_{v}")
        for t, v in ANSWER_OPTIONS
    ]
    return InlineKeyboardMarkup([btns[:2], btns[2:4], [btns[4]]])


def build_gender_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("👨 مرد", callback_data="gender_male")],
        [InlineKeyboardButton("👩 زن", callback_data="gender_female")],
    ])