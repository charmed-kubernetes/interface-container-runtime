# interface-container-runtime

## Overview

This interface handles communication between subordinate charms, that provide a container runtime and charms requiring a container runtime.

## Usage

### Provides

The providing side of the container interface provides a place for a container runtime to connect to.

Your charm should respond to the {endpoint_name}.available state, which indicates that there is at least one container runtime connected.

The return value is a list of dicts of the following form:

```python
[
    {
        'service_name': name_of_service,
        'runtime_socket': uri_to_container_runtime_socket
    }
]
```

A trivial example of handling this interface would be:

```python
@when('containerd.available')
def update_kubelet_config(containerd):
    services = containerd.services()
    if not data_changed('containerd.services', services):
        return
    kubelet.config['container_runtime_endpoint'] = \
        services[0]['runtime_socket']
```

### Requires

The requiring side of the container interface requires a place for a container runtime to connect to.
