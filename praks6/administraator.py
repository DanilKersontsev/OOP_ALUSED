from praks4.administraator import Admin
class Privileegid(Admin):
    def __init__(self, privileegid):
        self.privileegid = []
        self.privileegid.append(privileegid)

admin2 = Privileegid("lubatud lisada kasutajad")
admin2.naita_privileegid()
