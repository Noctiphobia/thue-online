from enum import Enum
from typing import List
from utils import read_int

import itertools


class PlayerType(Enum):
    HUMAN = 1,
    AI = 2


def get_alphabet() -> str:
    default_alphabet = ''.join(get_characters_between('0', '9') + get_characters_between('a', 'z') + get_characters_between('A', 'Z'))
    select_number_of_letters = 'Liczba dostępnych liter (od 1 do {})'.format(len(default_alphabet))
    select_alphabet = 'Wprowadzenie wszystkich dostępnych liter'
    mode = get_option('Proszę wybrać metodę wprowadzenia alfabetu: ', [select_number_of_letters, select_alphabet])
    if mode == 1:
        alphabet = default_alphabet[:read_int(select_number_of_letters + ': ', (1, len(default_alphabet)))]
    else:
        alphabet = ''.join(sorted(list(set(input(select_alphabet + ': ')))))
    print('Wyznaczony alfabet: {}'.format(alphabet))
    return alphabet


def get_game_mode() -> (PlayerType, PlayerType):
    player_types = ['człowiek', 'komputer']
    mode = get_option('Proszę wybrać tryb gry: ', ['{} kontra {}'.format(player_1, player_2) for player_1, player_2 in itertools.product(player_types, player_types)])
    player_1 = PlayerType.HUMAN if mode in (1, 2) else PlayerType.AI
    player_2 = PlayerType.HUMAN if mode in (1, 3) else PlayerType.AI
    return player_1, player_2


def get_max_game_length() -> int:
    return read_int('Proszę wybrać maksymalną liczbę ruchów: ', (1, None))


def get_option(prompt: str, options: List[str]) -> int:
    numbered_options = ['{}. {}'.format(number + 1, option) for number, option in enumerate(options)]
    full_prompt = '\n'.join([prompt] + numbered_options + ['Wybór (1-{}): '.format(len(options))])
    return read_int(full_prompt, (1, len(options)))


def get_characters_between(start: str, end: str) -> List[str]:
    return [chr(char_code) for char_code in range(ord(start), ord(end) + 1)]
