"""AC50B fields."""

from ..base_devices.ProtocolV2Device import ProtocolV2Device


class AC50B(ProtocolV2Device):
    def __init__(self, address: str, sn: str):
        super().__init__(address, "AC50B", sn)
