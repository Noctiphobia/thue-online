from config import *
from utils import *
import random

class Thue:

    def __init__(self):
        self.player_1 = None
        self.player_2 = None
        self.alphabet = None
        self.max_length = None
        self.sequence = ''

    def configure(self) -> None:
        self.player_1, self.player_2 = get_game_mode()
        self.alphabet = get_alphabet()
        self.max_length = get_max_game_length()

    def play(self) -> int:
        if None in [self.player_1, self.player_2, self.alphabet, self.max_length]:
            raise ValueError('Gra nie została skonfigurowana.')
        self.sequence = ''
        winner = None
        while winner is None:
            print(pad('Ruch {}'.format(len(self.sequence) + 1)))
            position = read_int('Proszę podać pozycję (0-{}): '.format(len(self.sequence)), (0, len(self.sequence))) if self.player_1 is PlayerType.HUMAN else self._make_ai_1_move()
            print_highlighted_at_position(self.sequence, position, '?')
            letter = read_letter('Proszę podać literę: ', self.alphabet) if self.player_2 is PlayerType.HUMAN else self._make_ai_2_move(position)
            print_highlighted_at_position(self.sequence, position, letter)
            self.sequence = self.sequence[:position] + letter + self.sequence[position:]
            winner = self._get_winner()
        print(pad('Wygrał gracz {}'.format(winner)))
        return winner

    def _get_winner(self) -> Union[int, None]:
        repetition = self._find_repetition(self.sequence)
        if repetition is not None:
            print(pad('REPETYCJA'))
            print_highlighted_between(self.sequence, repetition)
            return 1
        if len(self.sequence) >= self.max_length:
            return 2
        return None

    @staticmethod
    def _find_repetition(sequence: str) -> Union[Tuple[int, int], None]:
        for position in range(0, len(sequence)):
            for repetition_length in range(1, int((len(sequence) - position) / 2) + 1):
                if sequence[position:(position + repetition_length)] == sequence[(position + repetition_length):(
                        position + 2 * repetition_length)]:
                    return position, position + 2 * repetition_length
        return None

    def _make_ai_2_move(self, position: int) -> str:
        for character in self.alphabet:
            if self._find_repetition(self.sequence[:position] + character + self.sequence[position:]) is None:
                return character
        return self.alphabet[0]

    def _make_ai_1_move(self) -> int:
        return random.randint(0, len(self.sequence))
