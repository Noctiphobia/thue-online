import math
from typing import Tuple, Union
from termcolor import colored


def read_int(prompt: str, value_range: Tuple[Union[int, None], Union[int, None]]=None) -> int:
    response = None
    range_min, range_max = value_range or (None, None)
    while response is None:
        try:
            selection = int(input(prompt))
            if selection < (range_min or float('-inf')) or selection > (range_max or float('inf')):
                raise ValueError()
            response = selection
        except ValueError:
            prompt = 'Niepoprawny wybór - proszę podać liczbę' + ' z zakresu od {} do {}: '.format(
                range_min if range_min is not None else '-\u221E', range_max if range_max is not None else '\u221E') if value_range is not None else ': '
    return response


def read_letter(prompt: str, possible_values: str) -> str:
    letter = None
    while letter is None:
        response = input(prompt)
        if len(response) == 1 and response in possible_values:
            letter = response
        else:
            prompt = 'Niepoprawny wybór - proszę wybrać literę spośród {}.'.format(possible_values)
    return letter


def pad(string: str, length: int=30) -> str:
    padding_to_add = length - len(string) - 2
    if padding_to_add <= 0:
        return string
    return int(math.floor(padding_to_add/2)) * '-' + ' ' + string + ' ' + int(math.ceil(padding_to_add/2)) * '-'


def print_highlighted_at_position(sequence: str, position: int, position_char: str):
    print(sequence[:position] + colored(position_char, 'red', attrs=['blink', 'bold']) + sequence[position:])


def print_highlighted_between(sequence: str, interval: Tuple[int, int]):
    start, end = interval
    print(sequence[:start] + colored(sequence[start:end], 'red', attrs=['blink', 'bold']) + sequence[end:])