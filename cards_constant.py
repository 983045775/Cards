# 三种选项

S_ADD = "1"
S_SHOW_ALL = "2"
S_SEACH = "3"
S_EXIT = "0"

str_space = "\t\t\t\t"

# 存储个人信息的列表
cards_list = []


def del_or_change(name):
    while True:
        choose = input("请输入您想要的操作（[1]、修改；[2]、删除；[0]、返回上级菜单）：")
        if choose.__eq__("1"):
            # 修改
            for dict_people in cards_list:
                if dict_people["name"].__eq__(name):
                    # 找到了
                    change_dict(dict_people)
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
    name_str = input("修改姓名(不修改则输入回车)").strip()
    phone_str = input("修改电话号码(不修改则输入回车)").strip()
    qq_str = input("修改QQ号码(不修改则输入回车)").strip()
    mail_str = input("修改邮箱地址(不修改则输入回车)").strip()

    if len(name_str) == 0:
        name_str = dict_msg["name"]
    if len(phone_str) == 0:
        phone_str = dict_msg["phone"]
    if len(qq_str) == 0:
        qq_str = dict_msg["qq"]
    if len(mail_str) == 0:
        mail_str = dict_msg["mail"]
    dict_msg.update({"name": name_str})
    dict_msg.update({"qq": qq_str})
    dict_msg.update({"mail": mail_str})
    dict_msg.update({"phone": phone_str})
