from address import Address

class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address  # экземпляр класса Address
        self.from_address = from_address  # экземпляр класса Address
        self.cost = cost  # стоимость отправления
        self.track = track  # трек-номер отправления