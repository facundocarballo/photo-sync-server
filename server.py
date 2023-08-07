import tkinter as tk
from flask import Flask, request
from Requests.Get.IP.localip import get_local_ip
from Requests.Post.msg import Message
from Handlers.System.system import save_data
import threading

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
BASE_PATH = 'media/'
IMG_PATH = 'images/'
VIDEO_PATH = 'videos/'

# Methods
def local_ip():
    ip, _ = get_local_ip()
    return str(ip)

def create_server():
    ip = local_ip()
    app.run(host=ip,port=PORT)

IP_ADDRESS = "IP ADDRESS: " + local_ip()

# API Methods
@app.route(IMAGES_ENDPOINT, methods=[POST])
def images():
    msg = Message(request.get_json())
    save_data(path=BASE_PATH+IMG_PATH, msg=msg, i=0)
    return "Image saved successfully!", 200

@app.route(VIDEOS_ENDPOINT, methods=[POST])
def videos():
    msg = Message(request.get_json())
    save_data(path=BASE_PATH+VIDEO_PATH, msg=msg, i=0)
    return "Video saved successfully!", 200



window = tk.Tk(screenName="PhotoSync")
window.geometry("720x200")
window.title("PhotoSync")

# UI Components
server_btn = tk.Button(window, text=IP_ADDRESS, command=None)

# Render Components
server_btn.pack()

# Threads
server_thread = threading.Thread(target=create_server)
server_thread.start()

# Show Window
window.mainloop()