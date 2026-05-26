def level_emoji(pct):
    if   pct >= 80: return "🌟"
    elif pct >= 65: return "✅"
    elif pct >= 50: return "📊"
    elif pct >= 35: return "⚠️"
    else:           return "🔴"

def pct_bar(pct, width=10):
    filled = round(pct / 100 * width)
    return "█" * filled + "░" * (width - filled)    