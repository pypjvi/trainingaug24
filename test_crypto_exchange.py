import unittest

from unittest.mock import patch

from crypto_exchange import CryptoExchange

class TestCryptoExchange(unittest.TestCase):
    def setUp(self):
        self.exchange = CryptoExchange()

    def test_fetch_real_time_price_btc_usd(self):
        return None
    
    def test_fetch_fee_structure_btc(self):
        return None
    
    def test_fetch_real_time_price_eth_usd(self):
        return None
