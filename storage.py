history = []

def add_value(v):
    history.append(v)
    if len(history) > 200:
        history.pop(0)

def get_history():
    return history
