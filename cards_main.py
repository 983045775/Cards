#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3

from cards_tools import CardsUtils

cards_utils = CardsUtils()

while True:
    # 欢迎界面
    cards_utils.splash_welcome()
    # 取到输入值
    choose = input("请选择希望执行的操作")
    print("您选择的操作是:%s" % choose)
    print("-" * 50)

    if choose in [cards_utils.S_ADD, cards_utils.S_SHOW_ALL, cards_utils.S_SEACH]:
        if choose.__eq__(cards_utils.S_ADD):
            # 添加
            cards_utils.add_cards()
        elif choose.__eq__(cards_utils.S_SHOW_ALL):
            # 查看所有
            cards_utils.show_all()
            pass
        elif choose.__eq__(cards_utils.S_SEACH):
            # 搜索
            cards_utils.seach_name()
            pass
    elif choose.__eq__(cards_utils.S_EXIT):
        print("欢迎再次使用名片系统！")
        print("-" * 50)
        break
    else:
        print("您的输入有误，请检查后重新输入！")

    print()
    print("-" * 50)
