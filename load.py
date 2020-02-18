#coding=utf-8
from wxpy import *

import config

logger = logging.getLogger('itchat')


def load_config_to_bot(bot):
    bot_status = 'Logon success.'
    if not config.bot_master_name:
        bot.master = bot.file_helper
        bot_status += '\nNo admin set.\n\n'
    else:
        master = search_friend(bot, config.bot_master_name)
        # Find admin
        if master:
            bot.master = master
            bot_status += '\nAdmin set：{0}, click here to view guide->' \
                          'https://github.com/pig6/wxrobot\n\n'.format(config.bot_master_name)
        else:
            bot.master = bot.file_helper
            bot_status += '\nFind friend with name {}, no Admin here！\n\n'.format(config.bot_master_name)
    bot.is_friend_auto_reply = config.is_friend_auto_reply
    bot.is_group_reply = config.is_group_reply
    bot.is_group_at_reply = config.is_group_at_reply
    bot.is_listen_friend = config.is_listen_friend
    bot.is_forward_mode = config.is_forward_mode
    bot.is_listen_sharing = config.is_listen_sharing
    bot.is_forward_revoke_msg = config.is_forward_revoke_msg
    bot.is_forward_group_at_msg = config.is_forward_group_at_msg
    # Load friends and groups
    load_listen_friend(bot)
    load_forward_groups(bot)
    load_listen_sharing_groups(bot)
    # Send robot status
    bot_status = bot_status if 'File Transfer' in bot_status else bot_status + bot_status_detail(bot)
    bot.master.send(bot_status)
    logger.info(bot_status)


def load_listen_friend(bot):
    if bot.is_listen_friend:
        bot.listen_friends = search_friends(bot, config.listen_friend_names)
        if not bot.listen_friends:
            bot.listen_friends = []
            bot.is_listen_friend = False
            return 'Friend {} is not found'.format(str(config.listen_friend_names))

        bot.listen_friend_groups = bot.groups().search(config.listen_friend_groups)
        if len(bot.listen_friend_groups) < 1:
            bot.listen_friend_groups = []
            bot.is_listen_friend = False
            return 'Group {} is not found'.format(config.listen_friend_groups)
    return None


def load_forward_groups(bot):
    if bot.is_forward_mode:
        bot.forward_groups = bot.groups().search(config.forward_groups)
        if len(bot.forward_groups) < 1:
            bot.forward_groups = []
            bot.is_forward_mode = False
            return 'Forward group with {} is not found'.format(config.forward_groups)
    return None


def load_listen_sharing_groups(bot):
    if bot.is_listen_sharing:
        bot.listen_sharing_groups = bot.groups().search(config.listen_sharing_groups)
        if len(bot.listen_sharing_groups) < 1:
            bot.listen_sharing_groups = []
            bot.is_listen_sharing = False
            return 'Sharing group {} is not found'.format(config.listen_sharing_groups)
    return None


def bot_status_detail(bot):
    bot_config_status = 'Robot configure state：'
    # bot_config_status += '\nRobot admin：{0} {1}'.format(bot.master.remark_name, bot.master.nick_name)
    if bot.is_forward_mode:
        bot_config_status += '\nForward mode is on，info would be switched to {}.'.format(str(bot.forward_groups))
    bot_config_status += '\nis friend auto reply：{}'.format(('Yes' if bot.is_friend_auto_reply else 'No'))

    bot_config_status += '\nGroup reply：{}'.format(('Yes' if bot.is_group_reply else 'No'))
    if bot.is_group_reply:
        bot_config_status += ',@ for reply：{}'.format('Yes' if bot.is_group_at_reply else 'No')

    bot_config_status += '\nGroup @ on：{}'.format(('Yes' if bot.is_forward_group_at_msg else 'No'))

    bot_config_status += '\nRevoke available：{}'.format(('Yes' if bot.is_forward_revoke_msg else 'No'))

    bot_config_status += '\nListen friend：{}'.format('Yes' if bot.is_listen_friend else 'No')
    if bot.is_listen_friend:
        bot_config_status += ', Listen {1} in Group {0}'.format(str(bot.listen_friend_groups), str(bot.listen_friends))

    bot_config_status += '\nForward mode: No'

    bot_config_status += '\nListener mode:{}'.format('Yes' if bot.is_listen_sharing else 'No')
    if bot.is_listen_sharing:
        bot_config_status += '，Sharing groups are:{}'.format(str(bot.listen_sharing_groups))
    return bot_config_status


def search_friend(bot, name):
    nick_name_friend = None
    for friend in bot.friends():
        if getattr(friend, 'remark_name', None) == name:
            return friend
        elif not nick_name_friend and getattr(friend, 'nick_name', None) == name:
            nick_name_friend = friend
    return nick_name_friend or None


def search_friends(bot, names):
    split_names = names.split('|')
    result_list = []
    for friend in bot.friends():
        if getattr(friend, 'remark_name', None) in split_names:
            result_list.append(friend)
        elif getattr(friend, 'nick_name', None) in split_names:
            result_list.append(friend)
    return result_list
