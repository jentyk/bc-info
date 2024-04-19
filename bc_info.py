import csv
from dataclasses import dataclass
from typing import Dict, TextIO

from bitcoinlib.services.services import Service


@dataclass
class BcInfo:
    """Bitcoin info getter"""
    service: Service

    def get_bc_info(self, address: str) -> Dict[str, str]:
        """
        Get blockchain information for a given address.

        :param address: The address for which to get blockchain information.
        :type address: str
        :return: A dictionary containing the blockchain information for the given
        address.
        :rtype: dict
        """
        self.service.getbalance(address)
        return self.service.getcacheaddressinfo(address)

    def write_bc_info_csv(self, address: str, file_handle: TextIO) -> None:
        """
        Writes the blockchain information for the given address to a CSV file.

        :param address: The address for which to retrieve blockchain information.
        :param file_handle: The file handle of the CSV file to write the information to.
        :return: None
        """
        bc_info = self.get_bc_info(address)
        w = csv.DictWriter(file_handle, fieldnames=bc_info.keys())
        w.writeheader()
        w.writerow(bc_info)


def write_bc_info_csv(address: str, file_handle: TextIO,
                      service: Service = Service(network='bitcoin',
                                                 min_providers=5)) -> None:
    """
    Writes the blockchain information in CSV format for the given address.

    :param address: The address for which the blockchain information is to be fetched.
    :param file_handle: The file handle to write the CSV data to.
    :param service: The blockchain service to use (default: bitcoin with at least 5
    providers).
    :type address: str
    :type file_handle: file-like object
    :type service: Service
    :return: None
    :rtype: None
    """
    bc_info = BcInfo(service)
    bc_info.write_bc_info_csv(address, file_handle)


if __name__ == "__main__":
    address = "mqR6Dndmez8WMpb1hBJbGbrQ2mpAU73hQC"
    path = "info.csv"
    with open(path, 'w', newline='') as fle:
        write_bc_info_csv(address, fle, Service(network='testnet', min_providers=5))
