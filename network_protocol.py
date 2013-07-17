from random import randint

class NetworkProtocol:

    """
    """

    def __init__(self, address_length, address_depth):
        self.address_length = address_length
        self.address_depth = address_depth

    def random_address(self):
        res = []
        for i in range(self.address_length):
            rand = randint(1, self.address_depth)
            res.append(rand)
        return res

    def subnet_mask(self, subnet):
        # TODO
        pass

if __name__ == "__main__":

    protocol = NetworkProtocol(55, 420)
    res = protocol.random_address()
    print str(res)
