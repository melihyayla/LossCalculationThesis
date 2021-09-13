class Module:

    def __init__(self, cell, cell_number, optic_loss, size, fill_factor, cell_distance):
        self.cell_number = cell_number
        self.optic_loss = optic_loss
        self.size = size
        self.cell = cell
        self.fill_factor = fill_factor
        self.cell_distance = cell_distance

    def total_cell_power(self):
        return self.cell_number*self.cell.power()

    def voc(self):
        return self.cell.voc * self.cell_number / 1000

    def isc(self):
        return self.cell.isc * self.optic_loss / 100

    def power(self):
        return self.fill_factor / 100 * self.voc() * self.isc()

    def efficiency(self):
        return (self.power() / (self.size / 10)) / 100

    def __str__(self) -> str:
        return 'cell_num={0}, optic_loss={1}, size={2}, module_voc={3}, cell_isc={4}, fill_factor={5}, cell_voc={6}, ' \
               'isc={7},power={8},efficiency={9}' \
            .format(self.cell_number, self.optic_loss, self.size, self.voc(),
                    self.cell.isc, self.fill_factor, self.cell.voc, self.isc(), self.power(), self.efficiency())
