class Shape:
    geometric_type = 'Generic Shape'
    def area(self):
        raise NotImplementedError
    def get_geometric_type(self):
        return self.geometric_type
