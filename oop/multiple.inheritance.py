class Shape:
    geometric_type = 'Generic Shape'
    def area(self):
        raise NotImplementedError
    def get_geometric_type(self):
        return self.geometric_type

class Plotter:
    def plot(self, ratio, topleft):
        print('Plotting at {}, ration {}.'.format(topleft, ratio))
        