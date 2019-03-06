from charms.reactive import (
    Endpoint,
    hook,
    scopes
)


class ContainerProvides(Endpoint):
    scopes = scopes.GLOBAL

    def container_ready(self):
        return self.get_remote(
            '{endpoint_name}-ready', 'false'
        ).lower() == 'true'

    @hook('{provides:container}-relation-changed')
    def changed(self):
        if self.container_ready():
            self.set_state('{endpoint_name}.ready')
        else:
            self.remove_state('{endpoint_name}.ready')

    @hook('{provides:container}-relation-departed')
    def departed(self):
        self.remove_state('{endpoint_name}.ready')
