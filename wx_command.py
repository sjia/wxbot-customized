#coding=utf-8
import load


def do_command(msg):
    if 'View State' == msg.text:
        msg.reply(load.bot_status_detail(msg.bot))
        return None

    if 'Forward Off' == msg.text:
        msg.bot.is_forward_mode = False
        msg.reply('Succeed')
        return None

    if msg.bot.is_forward_mode:
        forward_result = remote_forward(msg)
        msg.bot.is_forward_mode = False
        msg.reply('Forward msg to：{}，auto quite the mode'.format(forward_result))
        return None

    if 'Friend autoReply on' == msg.text:
        msg.bot.is_friend_auto_reply = True
        msg.reply('Succeed')
        return None

    if 'Friend autoReply off' == msg.text:
        msg.bot.is_friend_auto_reply = False
        msg.reply('Succeed')
        return None

    if 'Group autoReply on' == msg.text:
        msg.bot.is_group_reply = True
        msg.reply('Succeed')
        return None

    if 'Group autoReply off' == msg.text:
        msg.bot.is_group_reply = False
        msg.reply('Succeed')
        return None

    if 'Open @ in group' == msg.text:
        msg.bot.is_group_at_reply = True
        msg.reply('Succeed')
        return None

    if 'Close @ in group' == msg.text:
        msg.bot.is_group_at_reply = False
        msg.reply('Succeed')
        return None

    if 'Open group forward' == msg.text:
        msg.bot.is_forward_group_at_msg = True
        msg.reply('Succeed')
        return None

    if 'Close group forward' == msg.text:
        msg.bot.is_forward_group_at_msg = False
        msg.reply('Succeed')
        return None

    if 'Open revoke mode' == msg.text:
        msg.bot.is_forward_revoke_msg = True
        msg.reply('Succeed')
        return None

    if 'Close revoke mode' == msg.text:
        msg.bot.is_forward_revoke_msg = False
        msg.reply('Succeed')
        return None

    if 'Open listener mode' == msg.text:
        msg.bot.is_listen_friend = True
        # reload the configuration info
        errmsg = load.load_listen_friend(msg.bot)
        if errmsg:
            msg.reply('Open listener mode failed，{}'.format(errmsg))
        else:
            msg.reply('Listener mode on，listen {1} in {0}'.format(str(msg.bot.listen_friend_groups), str(msg.bot.listen_friends)))
        return None

    if 'Close listener mode' == msg.text:
        msg.msg.bot.is_listen_friend = False
        msg.reply('Close listener mode')
        return None

    if 'Open listener mode' == msg.text:
        msg.bot.is_listen_sharing = True
        errmsg = load.load_listen_sharing_groups(msg.bot)
        if errmsg:
            msg.reply('failed，{}'.format(errmsg))
        else:
            msg.reply('Succeed，to listen these groups：{}'.format(str(msg.bot.listen_sharing_groups)))
        return None

    if 'Close listener mode' == msg.text:
        msg.bot.is_listen_sharing = False
        msg.reply('Succeed')
        return None

    if 'Open forward mode' == msg.text:
        msg.bot.is_forward_mode = True
        # 重新加载配置信息
        errmsg = load.load_forward_groups(msg.bot)
        if errmsg:
            msg.reply('Failed，{}'.format(errmsg))
        else:
            msg.reply('Succeed，send info to me and I will forward to:{0}，if not you can tell me：{1}'.format(str(msg.bot.forward_groups), 'Close forward mode'))
        return None

    if 'Sleep' == msg.text:
        remote_down(msg)
        msg.reply('Sleep mode, all functions in sleep.')
        return None

    if 'Open' == msg.text:
        remote_reup(msg)
        msg.reply('Succeed')
        return None

    if 'Quit' == msg.text:
        msg.reply('Exiting...')
        msg.bot.logout()
        return None

    if 'View state' == msg.text:
        msg.reply(load.bot_status_detail(msg.bot))
        return None

    msg.reply('Not understand the info：{}'.format(msg.text))
    return None

# Open all registers
def remote_reup(msg):
    msg.bot.registered.enable()

def remote_down(msg):
    do_command_register = msg.bot.registered.get_config(msg)
    msg.bot.registered.remove(do_command_register)
    msg.bot.registered.disable()
    msg.bot.registered.append(do_command_register)

def remote_forward(msg):
    forward_groups = []
    for group in msg.bot.forward_groups:
        msg.forward(group, suffix='sjia-forward')
        forward_groups.append(group.name)
    return forward_groups
