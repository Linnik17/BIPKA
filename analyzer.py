def smart_analysis(history):
    if len(history) < 5:
        return "⏳ Нужно больше данных (минимум 5)"

    last = history[-1]
    avg = sum(history[-10:]) / len(history[-10:])

    low_streak = 0
    for x in reversed(history[-10:]):
        if x < 1.5:
            low_streak += 1
        else:
            break

    high = sum(1 for x in history[-10:] if x > 3)

    # 💣 логика
    if low_streak >= 3:
        return (
            "🔥 ОБНАРУЖЕНА СЕРИЯ НИЗКИХ\n"
            "🎯 Возможен резкий выход 2.5x - 4x\n"
            f"📊 среднее: {avg:.2f}"
        )

    if high >= 3:
        return (
            "⚠️ ПЕРЕГРЕВ РЫНКА\n"
            "🚨 лучше пропустить вход\n"
            f"📊 среднее: {avg:.2f}"
        )

    if avg < 2:
        return (
            "📈 Спокойный рынок\n"
            "🎯 возможен рост 2x - 3x"
        )

    return (
        "⚖️ Нейтральная зона\n"
        "⏳ лучше наблюдать"
    )
