'''
用于初始化socketio
功能 :1.返回sio接口 2.定义各项事件相应
'''
import socketio
header = {
        'Host': 'bondage-club-server.herokuapp.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Origin': 'https://www.bondageprojects.elementfx.com',
        'Connection': 'keep-alive',
        'Referer': 'https://www.bondageprojects.elementfx.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
}
def connect():
    '''
    socketio函数初始化与调用
    '''
    # standard Python  初始化socket
    #sio = socketio.Client()
    sio = socketio.Client(logger=True, engineio_logger=True)
    #此方法用于处理登录返回信息
    @sio.on('LoginResponse')
    def on_message(data):
        print('成功登录')
        print("您的用户名是:" + data["Name"])
        print("你的登录id是:" + str(data["MemberNumber"]))
    
    '''
    此方法用于处理实时在线人数
    '''
    @sio.on('ServerInfo')
    def on_message(data):
        #print('I received a ServerInfo!!!')
        #print(type(data))
        print("当前在线人数为：" + str(data['OnlinePlayers']))

    '''
    此方法用于处理当前房间
    '''
    @sio.on('ChatRoomSearchResult')
    def on_message(data):
        #print('I received a ServerInfo!!!')
        #print(type(data))
        list_room = []
        print(type(data))
        print(data)
        for dic in data:
            list_room.append(dic["Name"])
        print("当前所有房间：")
        print(list_room)

    @sio.on('ChatRoomMessage')
    def on_message(data):
        Data_Type = data["Type"]
        if Data_Type == "Chat":
            print(str(data["Sender"]) + "说：" + str(data["Content"]))
        elif Data_Type == "Status":
            if data["Content"] == "Talk":
                print(str(data["Sender"]) + "正在输入")
        print(data)

    '''
    返回好友列表事件处理
    '''
    @sio.on('AccountQueryResult')
    def on_message(data):
        print("当前在线好友:")
        Friend_list = data["Result"]
        for i in Friend_list:
            print(i)

    #对于没有事件处理程序的任何事件，都会调用“包罗万象”的事件处理程序。'*'您可以使用as 事件名称定义一个包罗万象的处理程序：
    @sio.on('*')
    def catch_all(event, data):
        print("尚未被处理的事件：" + str(event))
        print(data)

    #连接，连接错误，断开函数
    @sio.event
    def connect():
        print("I'm connected!")

    @sio.event
    def connect_error(data):
        print("The connection failed!")

    @sio.event
    def disconnect():
        print("I'm disconnected!")
    sio.connect('https://bondage-club-server.herokuapp.com/socket.io/',headers=header,wait_timeout = 10)#连接聊天室
    print('my sid is', sio.sid)
    print("模拟登录")
    return sio