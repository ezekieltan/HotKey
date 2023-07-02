class RecentOperations:
    def __init__(self, max_size=10):
        self.max_size = max_size
        self.recentOperations = []

    def addOperation(self, key, down):
        self.recentOperations.append({'key': key.upper(), 'down': down})
        if len(self.recentOperations) > self.max_size:
            self.recentOperations.pop(0)

    def getLastNItems(self, n):
        if (len(self.recentOperations) == 0):
            return None
        if (len(self.recentOperations) <= n):
            return self.recentOperations
        return self.recentOperations[-n:]

    def getLast(self):
        if (len(self.recentOperations) == 0):
            return None
        return self.recentOperations[-1:][0]

    def getAll(self):
        return self.recentOperations
