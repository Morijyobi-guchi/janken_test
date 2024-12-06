from source import player
from source import computer
from source import janken_judge


def play_round(round_number, player_win, computer_win):
    """1ラウンドのじゃんけんを行う処理"""
    print(f"----- ラウンド {round_number} -----")
    computer_hand = computer.computer_pon()
    player_hand = player.player_pon()
    result = janken_judge.judge(computer_hand, player_hand)

    print(f"あなたの手: {player_hand}")
    print(f"コンピューターの手: {computer_hand}\n")

    if result == 'draw':
        print("あいこです！再度対決！\n")
        return player_win, computer_win, False  # ラウンドを繰り返す
    else:
        if result == 'player_win':
            player_win += 1
            print("あなたの勝ちです！\n")
        else:
            computer_win += 1
            print("コンピューターの勝ちです！\n")
        return player_win, computer_win, True  # ラウンドを進める

def print_final_result(player_win, computer_win):
    """最終結果を表示する処理"""
    print("【最終結果】")
    print(f"あなた: {player_win}勝")
    print(f"コンピュータ: {computer_win}勝")
    if player_win >= computer_win:
        print("あなたの総合勝利です！")
    else:
        print("コンピュータの総合勝利です！")

def main():
    player_win = 0
    computer_win = 0
    round_number = 1

    while round_number <= 3:
        player_win, computer_win, proceed = play_round(round_number, player_win, computer_win)
        if proceed:
            round_number += 1

    print_final_result(player_win, computer_win)

if __name__ == '__main__':
    main()
