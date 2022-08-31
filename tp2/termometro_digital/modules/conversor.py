# -*- coding: utf-8 -*-

class Conversor:

    def __init__(self, p_min_in,p_max_in, p_min_out, p_max_out):
               
        
        self.min_in = p_min_in 
        self.max_in = p_max_in
        self.min_out = p_min_out
        self.max_out = p_max_out

    def convertir(self,p_val):
        
        if isinstance(p_val,float):
            if self.max_in >= p_val >= self.min_in:
                m = (self.max_out-self.min_out)/(self.max_in-self.min_in)
                p = self.min_out
                return m * p_val + p
        
            else:
                raise ValueError("El valor debe de entrada estar entre: " + str(self.min_in) + " y " + str(self.max_in))
        else:
            raise TypeError("Se debe proveer un flotante")
    
        