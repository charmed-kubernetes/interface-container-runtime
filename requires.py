from charms.reactive import (
    Endpoint,
    set_flag,
    clear_flag
)

from charms.reactive import (
    when,
    when_not
)


class ContainerRequires(Endpoint):
    @when('endpoint.{endpoint_name}.changed')
    def changed(self):
        if any(unit.received_raw['port'] for unit in self.all_joined_units):
            set_flag(self.expand_name('{endpoint_name}.available'))

    @when_not('endpoint.{endpoint_name}.joined')
    def broken(self):
        clear_flag(self.expand_name('{endpoint_name}.available'))
