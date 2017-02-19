import socket
import winsound

import requests
from pygame import mixer

import general





#BEEP1 = pyglet.media.load('beep1.ogg')
#BEEP2 = pyglet.media.load('beep2.ogg')
#BEEP3 = pyglet.media.load('beep3.ogg')
#BEEP4 = pyglet.media.load('beep4.ogg')
#s_to_file = {"BEEP1": BEEP1, "BEEP2": BEEP2, "BEEP3": BEEP3, "BEEP4": BEEP4}


def main():
    mixer.init()
    server_socket = socket.socket()
    server_socket.bind(("0.0.0.0", 7755))
    server_socket.listen(1)
    client_socket, client_address = server_socket.accept()
    run = True

    while run:
        notes = general.recv(client_socket)
        print notes
        if notes == False:
            winsound.PlaySound("Pain.wav", winsound.SND_FILENAME)
            try:
                requests.post("http://10.10.11.68", json={"command": "take", "param": 60})
            except:
                pass
        else:
            for note in notes:
                for _ in range(note[2]):
                    winsound.Beep(note[0], note[1])
                    # time.sleep(0.1)

        general.send(client_socket, "good")


main()