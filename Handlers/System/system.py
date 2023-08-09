import os
from Handlers.Date.date import YEAR, MONTH, DAY
from Requests.Post.msg import Message

def write_file(path: str, data: bytes):
    with open(path, "wb") as file:
        file.write(data)

def check_folder(path: str):
    if os.path.exists(path) == False:
        os.mkdir(path)

def save_data(path: str, msg: Message, i: int):
    if i == YEAR:
        check_folder(path + msg.date.year)
        save_data(path + msg.date.year, msg, MONTH)
        return
    if i == MONTH:
        check_folder(path + msg.date.month)
        save_data(path + msg.date.month, msg, DAY)
        return
    if i == DAY:
        check_folder(path + msg.date.day)
        save_data(path + msg.date.day, msg, DAY+1)
        return
    write_file(path+msg.filename, msg.data)