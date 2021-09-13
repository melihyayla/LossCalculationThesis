import math


class Cell:

    def __init__(self, edge_length, voc, isc, fill_factor, series_resistance, busbar_number):
        self.voc = voc
        self.isc = isc
        self.edge_length = edge_length
        self.fill_factor = fill_factor
        self.series_resistance = series_resistance
        self.busbar_number = busbar_number

    def radius(self):
        return self.edge_length * math.sqrt(2)

    def area(self):
        areaValue = (0.5 * math.pow(self.radius(), 2) * (
                math.pi / 2 - 2 * (math.acos(self.edge_length / self.radius())))) \
                    + self.edge_length * math.sqrt(math.pow(self.radius(), 2) - math.pow(self.edge_length, 2)) / 100
        return areaValue

    def efficiency(self):
        return self.voc * self.isc * self.fill_factor / self.area() / 100

    def power(self):
        return self.efficiency() * (self.area() / 10)

    def __str__(self) -> str:
        return 'Voc={0}, Isc={1}, Edge Length={2}, Fill Factor={3}, Series Resistance={4}, Radius={5}, \nArea={6}, ' \
               'Efficiency={7}, Power={8}' \
            .format(self.voc, self.isc, self.edge_length, self.fill_factor, self.series_resistance,
                    self.radius(), self.area(), self.efficiency(), self.power())
