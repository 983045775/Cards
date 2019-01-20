import cards_constant


class CardsUtils:

    def splash_welcome(self):
        """欢迎界面

        """
        print("*" * 50)
        print("欢迎使用【名片管理系统】V2.0.0", end="\r\n\r\n")
        print("%s.新增名片" % cards_constant.S_ADD)
        print("%s.显示全部" % cards_constant.S_SHOW_ALL)
        print("%s.搜索名片" % cards_constant.S_SEACH, end="\r\n\r\n")
        print("%s.退出系统" % cards_constant.S_EXIT)
        print("*" * 50)

    def add_cards(self):
        print("新增名片")
        name_str = input("请输入姓名:").strip()
        phone_str = input("请输入电话号码：").strip()
        qq_str = input("请输入QQ号码：").strip()
        mail_str = input("请输入邮箱地址：").strip()
        if len(name_str) > 0 or len(phone_str) > 0 or len(qq_str) > 0 or len(mail_str) > 0:
            msg_dict = {"name": name_str,
                        "phone": phone_str,
                        "qq": qq_str,
                        "mail": mail_str}
            print(msg_dict)
            print("新增 %s 的名片成功！" % name_str)
            cards_constant.cards_list.append(msg_dict)
        else:
            print("不要输入空")

    def show_all(self):
        if len(cards_constant.cards_list) == 0:
            print("没有人哦")
            return
        print("显示所有名片")
        print(
            "姓名" + cards_constant.str_space + "电话" + cards_constant.str_space + "QQ" + cards_constant.str_space + "邮箱")
        print("=" * 50)
        # 遍历所有列表字典
        i = 1
        for msg_dict in cards_constant.cards_list:
            i += 1
            for key, value in msg_dict.items():
                print("%s" % value, end=cards_constant.str_space)
            if i != (len(msg_dict) - 1):
                print()

    def seach_name(self):
        print("搜索名片")

        seach_name = input("请输入您要查找的姓名：")

        for msg_dict in cards_constant.cards_list:
            # 字典对象
            if msg_dict["name"].__eq__(seach_name):
                # 说明找到了
                print(
                    "姓名" + cards_constant.str_space + "电话" + cards_constant.str_space + "QQ" + cards_constant.str_space + "邮箱")
                print("==" * 50)
                for key, value in msg_dict.items():
                    print("%s" % value, end=cards_constant.str_space)
                # TODO 新的选项
                print()
                cards_constant.del_or_change(msg_dict["name"])
                break
        else:
            print("您要查找的姓名不存在，请确认！")
