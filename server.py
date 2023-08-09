import tkinter
from tkinter import filedialog
from flask import Flask, request
from Requests.Get.localip import get_local_ip
from Requests.Post.msg import Message
from Handlers.System.system import save_data
import threading
from Handlers.System.system import check_folder

# API Methods
GET = 'GET'
POST = 'POST'

# API Endpoints
LOCAL_IP_ENDPOINT = "/local-ip"
IMAGES_ENDPOINT = '/img'
VIDEOS_ENDPOINT = '/video'

PORT = 3690
app = Flask("Photo Sync")

# Paths
BASE_PATH = 'media'
IMG_PATH = 'images/'
VIDEO_PATH = 'videos/'

# Methods
def local_ip():
    ip, _ = get_local_ip()
    return str(ip)

def create_server():
    ip = local_ip()
    app.run(host=ip, port=PORT)

def handle_path_label():
    global BASE_PATH
    BASE_PATH = filedialog.askdirectory()
    BASE_PATH += "/"
    path_label.configure(text=BASE_PATH)

def handle_thread():
    server_thread = threading.Thread(target=create_server)
    server_thread.start()

IP_ADDRESS = "IP ADDRESS: " + local_ip()

# API Methods
@app.route(IMAGES_ENDPOINT, methods=[POST])
def images():
    msg = Message(request.get_json())
    check_folder(BASE_PATH+IMG_PATH)
    save_data(path=BASE_PATH+IMG_PATH, msg=msg, i=0)
    return "Image saved successfully!", 200

@app.route(VIDEOS_ENDPOINT, methods=[POST])
def videos():
    msg = Message(request.get_json())
    check_folder(path=BASE_PATH+VIDEO_PATH)
    save_data(path=BASE_PATH+VIDEO_PATH, msg=msg, i=0)
    return "Video saved successfully!", 200



window = tkinter.Tk(screenName="PhotoSync")
window.configure(bg="black")
window.geometry("420x140")
window.title("PhotoSync")
window.iconbitmap("./photo.ico")

# UI Components
ip_label = tkinter.Label(window, text=IP_ADDRESS, bg="black", fg='white')
path_label = tkinter.Label(window, text=BASE_PATH, bg="black", fg='white')
select_folder_btn = tkinter.Button(window, text="Select Folder", command=handle_path_label, bg="black")
server_btn = tkinter.Button(window, text="Create Server", command=handle_thread, bg="black")

# Render Components
path_label.pack()
select_folder_btn.pack()
ip_label.pack()
server_btn.pack()

# Threads


# Show Window
window.mainloop()