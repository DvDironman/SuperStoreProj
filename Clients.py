class Clients:

    def __init__(self,clientid,name,email,address,phonenum,gender):
        self.clientid=clientid
        self.name=name
        self.email=email
        self.address=address
        self.phonenum=phonenum
        self.gender=gender
        if "@" not in self.email or ".com" not in self.email:
            self.email=name+'@fakegmail.com'
        if gender != ("M" or "m") and gender != ("F" or "f"):
            self.gender="uk" #unknown
        if len(str(phonenum))!=9:
            self.phonenum="0000000000"

    def print_me(self):
        print(f'client_id:{self.clientid}\nname:{self.name}\nemail:{self.email}\naddress:{self.address}\nphone_number:{self.phonenum}\ngender:{self.gender}')

    def __str__(self):
        return f'{self.clientid},{self.name},{self.email},{self.address},{self.phonenum},{self.gender}'

    def __repr__(self):
        return str(self)




