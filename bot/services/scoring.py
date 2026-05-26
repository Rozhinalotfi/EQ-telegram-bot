from bot.constants.scales import REVERSE_QUESTIONS, COMPOSITE_SCALES

MAX_PER_SUBSCALE = 30
MAX_TOTAL = 450

def compute_all(raw_answers):
    scored = [
        (6 - v) if (i + 1) in REVERSE_QUESTIONS else v
        for i, v in enumerate(raw_answers)
    ]

    sub_scores = []
    for si in range(15):
        q_nums = [si + 1 + 15 * k for k in range(6)]
        sub_scores.append(sum(scored[q - 1] for q in q_nums))

    sub_pcts = [round(s / MAX_PER_SUBSCALE * 100, 1) for s in sub_scores]

    total_score = sum(sub_scores)
    total_pct = round(total_score / MAX_TOTAL * 100, 1)

    comp_pcts = []
    for _, _, indices in COMPOSITE_SCALES:
        comp_raw = sum(sub_scores[i] for i in indices)
        comp_pcts.append(round(comp_raw / (len(indices)*MAX_PER_SUBSCALE) * 100, 1))

    return sub_scores, sub_pcts, total_score, total_pct, comp_pcts