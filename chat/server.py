import socket as s
import threading as t
import time 

# Bana soru sormak için veya daha fazla türkce kaynak için instagram ve GitHub da takip edebilirsin.
# github.com/canemingozde
# instagram.com/canemingozde


class Server:
    host = "127.0.0.1"
    port = 64543
    server = s.socket(s.AF_INET,s.SOCK_STREAM)
    for i in range(4):
        time.sleep(0.7)
        print("Server oluşturuluyor...")
        print()

    def __init__(self):
        self.server.bind((self.host,self.port))
        print("************* Server oluşturuldu *************\n")
        self.server.listen(1)
        print("------------- Client dinleniyor. -------------")
        print()
        self.client,self.client_adr = self.server.accept()
        print(f"Bağlanan bilgisayarın ip ve portu: {self.client_adr}")
        print("_________________________________________________________")
       


    def msj_yola(self):
        while True:
            giden_msj = input()
            self.client.send(giden_msj.encode())


    def msj_al(self):
        calistir = t.Thread(target=self.msj_yola)
        calistir.start()
        while True:
            gelen_msj = self.client.recv(1024).decode()
            print(f"İstemciden gelen mesaj: {gelen_msj}")




if __name__ == "__main__":
    a = Server()
    a.msj_al()






