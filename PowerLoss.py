class PowerLoss:

    def __init__(self, module, resistance):
        self.module = module
        self.resistance = resistance

    def power_loss_ribbons_bw_cells(self):
        return (self.module.isc()*self.module.isc())*self.resistance.module_ribbon_resistance_between_cell()

    def power_loss_cell_series_resistance(self):
        return (self.module.isc()*self.module.isc())*self.resistance.total_cell_series_resistance()

    def power_loss_busbar(self):
        return (self.module.isc())*self.resistance.busbar_total_resistance

    def module_total_power_loss(self):
        return self.power_loss_ribbons_bw_cells()+self.power_loss_cell_series_resistance()+self.power_loss_busbar()

    def __str__(self) -> str:
        return 'power_loss_ribbons_bw_cells={0}, power_loss_cell_series_resistance={1}, power_loss_busbar={2},' \
               'module_total_power_loss={3}'\
            .format(self.power_loss_ribbons_bw_cells(), self.power_loss_cell_series_resistance(),
                    self.power_loss_busbar(), self.module_total_power_loss())
