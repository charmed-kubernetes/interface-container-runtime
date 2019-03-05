from charms.reactive import (
    RelationBase,
    hook,
    scopes
)


class ContainerProvides(RelationBase):
    scopes = scopes.GLOBAL

    def container_ready(self):
        return self.get_remote(
            '{relation_name}-ready', 'false'
        ).lower() == 'true'

    @hook('{provides:container}-relation-changed')
    def changed(self):
        if self.container_ready():
            self.set_state('{relation_name}.ready')
        else:
            self.remove_state('{relation_name}.ready')

    @hook('{provides:container}-relation-departed')
    def departed(self):
        self.remove_state('{relation_name}.ready')
