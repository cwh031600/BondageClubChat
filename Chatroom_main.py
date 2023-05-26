import Chatroom_fun
import Chatroom_connect
import time

def connect():
    sio = Chatroom_connect.connect()
    Chatroom_fun.log_in(sio,"1544846250","Htn9SpTR4hGa6VT")
    time.sleep(2)
    Chatroom_fun.get_chat_room(sio)
    Chatroom_fun.find_friend(sio)
    Chatroom_fun.chat_room_join(sio)
    sio.wait()
    sio.disconnect()


if __name__ == "__main__":
    '''
    主体函数
    '''
    connect()

