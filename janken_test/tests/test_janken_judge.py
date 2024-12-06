import unittest
from unittest import parameterized
from source.janken_judge import judge

class TestJankenJudge(unittest.TestCase):
    @parameterized.expand([
        ("draw_goo", "グー", "グー", "draw"),
        ("draw_choki", "チョキ", "チョキ", "draw"),
        ("draw_paa", "パー", "パー", "draw"),
        ("player_win_goo_vs_choki", "チョキ", "グー", "player_win"),
        ("player_win_choki_vs_paa", "パー", "チョキ", "player_win"),
        ("player_win_paa_vs_goo", "グー", "パー", "player_win"),
        ("computer_win_choki_vs_goo", "グー", "チョキ", "computer_win"),
        ("computer_win_paa_vs_choki", "チョキ", "パー", "computer_win"),
        ("computer_win_goo_vs_paa", "パー", "グー", "computer_win"),
    ])
    def test_judge(self, name, computer_hand, player_hand, expected_result):
        self.assertEqual(judge(computer_hand, player_hand), expected_result)

if __name__ == "__main__":
    unittest.main()
