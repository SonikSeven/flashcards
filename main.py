import random
import os
import argparse


original_print = print
original_input = input
log_name = 'temporary_log.txt'
open(log_name, 'w').close()
flashcards = {}
errors = {}
parser = argparse.ArgumentParser()
parser.add_argument('--import_from')
parser.add_argument('--export_to')
args = parser.parse_args()


def print(*args, file=None, **kw):
    if file:
        return original_print(*args, file=file, **kw)
    with open(log_name, 'a') as log_file:
        original_print(*args, **kw, file=log_file)
    original_print(*args, **kw)


def input(*args):
    result = original_input(*args)
    with open(log_name, 'a') as log_file:
        original_print(*args, end='', file=log_file)
        original_print(result, file=log_file)
    return result


def add_card():
    card = input('The card:\n')
    while card in flashcards:
        card = input(f'The term "{card}" already exists. Try again:\n')
    definition = input('The definition of the card:\n')
    while definition in flashcards.values():
        definition = input(f'The definition "{definition}" already exists. Try again:\n')
    flashcards[card], errors[card] = definition, 0
    print(f'The pair ("{card}":"{definition}") has been added.\n')


def remove_card():
    card = input('Which card?\n')
    if card in flashcards:
        del flashcards[card], errors[card]
        print('The card has been removed.\n')
    else:
        print(f'Can\'t remove "{card}": there is no such card.\n')


def ask_definition():
    for n in range(1, int(input('How many times to ask?\n')) + 1):
        card, definition = random.choice(list(flashcards.items()))
        answer = input(f'Print the definition of "{card}":\n')
        if answer == definition:
            print('Correct!')
            continue
        elif answer in flashcards.values():
            correct_card = list(flashcards)[list(flashcards.values()).index(answer)]
            print(f'Wrong. The right answer is "{definition}", but your definition is correct for "{correct_card}".')
        else:
            print(f'Wrong. The right answer is "{definition}".')
        errors[card] += 1


def export_cards(file_name=False):
    if file_name is False:
        file_name = input('File name:\n')
    with open(file_name, 'w') as cards_file:
        for card, definition in flashcards.items():
            print(card, definition, errors[card], sep='|', file=cards_file)
    print(len(flashcards), 'cards have been saved.\n')


def import_cards(file_name=False):
    if file_name is False:
        file_name = input('File name:\n')
    if not os.path.exists(file_name):
        return print('File not found.\n')
    with open(file_name) as cards_file:
        for n, line in enumerate(cards_file, start=1):
            card, definition, count = line.strip().split('|')
            flashcards[card], errors[card] = definition, int(count)
    print(n, 'cards have been loaded.\n')


def log_console():
    new_log_name = input('File name:\n')
    with open(log_name) as log_file:
        with open(new_log_name, 'w') as new_log_file:
            new_log_file.writelines(log_file)
    print('The log has been saved.\n')


def hardest_card():
    max_count = max(errors.values()) if errors else 0
    hardest_cards = [card for card, count in errors.items() if count == max_count]
    if max_count == 0:
        print('There are no cards with errors.\n')
    elif len(hardest_cards) > 1:
        hardest_cards = ', '.join(hardest_cards)
        print(f'The hardest cards are {hardest_cards}. You have {max_count} errors answering them.\n')
    else:
        hardest_cards = ', '.join(hardest_cards)
        print(f'The hardest card is {hardest_cards}. You have {max_count} errors answering it.\n')


def reset_stats():
    for card in errors:
        errors[card] = 0
    print('Card statistics have been reset.\n')


def exit_program():
    original_print("Bye bye!")
    os.remove(log_name)
    if args.export_to:
        export_cards(args.export_to)
    return True


def main():
    actions = {'add': add_card,
               'remove': remove_card,
               'import': import_cards,
               'export': export_cards,
               'ask': ask_definition,
               'exit': exit_program,
               'log': log_console,
               'hardest card': hardest_card,
               'reset stats': reset_stats}
    if args.import_from:
        import_cards(args.import_from)
    while True:
        action = input('Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):\n')
        if action in actions and actions[action]():
            break


if __name__ == '__main__':
    main()
