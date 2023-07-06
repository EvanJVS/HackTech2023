class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if carType == 1:
            if self.big >= 1:
                self.big -= 1
                return True
        if carType == 2:
            if self.medium >= 1:
                self.medium -= 1
                return True
        if carType == 3:
            if self.small >= 1:
                self.small -= 1
                return True
        return False
