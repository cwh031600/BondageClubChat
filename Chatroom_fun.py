import time
def socket_emit(sio,set,input):
    '''
    input为传递信息的字符串
    sio为连接端口
    set-str类型 用于设置协议种类
    input-str类型 用于主体信息传输
    set当前已知种类
    "AccountLogin"----用于用户登录
    "AccountUpdate"----用于用户更新
    '''
    sio.emit(set, input)
    #sio.emit('AccountLogin', {'AccountName': '1544846250',"Password":'Htn9SpTR4hGa6VT'})

def log_in(sio,name,password):
    '''
    登录函数name,password分别为用户名和密码
    '''
    #str_input = '{"AccountName":' + str(name) + ',"Password":' + str(password) + '}'
    str_dic = {"AccountName":str(name),"Password":str(password)}
    #str_dic_json = json.dumps(str_dic)
    #print(str_dic_json)
    socket_emit(sio,"AccountLogin",str_dic)
    Account_Up_date(sio)#用户信息更新

def get_chat_room(sio):
    '''
    获取chatroom的列表
    '''
    socket_emit(sio,"ChatRoomSearch",{"Query":"","Language":"","Space":"","Game":"","FullRooms":"true"})
    time.sleep(5)
    #socket_emit(sio,"ChatRoomSearch",{"Query":"","Language":"","Space":"","Game":"","FullRooms":"true"})

def chat_room_join(sio):
    '''
    加入房间
    '''
    #42["ChatRoomJoin",{"Name":"031600"}]
    socket_emit(sio,"ChatRoomJoin",{"Name":"031600"})

def Account_Up_date(sio):
    '''
    用于登录的用户信息更新
    '''
    #42["ChatRoomJoin",{"Name":"031600"}]
    socket_emit(sio,"AccountUpdate",{"BlockItems":{},"LimitedItems":{"ItemMisc":{"CombinationPadlock":[""],"PasswordPadlock":[""],"TimerPasswordPadlock":[""],"HighSecurityPadlock":[""]}},"FavoriteItems":{"ItemNeckAccessories":{"CollarCowBell":[""]}},"HiddenItems":[]})
    socket_emit(sio,"AccountUpdate",{"ConfiscatedItems":[]})

def find_friend(sio):
    '''
    查询在线好友
    '''
    socket_emit(sio,"AccountQuery",{"Query":"OnlineFriends"})