class Busbar:

    # Yapı gelecek feedbacke göre değişebilir
    def __init__(self, edge_resistance, middle_resistance):
        self.edge_resistance = edge_resistance
        self.middle_resistance = middle_resistance

    def total_resistance(self):
        return self.edge_resistance + self.middle_resistance

    def __str__(self) -> str:
        return 'Edge_resistance={0}, Middle_resistance={1}'.format(self.edge_resistance, self.middle_resistance)
