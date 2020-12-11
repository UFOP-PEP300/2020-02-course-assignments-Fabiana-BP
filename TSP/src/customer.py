class Customer:
    _id = int()
    _xCoord = float()
    _yCoord = float()
    def __init__(self, id, xCoord, yCoord):
        self._id = id
        self._xCoord = xCoord
        self._yCoord = yCoord

    def get_id(self):
        return self._id

    def get_xCoord(self):
        return self._xCoord
    
    def get_yCoord(self):
        return self._yCoord

    def __repr__(self):
        return str(self._id)
    
    def __str__(self):
        return str(self._id)
    
    def __eq__(self,other):
        return self._id == other.get_id()