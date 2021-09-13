class Ribbon:

    def __init__(self, thickness, width, resistivity):
        self.thickness = thickness
        self.width = width
        self.resistivity = resistivity

    def __str__(self) -> str:
        return 'Thickness={0}, Width={1}, Resistivity={2}'.format(self.thickness, self.width, self.resistivity)