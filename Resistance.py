class Resistance:

    def __init__(self, cell, module, ribbon, busbar):
        self.cell = cell
        self.module = module
        self.ribbon = ribbon
        self.busbar = busbar
        self.busbar_total_resistance = busbar.total_resistance()

    def resistance_bw_cells(self):
        return self.ribbon.resistivity * (self.module.cell_distance + self.cell.edge_length * 2 / 1000) / \
               (self.ribbon.width * self.ribbon.thickness)

    def series_ribbon_resistance_bw_cell_module(self):
        return self.resistance_bw_cells() * self.module.cell_number / self.cell.busbar_number

    def module_cell_series_res(self):
        return self.module.cell_number * self.cell.series_resistance

    def module_total_resistance(self):
        return self.series_ribbon_resistance_bw_cell_module() + self.module_cell_series_res() + \
               self.busbar.total_resistance()

    # Yatay Kısımdaki hesaplamalar
    def module_ribbon_resistance_between_cell(self):
        return ((self.resistance_bw_cells() * self.module.cell_number / self.cell.busbar_number)
                - (self.ribbon.resistivity * self.module.cell_distance / self.ribbon.thickness
                   * self.ribbon.width * self.cell.busbar_number)) * 2 / 3

    def total_cell_series_resistance(self):
        return self.cell.series_resistance*self.module.cell_number

    def __str__(self) -> str:
        return 'resistance_bw_cells={0}, series_ribbon_resistance_bw_cell_module={1}, module_cell_series_res={2},' \
               'module_total_resistance={3}, module_ribbon_resistance_between_cell={4}, ' \
               'total_cell_series_resistance={5}'\
            .format(self.resistance_bw_cells(), self.series_ribbon_resistance_bw_cell_module(),
                    self.module_cell_series_res(), self.module_total_resistance(),
                    self.module_ribbon_resistance_between_cell(), self.total_cell_series_resistance())
