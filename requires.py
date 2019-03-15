from charms.reactive import (
    Endpoint,
    set_flag,
    clear_flag
)

from charms.reactive import (
    when,
    when_not
)


class ContainerRuntimeRequires(Endpoint):
    @when('endpoint.{endpoint_name}.changed')
    def changed(self):
        set_flag(self.expand_name('endpoint.{endpoint_name}.available'))

    @when_not('endpoint.{endpoint_name}.joined')
    def broken(self):
        clear_flag(self.expand_name('endpoint.{endpoint_name}.available'))

    def set_config(self, socket, runtime, nvidia_enabled):
        """
        Set the configuration to be published.

        :param socket: String uri to runtime socket
        :param runtime: String runtime executable
        :param nvidia_enabled: Boolean nvidia runtime enabled
        :return: None
        """
        for relation in self.relations:
            relation.to_publish.update({
                'socket': socket,
                'runtime': runtime,
                'nvidia_enabled': nvidia_enabled
            })
