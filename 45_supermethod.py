class intro():
    def sent(self):
        print("Hello, This is introduction part.")

class body(intro):
    def sent(self):
        super().sent()
        print("This is body part.")

class conc(body):
    def sent(self):
        super().sent()
        print("This is concluion part.")

c=conc()
c.sent()