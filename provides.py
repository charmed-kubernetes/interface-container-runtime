from charms.reactive import (
    Endpoint,
    set_flag,
    clear_flag
)

from charms.reactive import (
    when,
    when_not
)


class ContainerRuntimeProvides(Endpoint):
    @when('endpoint.{endpoint_name}.joined')
    def joined(self):
        set_flag(self.expand_name('endpoint.{endpoint_name}.available'))

    @when_not('endpoint.{endpoint_name}.joined')
    def broken(self):
        clear_flag(self.expand_name('endpoint.{endpoint_name}.available'))

    def configure(self):
        pass
