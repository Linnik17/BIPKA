def smart_analysis(history):
    if len(history) < 5:
        return "⏳ Нужно минимум 5 коэффициентов"

    last5 = history[-5:]

    low = sum(1 for x in last5 if x < 1.5)
    high = sum(1 for x in last5 if x > 3)
    avg = sum(last5) / len(last5)

    if low >= 4:
        return "🔥 Серия низких → возможен высокий вылет (2x–5x)"

    if high >= 2:
        return "⚠️ Было много высоких → возможен откат"

    if avg < 2:
        return "📈 Спокойно → возможен рост 2x–3x"

    return "⚖️ Нейтрально → лучше ждать"
