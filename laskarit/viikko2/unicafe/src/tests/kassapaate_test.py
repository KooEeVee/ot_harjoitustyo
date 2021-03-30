import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
    
    def test_luotu_kassa_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_kassan_saldo_alussa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_kassan_edulliset_lounaat_alussa_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kassan_maukkaat_lounaat_alussa_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_edullinen_lounas_kun_maksu_riittava_kassan_saldo_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_kateisosto_edullinen_lounas_kun_maksu_riittava_kassan_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250), 10)

    def test_kateisosto_maukas_lounas_kun_maksu_riittava_kassan_saldo_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_kateisosto_maukas_lounas_kun_maksu_riittava_kassan_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(410), 10)

    def test_kateisosto_edullinen_lounas_kun_maksu_riittava_kassan_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisosto_maukas_lounas_kun_maksu_riittava_kassan_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisosto_edullinen_lounas_kun_maksu_ei_riittava_kassan_saldo_lounaiden_maara_vaihtorahat_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(230)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(230), 230)

    def test_kateisosto_maukas_lounas_kun_maksu_ei_riittava_kassan_saldo_lounaiden_maara_vaihtorahat_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(390)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(390), 390)

    def test_korttiosto_edullinen_lounas_kun_maksu_riittava_oikea_summa_veloitetaan(self): 
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
        self.assertEqual(self.maksukortti.saldo, 1000-240)

    def test_korttiosto_maukas_lounas_kun_maksu_riittava_oikea_summa_veloitetaan(self): 
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
        self.assertEqual(self.maksukortti.saldo, 1000-400)

    def test_korttiosto_edullinen_lounas_kun_maksu_riittava_lounaiden_maara_oikea(self): 
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_korttiosto_maukas_lounas_kun_maksu_riittava_lounaiden_maara_oikea(self): 
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_korttiosto_edullinen_lounas_kun_maksu_ei_riittava_kortin_saldo_lounaiden_maara_ei_muutu(self):
        self.maksukortti2 = Maksukortti(230)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti2), False)
        self.assertEqual(self.maksukortti2.saldo, 230)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_korttiosto_maukas_lounas_kun_maksu_ei_riittava_kortin_saldo_lounaiden_maara_ei_muutu(self):
        self.maksukortti2 = Maksukortti(230)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti2), False)
        self.assertEqual(self.maksukortti2.saldo, 230)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kassan_saldo_ei_muutu_kortilla_ostettaessa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortille_ladattaessa_kortin_ja_kassan_saldo_kasvaa_jos_summa_suurempi_kuin_nolla(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.maksukortti.saldo, 1100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)

    def test_kortille_ladattaessa_kortin_ja_kassan_saldo_ei_kasva_jos_summa_pienempi_kuin_nolla(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1)
        self.assertEqual(self.maksukortti.saldo, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

        

    

    
        

    


    

    

    


    

    

     

