# 三种选项

S_ADD = "1"
S_SHOW_ALL = "2"
S_SEACH = "3"
S_EXIT = "0"

str_space = "\t\t\t\t"

# 存储个人信息的列表
cards_list = []


def splash_welcome():
    """欢迎界面

    """
    print("*" * 50)
    print("欢迎使用【名片管理系统】V2.0.0", end="\r\n\r\n")
    print("%s.新增名片" % S_ADD)
    print("%s.显示全部" % S_SHOW_ALL)
    print("%s.搜索名片" % S_SEACH, end="\r\n\r\n")
    print("%s.退出系统" % S_EXIT)
    print("*" * 50)


def add_cards():
    print("新增名片")
    name_str = input("请输入姓名:")
    phone_str = input("请输入电话号码：")
    qq_str = input("请输入QQ号码：")
    mail_str = input("请输入邮箱地址：")

    msg_dict = {"name": name_str,
                "phone": phone_str,
                "qq": qq_str,
                "mail": mail_str}
    print(msg_dict)
    print("新增 %s 的名片成功！" % name_str)
    cards_list.append(msg_dict)


def show_all():
    if len(cards_list) == 0:
        print("没有人哦")
        return
    print("显示所有名片")
    print("姓名" + str_space + "电话" + str_space + "QQ" + str_space + "邮箱")
    print("=" * 50)
    # 遍历所有列表字典
    i = 1
    for msg_dict in cards_list:
        i += 1
        for key, value in msg_dict.items():
            print("%s" % value, end=str_space)
        if i != (len(msg_dict) - 1):
            print()


def seach_name():
    print("搜索名片")

    seach_name = input("请输入您要查找的姓名：")

    for msg_dict in cards_list:
        # 字典对象
        if msg_dict["name"].__eq__(seach_name):
            # 说明找到了
            print("姓名" + str_space + "电话" + str_space + "QQ" + str_space + "邮箱")
            print("==" * 50)
            for key, value in msg_dict.items():
                print("%s" % value, end=str_space)
            # TODO 新的选项
            print()
            del_or_change(msg_dict["name"])
            break
    else:
        print("您要查找的姓名不存在，请确认！")


def del_or_change(name):
    while True:
        choose = input("请输入您想要的操作（[1]、修改；[2]、删除；[0]、返回上级菜单）：")
        if choose.__eq__("1"):
            # 修改
            for dict_people in cards_list:
                if dict_people["name"].__eq__(name):
                    # 找到了
                    new_card = change_dict(dict_people)
                    cards_list.remove(dict_people)
                    cards_list.append(new_card)
            break
        elif choose.__eq__("2"):
            # 删除
            for dict_people in cards_list:
                if dict_people["name"].__eq__(name):
                    cards_list.remove(dict_people)
                    print("删除成功")
            break
        elif choose.__eq__("0"):
            # 退出
            break
        else:
            print("输入错误,请重来")


def change_dict(dict_msg):
    name_str = input("修改姓名(不修改则输入回车)")
    phone_str = input("修改电话号码(不修改则输入回车)")
    qq_str = input("修改QQ号码(不修改则输入回车)")
    mail_str = input("修改邮箱地址(不修改则输入回车)")

    if (not name_str.isspace()) and len(name_str) == 0:
        name_str = dict_msg["name"]
    if (not phone_str.isspace()) and len(phone_str) == 0:
        phone_str = dict_msg["phone"]
    if (not qq_str.isspace()) and len(qq_str) == 0:
        qq_str = dict_msg["qq"]
    if (not mail_str.isspace()) and len(mail_str) == 0:
        mail_str = dict_msg["mail"]

    msg_dict = {"name": name_str,
                "phone": phone_str,
                "qq": qq_str,
                "mail": mail_str}
    return msg_dict