import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(110)
        self.assertEqual(str(self.maksukortti), "saldo: 1.2")

    def test_vahenee_oikein_kun_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.0")

    def test_saldo_ei_muutu_jos_rahaa_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(20)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_ota_rahaa_palauttaa_true_jos_rahat_riittavat(self):
        self.assertEqual(self.maksukortti.ota_rahaa(10), True)

    def test_ota_rahaa_palauttaa_false_jos_rahat_ei_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(20), False)
