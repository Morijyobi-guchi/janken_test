import unittest
from unittest.mock import patch
import source.janken_main

class TestJankenMain(unittest.TestCase):
    @patch('source.janken_main.computer.computer_pon', return_value='グー')
    @patch('source.janken_main.player.player_pon', return_value='チョキ')
    @patch('source.janken_main.janken_judge.judge', return_value='computer_win')
    def test_play_round_computer_win(self, mock_judge, mock_player, mock_computer):
        player_win, computer_win, proceed = source.janken_main.play_round(1, 0, 0)
        self.assertEqual(player_win, 0)
        self.assertEqual(computer_win, 1)
        self.assertTrue(proceed)

    @patch('source.janken_main.computer.computer_pon', return_value='チョキ')
    @patch('source.janken_main.player.player_pon', return_value='グー')
    @patch('source.janken_main.janken_judge.judge', return_value='player_win')
    def test_play_round_player_win(self, mock_judge, mock_player, mock_computer):
        player_win, computer_win, proceed = source.janken_main.play_round(1, 0, 0)
        self.assertEqual(player_win, 1)
        self.assertEqual(computer_win, 0)
        self.assertTrue(proceed)

    @patch('source.janken_main.computer.computer_pon', return_value='グー')
    @patch('source.janken_main.player.player_pon', return_value='グー')
    @patch('source.janken_main.janken_judge.judge', return_value='draw')
    def test_play_round_draw(self, mock_judge, mock_player, mock_computer):
        player_win, computer_win, proceed = source.janken_main.play_round(1, 0, 0)
        self.assertEqual(player_win, 0)
        self.assertEqual(computer_win, 0)
        self.assertFalse(proceed)

    def test_print_final_result_player_win(self):
        with patch('builtins.print') as mock_print:
            source.janken_main.print_final_result(2, 1)
            mock_print.assert_any_call("【最終結果】")
            mock_print.assert_any_call("あなた: 2勝")
            mock_print.assert_any_call("コンピュータ: 1勝")
            mock_print.assert_any_call("あなたの総合勝利です！")

    def test_print_final_result_computer_win(self):
        with patch('builtins.print') as mock_print:
            source.janken_main.print_final_result(1, 2)
            mock_print.assert_any_call("【最終結果】")
            mock_print.assert_any_call("あなた: 1勝")
            mock_print.assert_any_call("コンピュータ: 2勝")
            mock_print.assert_any_call("コンピュータの総合勝利です！")

if __name__ == '__main__':
    unittest.main()
