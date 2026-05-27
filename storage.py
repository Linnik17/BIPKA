history = []

def add_value(value: float):
    history.append(value)
    if len(history) > 300:
        history.pop(0)

def get_history():
    return history
