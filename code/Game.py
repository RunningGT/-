# 顺手写的猜拳小程序
import random
import os


def clear_screen():
    if os.name == 'nt':
        os.system('cls')


def play_with_players():
    sum_wins = 0
    player1_wins = 0
    player2_wins = 0

    while True:
        clear_screen()

        player1_choice = get_player_choice("玩家一")
        player2_choice = get_player_choice("玩家二")

        print("玩家一出拳：%d" % player1_choice)
        print("玩家二出拳：%d" % player2_choice)

        # 比较大小
        if (player1_choice == 1 and player2_choice == 2) or (player1_choice == 2 and player2_choice == 3) or (
                player1_choice == 3 and player2_choice == 1):
            print("玩家一胜利")
            player1_wins += 1
        elif (player2_choice == 1 and player1_choice == 2) or (player2_choice == 2 and player1_choice == 3) or (
                player2_choice == 3 and player1_choice == 1):
            print("玩家二胜利")
            player2_wins += 1
        else:
            print("平局")

        sum_wins += 1

        # 每一次比完，询问是否继续
        if not continue_game():
            # 只有在用户选择“0”不继续游戏后才输出统计结果
            print("================游戏结束================")
            print("一共玩了%d次" % sum_wins)
            print("玩家一胜利%d次" % player1_wins)
            print("玩家二胜利%d次" % player2_wins)
            print("平局%d次" % (sum_wins - player1_wins - player2_wins))
            print("程序结束")
            # 输出统计结果后暂停
            os.system("pause")
            break


def play_with_computer():
    sum_wins = 0
    player_wins = 0
    computer_wins = 0

    while True:
        clear_screen()

        player_choice = get_player_choice("玩家")
        computer_choice = random.randint(1, 3)

        print("玩家出拳：%d" % player_choice)
        print("电脑出拳：%d" % computer_choice)

        # 比较大小
        if (player_choice == 1 and computer_choice == 2) or (player_choice == 2 and computer_choice == 3) or (
                player_choice == 3 and computer_choice == 1):
            print("玩家胜利")
            player_wins += 1
        elif (computer_choice == 1 and player_choice == 2) or (computer_choice == 2 and player_choice == 3) or (
                computer_choice == 3 and player_choice == 1):
            print("电脑胜利")
            computer_wins += 1
        else:
            print("平局")

        sum_wins += 1

        # 每一次比完，询问是否继续
        if not continue_game():
            # 只有在用户选择“0”不继续游戏后才输出统计结果
            print("================游戏结束================")
            print("一共玩了%d次" % sum_wins)
            print("玩家胜利%d次" % player_wins)
            print("电脑胜利%d次" % computer_wins)
            print("平局%d次" % (sum_wins - player_wins - computer_wins))
            print("程序结束")
            os.system("pause")
            break


def get_player_choice(player_name):
    while True:
        try:
            choice = int(input(f"{player_name}请出拳（1-石头  2-剪刀  3-布）："))
            if 1 <= choice <= 3:
                return choice
            else:
                print("错误：请输入有效的数字（1-3之间的整数）")
        except ValueError:
            print("错误：请输入有效的数字")


def continue_game():
    choice = input("按0结束游戏，按回车或其他键继续：")
    return choice != '0'


def main():
    while True:
        clear_screen()
        print("====== 猜拳游戏 ======")
        print("1. 模式一：玩家一与玩家二轮流输入")
        print("2. 模式二：电脑与玩家轮流输入")
        print("0. 退出游戏")

        try:
            mode_choice = int(input("请选择模式: "))
        except ValueError:
            print("错误：请输入有效的数字")
            continue

        if mode_choice == 1:
            play_with_players()
        elif mode_choice == 2:
            play_with_computer()
        elif mode_choice == 0:
            print("程序结束")
            break
        else:
            print("错误：请输入有效的选项")


if __name__ == "__main__":
    main()
