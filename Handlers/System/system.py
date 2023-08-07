import os
from Handlers.Date.date import YEAR, MONTH, DAY
from Requests.Post.msg import Message

def write_file(path: str, data: bytes):
    with open(path, "wb") as file:
        file.write(data)

def check_folder(path: str, msg: Message, i: int):
    if os.path.exists(path) == False:
        os.mkdir(path)
    save_data(path, msg, i+1)

def save_data(path: str, msg: Message, i: int):
    if i == YEAR:
        check_folder(path + msg.date.year, msg, YEAR)
        return
    if i == MONTH:
        check_folder(path + msg.date.month, msg, MONTH)
        return
    if i == DAY:
        check_folder(path + msg.date.day, msg, DAY)
        return
    write_file(path+msg.filename, msg.data)