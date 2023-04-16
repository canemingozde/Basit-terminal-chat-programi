import socket as s
import threading as t

# Bana soru sormak için veya daha fazla türkce kaynak için instagram ve GitHub da takip edebilirsin.
# github.com/canemingozde
# instagram.com/canemingozde


class Client:
    host = "127.0.0.1"
    port = 64543
    client = s.socket(s.AF_INET,s.SOCK_STREAM)

    def __init__(self):
        self.client.connect((self.host,self.port))
        print("************** Servara bağlantı başarılı. **************")
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
            print(f"Sunucudan gelen mesaj: {gelen_msj}")



if __name__ == "__main__":
    a = Client()
    a.msj_al()



