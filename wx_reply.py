# coding=utf-8
import re
import tuling_robot


def auto_accept_friends(msg):
    # Accept friend card
    new_friend = msg.card.accept()
    # Send msg to friends.
    new_friend.send('I have accepted your request')


def auto_reply(msg):
    # handle_withdraw_msg(msg)
    keyword_reply(msg) or tuling_reply(msg)


def keyword_reply(msg):
    if 'What is your name' in msg.text or 'Who are you' in msg.text:
        return msg.reply('Robot kids with 3 years old')
    pass


def tuling_reply(msg):
    tuling_robot.auto_reply(msg)


def handle_system_msg(msg):
    raw = msg.raw
    # 4: msg revoke code
    if raw['Status'] == 4 and msg.bot.is_forward_revoke_msg:
        forward_revoke_msg(msg)


def forward_revoke_msg(msg):
    revoke_msg_id = re.search('<msgid>(.*?)</msgid>', msg.raw['Content']).group(1)
    for old_msg_item in msg.bot.messages[::-1]:
        # Find the old one which being revoked.
        if revoke_msg_id == str(old_msg_item.id):
            # Judge friend revoke or group revoke
            if old_msg_item.member:
                sender_name = '群「{0}」中的「{1}」'.format(old_msg_item.chat.name, old_msg_item.member.name)
            else:
                sender_name = '「{}」'.format(old_msg_item.chat.name)
            # Card not able to be forwarded
            if old_msg_item.type == 'Card':
                sex = '男' if old_msg_item.card.sex == 1 else 'Female' or 'Unknown'
                msg.bot.master.send(
                    '「{0}」revoked one card：\nName：{1}，Gender：{2}'.format(sender_name, old_msg_item.card.name, sex))
            else:
                # Forward the msg which being revoked.
                old_msg_item.forward(msg.bot.master,
                                     prefix='{} revoked a msg'.format(sender_name,
                                                                      get_msg_chinese_type(old_msg_item.type)))
            return None


# Simply refactor them to replace with English descriptions.
def get_msg_chinese_type(msg_type):
    if msg_type == 'Text':
        return 'Text'
    if msg_type == 'Map':
        return 'Map'
    if msg_type == 'Card':
        return 'Card'
    if msg_type == 'Note':
        return 'Note'
    if msg_type == 'Sharing':
        return 'Sharing'
    if msg_type == 'Picture':
        return 'Picture'
    if msg_type == 'Recording':
        return 'Recording'
    if msg_type == 'Attachment':
        return 'Attachment'
    if msg_type == 'Video':
        return 'Video'
    if msg_type == 'Friends':
        return 'Friends'
    if msg_type == 'System':
        return 'System'
