from telegram.ext import CommandHandler


def command_handler(command, app):
    def decorator(func):
        handler = CommandHandler(command, func)
        app.add_handler(handler)
        return func
    return decorator
