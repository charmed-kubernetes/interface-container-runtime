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

    def clear_changed(self):
        """
        Call when done with `changed`.

        :return: None
        """
        clear_flag(self.expand_name('endpoint.{endpoint_name}.changed'))

    def get_config(self):
        """
        Get the configuration published.

        :return: Dictionary configuration
        """
        return self.all_joined_units.received

    def set_config(self, pause_image_override=None):
        """
        Set the configuration to be published.

        :param pause_image_override: Optional String override container pause image
        :return: None
        """
        for relation in self.relations:
            relation.to_publish.update({
                'pause_image_override': pause_image_override
            })

        set_flag(self.expand_name('endpoint.{endpoint_name}.changed'))
