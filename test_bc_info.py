import sys

from bc_info import write_bc_info_csv


def test_write_bc_info_csv(monkeypatch, mocker, capsys):
    """Test writing blockchain information to CSV file."""
    mock_service = mocker.patch('bitcoinlib.services.services.Service')
    mock_service.getcacheaddressinfo = lambda _: {
        'address': 'mqR6Dndmez8WMpb1hBJbGbrQ2mpAU73hQC', 'balance': 20538000,
        'last_block': None, 'n_txs': None, 'n_utxos': None}
    address = "mqR6Dndmez8WMpb1hBJbGbrQ2mpAU73hQC"
    write_bc_info_csv(address, sys.stdout)
    captured = capsys.readouterr()
    assert captured.out == ("address,balance,last_block,n_txs,n_utxos\r\n"
                            "mqR6Dndmez8WMpb1hBJbGbrQ2mpAU73hQC,0,,,\r\n")
