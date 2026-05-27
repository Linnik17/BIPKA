def analyze_market():
    return (
        "📊 Анализ рынка:\n"
        "- наблюдается волатильность\n"
        "- возможны короткие множители\n"
        "- риск повышен ⚠️"
    )


def generate_signal(history):
    if len(history) < 5:
        return "⏳ Недостаточно данных"

    avg = sum(history[-10:]) / len(history[-10:])

    if avg < 2:
        return "🎯 Сигнал: возможен рост до 2.5x - 3x"
    elif avg < 3:
        return "⚠️ Средний рынок, осторожный вход"
    else:
        return "🚨 Перегрев рынка, лучше пропустить"
