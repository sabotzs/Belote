import unittest
from team import Team
from player import Player

class TestTeam(unittest.TestCase):
    def test_team_without_players(self):
        exc = None
        try:
            Team("Pesho")
        except TypeError as error:
            exc = error
        self.assertIsNotNone(exc)

    def test_team_with_more_than_two_players(self):
        exc = None
        try:
            Team("Cats",Player("Gosho"),Player("Ivan"),Player("Pesho"))
        except TypeError as error:
            exc = error
        self.assertIsNotNone(exc)

    def test_with_arguments_that_is_not_string(self):
        exc = None
        try:
            Team("Cats","Pesho",12)
        except TypeError as error:
            exc = error
        self.assertIsNotNone(exc)

    def test_with_two_arguments_that_are_strings(self):
        exc = None
        try:
            Team("Cats",Player("Pesho"),Player("Gosho"))
        except TypeError as error:
            exc = error
        self.assertIsNone(exc)

if __name__ == '__main__':
    unittest.main()

