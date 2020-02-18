#coding=utf-8
from wxpy import *

import wx_reply
import wx_command
import load


bot = Bot(cache_path=True)
# bot = Bot(cache_path=True, console_qr=True)
load.load_config_to_bot(bot)


@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    wx_reply.auto_accept_friends(msg)


@bot.register(chats=Friend)
def friend_msg(msg):
    if not msg.bot.is_friend_auto_reply:
        return None
    if msg.type == TEXT:
        my_friend=bot.friends().search('enable')[0]
        print (my_friend)
        if my_friend:
            wx_reply.auto_reply(msg)
            return None
    elif msg.type == RECORDING:
        return 'I can not understand'
    else:
        pass


@bot.register(chats=Group)
def group_msg(msg):
    if msg.is_at and msg.bot.is_forward_group_at_msg:
        msg.forward(msg.bot.master, prefix='{0} @ you in {1}：'.format(msg.member.name, msg.chat.name))

    if msg.type == TEXT:
        if msg.bot.is_group_reply:
            if msg.bot.is_group_at_reply:
                if msg.is_at:
                    wx_reply.auto_reply(msg)
            else:
                wx_reply.auto_reply(msg)
    elif msg.type == SHARING and msg.bot.is_listen_sharing and msg.chat in msg.bot.listen_sharing_groups:
        msg.forward(msg.bot.master, prefix='Sharing listener：{1} shared in {0}:'.format(msg.member.name, msg.chat.name))
    else:
        pass
    if msg.bot.is_listen_friend and msg.chat in msg.bot.listen_friend_groups and msg.member.is_friend in msg.bot.listen_friends:
        msg.forward(msg.bot.master, prefix='Listen specific friend：{0} send msg in {1}：'.format(msg.member.is_friend.remark_name or msg.member.nick_name, msg.chat.name))
    return None


@bot.register(msg_types=NOTE)
def system_msg(msg):
    wx_reply.handle_system_msg(msg)


@bot.register(chats=bot.master)
def do_command(msg):
    wx_command.do_command(msg)

bot.join()