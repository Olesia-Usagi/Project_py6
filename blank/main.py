"""
Бот надає юзеру вибір на 5 команд: hello, exit, parse_files,
address_book, save_notes
"""

from collections import UserDict
from datetime import datetime
import shelve
from parse_folder import setup


def hello(*args):
    return "How can I help you?"


def exit(*args):
    return "Good bye!"


def parse_files(*args):
    s = 'Ви ввели команду для сортування папки.\n'
    result = setup
    return s, result


# def address_book(*args):
#     result = 'Імпортувати папку, в якій виконується ця функція + допоміжні команди'
#     return result
#
#
# def save_notes(*args):
#     result = 'Імпортувати папку, в якій виконується ця функція + допоміжні команди'
#     return result


COMMANDS = {hello: ["hello", "hi", "h"],
            exit: ["exit", "close", "good bye", ".", "bye"],
            parse_files: ['3'],
            # address_book: ['1'],
            # save_notes: ['2']
            }


def parse_command(user_input: str):
    for k, v in COMMANDS.items():
        for i in v:
            if user_input.lower().startswith(i.lower()):
                return k, tuple(user_input[len(i):].strip().split(" "))


def main():
    while True:
        user_input = input("Choice command:\n1. Adress book\n2.Notes\n3.Parse_files\n>>> ")
        try:
            result, data = parse_command(user_input)
            print(result(*data))
            if result is exit:
                break
        except TypeError:
            print(f"Not found. Please , choose the command: {[v for v in COMMANDS.values()]}")


if __name__ == "__main__":
    main()
