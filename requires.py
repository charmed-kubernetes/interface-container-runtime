from charms.reactive import (
    RelationBase,
    hook,
    scopes
)


class ContainerRequires(RelationBase):
    scope = scopes.GLOBAL

    @hook('{requires:container}-relation-joined')
    def joined(self):
        self.set_state('{relation_name}.connected')

    @hook('{requires:container}-relation-departed')
    def departed(self):
        self.remove_state('{relation_name}.connected')

    def set_ready(self):
        self.set_remote(data={
            'container-ready': True
        })

    def set_version(self, version):
        self.set_remote('container-version', version)

    def unset_ready(self):
        self.set_remote('container-ready', False)
