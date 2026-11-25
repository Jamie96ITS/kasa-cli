from kasa import Discover


def get_devices():
    return Discover.discover()
