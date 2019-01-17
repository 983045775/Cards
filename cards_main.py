#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import cards_tools

while True:
    # 欢迎界面
    cards_tools.splash_welcome()
    # 取到输入值
    choose = input("请选择希望执行的操作")
    print("您选择的操作是:%s" % choose)
    print("-" * 50)

    if choose in [cards_tools.S_ADD, cards_tools.S_SHOW_ALL, cards_tools.S_SEACH]:
        if choose.__eq__(cards_tools.S_ADD):
            # 添加
            cards_tools.add_cards()
        elif choose.__eq__(cards_tools.S_SHOW_ALL):
            # 查看所有
            cards_tools.show_all()
            pass
        elif choose.__eq__(cards_tools.S_SEACH):
            # 搜索
            cards_tools.seach_name()
            pass
    elif choose.__eq__(cards_tools.S_EXIT):
        print("欢迎再次使用名片系统！")
        print("-" * 50)
        break
    else:
        print("您的输入有误，请检查后重新输入！")

    print()
    print("-" * 50)
