#encoding=utf-8
import itchat
import time

# itchat.login()
# itchat.auto_login(enableCmdQR=True)


@itchat.msg_register('Text')
def auto_reply(msg):
    user_account = 'wtt2011-'
    # 当消息不是由自己发出的时候
    if msg['FromUserName'] == user_account or msg['FromUserName'] == u'@f37dae1f3971f702ed2fec397d38aca51104354acc031351437325a99a43aa14':
        # 发送一条提示给文件助手
        # itchat.send_msg(u"[%s]收到好友@%s 的信息：%s\n" %
        #                 (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg['CreateTime'])),
        #                  msg['User']['NickName'],
        #                  msg['Text']), 'filehelper')
        print msg
        itchat.send(u'自动回复已开启，到家之前不理你。（手动微笑）',user_account)
        # 回复给好友
        return u'[自动回复]您好，我现在有事不在，一会再和您联系。\n已经收到您的的信息：%s\n' % (msg['Text'])

if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    itchat.send(u'你好', 'filehelper')
    # itchat.send_msg(u'到家之前不理你！哼。发自python', 'wtt2011-')
    # 获取自己的UserName
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    print myUserName
    print itchat.get_friends(update=True)[0],
    itchat.run()