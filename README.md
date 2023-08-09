# PhotoSync Server

The server will focused on get the images and videos from the smartphone and then organize those assets in folders by **year**, **month** and **days**.

![Example of Folders](https://i.ibb.co/TRzQVHV/Folders-example.png)

## How Can I create a server?
You can create a PhotoSync Server following this steps:
1. You have to download this Desktop App (PhotoSync Server)
2. Open the PhotoSync Server App.
![PhotoSync Server Open](https://i.ibb.co/Vp8jpjZ/Captura-de-pantalla-2023-08-09-a-la-s-10-33-32.png)
3. Select the folder where you want to store your images and videos.
    1. Press the **Select Folder** Button.
    ![Select Button](https://i.ibb.co/HF3VQXT/Captura-de-pantalla-2023-08-09-a-la-s-10-39-52.png)

    2. Choose the folder where you want to store your images and videos.
    ![Choose folder](https://i.ibb.co/VJJRtyB/Captura-de-pantalla-2023-08-09-a-la-s-10-41-21.png)
    
4. Press the **Crea te Server** Button.
Done it, you already have the PhotoSync Server running waiting for the connection of the smartphone.

## Can I use this repo to create the Server?
Yes, you can clone this repo and run the server without problems.
1. Clone this repo
```bash
git clone https://github.com/facundocarballo/photo-sync-server.git
```
2. In the terminal, go to where you allocate this repo.
3. Check if you have python3 installed
```bash
python3 --version
```
> If you don't have python3 installed, you have to install it to run this server.
4. Run this command
```bash
python3 server.py
```