# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 18:30:33 2022

@author: DELL
"""

import unittest
from modules.conversor import Conversor

class TestConversor(unittest.TestCase):
    
    def setUp(self):
        pass
    
    # def test_convertir_valor_en_rango_valido(self):
        
    #     c = Conversor(0.0,5.0,-40.0,130.0)
    #     val_min = c.convertir(0.0)
    #     self.assertEqual(-40, val_min)
    
    def test_convertir_valor_fuera_de_rango(self):
        
        c = Conversor(0.0,5.0,-40.0,130.0)
        with self.assertRaises(ValueError):
            c.convertir(6.0)
        
    def tearDown(self):
        pass
    
    
if __name__ == '__main__':
    unittest.main()