def log_message(func):
    def wrapper(*args, **kwargs):
        print(f"Виклик функції {func.name}")
        return func(*args, **kwargs)
    return wrapper