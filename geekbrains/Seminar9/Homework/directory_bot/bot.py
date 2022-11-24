from typing import Union, List
from functools import wraps
import os
import logging

from telegram import Update, constants, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import filters, ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, CallbackQueryHandler

import directory as dir

if __name__ == '__main__':
    TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
    app = ApplicationBuilder().token(TOKEN).build()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


# Decorators:

def command_handler(command):
    def decorator(func):
        handler = CommandHandler(command, func)
        app.add_handler(handler)
        return func
    return decorator


def send_action(action):
    """Sends `action` while processing func command."""

    def decorator(func):
        @wraps(func)
        async def command_func(update, context, *args, **kwargs):
            await context.bot.send_chat_action(chat_id=update.effective_message.chat_id, action=action)
            return await func(update, context,  *args, **kwargs)
        return command_func

    return decorator


send_typing_action = send_action(constants.ChatAction.TYPING)


# Menu

def build_menu(
    buttons: List[InlineKeyboardButton],
    n_cols: int,
    header_buttons: Union[InlineKeyboardButton,
                          List[InlineKeyboardButton]] = None,
    footer_buttons: Union[InlineKeyboardButton,
                          List[InlineKeyboardButton]] = None
) -> List[List[InlineKeyboardButton]]:
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons if isinstance(
            header_buttons, list) else [header_buttons])
    if footer_buttons:
        menu.append(footer_buttons if isinstance(
            footer_buttons, list) else [footer_buttons])
    return menu


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    await query.answer()

    if query.data == 'сancel':
        await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.effective_message.id)

    elif query.data == 'add_real_friend':
        pass

    elif query.data == 'add_fix_friend':
        try:
            how_much = int(''.join(context.args))
        except Exception:
            how_much = 1
        new_ids = dir.add_fixtures(how_much)
        new_users = []
        for id in new_ids:
            new_user = dir.get_user(id)
            new_users.append(new_user)
            answer_text = ' У тебя ' + ('новая подруга' if new_user.get('sex') == 'F' else 'новый друг') + ' ' + \
                new_user.get('first_name') + ' ' + \
                new_user.get('last_name') + ' '
            answer_text += ('💃' if new_user.get('sex') == 'F' else '🕺')

            await context.bot.send_message(chat_id=update.effective_chat.id, text=answer_text)

    else:
        await query.edit_message_text(text=f"{query.data}")


# Commands:

@send_typing_action
@command_handler(['start', 'restart', 'remember'])
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    hello_text = "Привет, " + str(update.effective_user.first_name) + '! '

    tg_id = update.effective_user.id
    user_data = {
        'first_name': update.effective_user.first_name,
        'last_name': update.effective_user.last_name,
        'tg_id': tg_id,
    }

    id = dir.find_user_by_tg_id(tg_id)
    if not id:
        dir.add_user(user_data)
        hello_text += 'Я тебя запомнил 🧐'
    else:
        dir.update_user(id, user_data)
        hello_text += 'Я тебя помню 🤗'

    await context.bot.send_message(chat_id=update.effective_chat.id, text=hello_text)

    await help(update, context)


@send_typing_action
@command_handler('help')
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    answer = '''Вот список команд, которые я знаю:

    /help - Показать, что я умею
    /restart - Начать заново

    <b>Ты и я:</b>
    /remember - Я тебя запомню
    /forget - Я тебя забуду

    <b>Друзья:</b>
    /add_friend - Добавить друга
    /edit_friend - Изменить данные друга
    /friends - Показать друзей
    /delete_friends - Удалить всех друзей
    '''
    await update.message.reply_text(text=answer, parse_mode=constants.ParseMode.HTML)


@send_typing_action
@command_handler('forget')
async def forget(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tg_id = update.effective_user.id
    id = dir.find_user_by_tg_id(tg_id)
    if not id:
        answer_text = 'Я тебя не знаю 🙄'
    else:
        dir.delete_user(id)
        answer_text = 'Я тебя забыл 🙄'

    await context.bot.send_message(chat_id=update.effective_chat.id, text=answer_text)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Ты кто такой? 🧐')


@send_typing_action
@command_handler('add_friend')
async def add_friend(update: Update, context: ContextTypes.DEFAULT_TYPE):
    header_buttons = [
    ]
    main_buttons = [
        InlineKeyboardButton("Вымышленного", callback_data="add_fix_friend"),
        InlineKeyboardButton("Настоящего", callback_data="add_real_friend"),
    ]
    footer_buttons = [
        InlineKeyboardButton("Никакого", callback_data="сancel"),
    ]
    reply_markup = InlineKeyboardMarkup(
        build_menu(main_buttons, n_cols=2, header_buttons=header_buttons, footer_buttons=footer_buttons))
    await update.message.reply_text("Какого друга добавить:", reply_markup=reply_markup)

    # new_user = {}
    # answer_text = ''
    # if not context.args:
    #     answer_text = ('Вы не указали имя, фамилию и телефон.\n'
    #                    'Чтобы добавить нового друга, напишите в чат:\n'
    #                    '/add_friend Иван Козявкин +79991234567')
    # else:
    #     args_quantity = len(context.args)
    #     if args_quantity > 0:
    #         new_user['first_name'] = context.args[0]
    #         answer_text += new_user['first_name'] + ' '
    #     if args_quantity > 1:
    #         new_user['last_name'] = context.args[1]
    #         answer_text += new_user['last_name'] + ' '
    #     if args_quantity > 2:
    #         new_user['phone'] = context.args[2]

    #     new_id = dir.add_user(new_user)
    #     if added_user := dir.get_user(new_id):
    #         answer_text += 'теперь в твоём списке друзей 🎉'
    #     else:
    #         answer_text += 'так и не стал твоим другом 🤷‍♂️'
    # await update.message.reply_text(text=answer_text)


@send_typing_action
@command_handler('edit_friend')
async def edit_friend(update: Update, context: ContextTypes.DEFAULT_TYPE):
    header_buttons = [
        InlineKeyboardButton("Header Button", callback_data="Header Button"),
    ]
    main_buttons = [
        InlineKeyboardButton("Option 1", callback_data="1"),
        InlineKeyboardButton("Option 2", callback_data="2"),
        InlineKeyboardButton("Option 3", callback_data="3"),
        InlineKeyboardButton("Option 4", callback_data="4"),
    ]
    footer_buttons = [
        InlineKeyboardButton("Footer Button", callback_data="Footer Button"),
    ]
    reply_markup = InlineKeyboardMarkup(
        build_menu(main_buttons, n_cols=2, header_buttons=header_buttons, footer_buttons=footer_buttons))
    await update.message.reply_text("Выберите действие:", reply_markup=reply_markup)


@send_typing_action
@command_handler('friends')
async def friends(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tg_id = update.effective_user.id
    if friends := [user for user in dir.get_users() if user.get('tg_id') != tg_id]:
        answer = f'У тебя {len(friends)} друзей:\n\n'
        for friend in friends:
            answer += ('💃 ' if friend.get('sex') == 'F' else '🕺 ')
            if name := friend.get('first_name'):
                answer += name
            if last_name := friend.get('last_name'):
                answer += ' ' + last_name
            answer += '\n\n'
    else:
        answer = 'У тебя нет друзей. Но есть я 😉'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=answer)


@send_typing_action
@command_handler('delete_friends')
async def delete_friends(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tg_id = update.effective_user.id
    if friends := [user for user in dir.get_users() if user.get('tg_id') != tg_id]:
        answer = f'У тебя было {len(friends)} друзей:\n\n'
        for friend in friends:
            if dir.delete_user(friend.get('id')):
                if name := friend.get('first_name'):
                    answer += name
                if last_name := friend.get('last_name'):
                    answer += ' ' + last_name
                answer += ' больше не ' + \
                    ('друг' if friend['sex'] ==
                     'M' else 'подруга') + ' тебе 😑\n'
        answer += '\nА теперь иди заводи новых 🫂'
    else:
        answer = 'Да не парья, у тебя всё равно нет друзей. Но есть я 😉'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=answer)


@send_typing_action
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Не понимаю такую команду.")

if __name__ == '__main__':
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(MessageHandler(filters.COMMAND, unknown))
    app.run_polling()


# Commands for BotFather:
# help - Показать, что я умею
# remember - Я тебя запомню
# forget - Я тебя забуду
# add_friend - Добавить друга
# edit_friend - Изменить данные друга
# friends - Показать друзей
# delete_friends - Удалить всех друзей
# restart - Начать заново
