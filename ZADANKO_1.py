import socket
from _thread import *

server = "localhost"
port = 5555

#TODO stwórz socket operujący na ipv4 i protokole TCP
# s = socket.socket(WSTAW ODPOWIEDNIE ARGUMENTY)



try:
    #TODO przypisz socketowi s odpowiedni adres i port (zdefiniowane u góry) funkcją
    # s.bind()



except socket.error as e:
    str(e)

#TODO ustaw socket w tryb nasłuchiwania



print("Server Started")

#TODO stwórz dwuelementową listę players i wpisz do niej dwie liczby
# pierwsza będzie zwiększana do 1000 przez pierwszego klienta, a druga zmniejszana do 0 przez drugiego



strPlayers = str(players[0]) + ',' + str(players[1])

def threaded_client(conn, player):
    conn.sendall(str.encode(strPlayers + ',' + str(player)))
    reply = ""
    while True:
        try:
            info = conn.recv(2048).decode()

            #TODO zaktualizuj listę players, pamiętając że otrzymane dane opisują tylko gracza, który je wysłał



            if not info:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = str(players[0])
                else:
                    reply = str(players[1])

                print("Received: ", info)
                print("Sending : ", reply)

            #TODO zakoduj wiadomość (podobnie jak po wywołaniu funkcji) i wyślij ją do klienta



        except:
            break
        print(players)
    print("Lost connection")
    conn.close()


currentPlayer = 0
while True:
    #TODO zaakceptuj połączenie z zewnątrz funkcją s.accept(), zwróci ona dwie wartości,
    # połączenie za pomocą którego będziemy wysyłać i odbierać dane oraz adres, zapisz te zmienne jako conn i addr



    print("Connected to:", addr)

    #TODO rozpocznij nowy wątek przy pomocy funkncji
    # start_new_thread(<WYWOŁYWANA FUNKCJA>, <OBIEKT TUPLE ZAWIERAJĄCY POŁĄCZENIE I NUMER GRACZA (ARGUMENTY)>)



    currentPlayer += 1
