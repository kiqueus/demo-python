#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 16:57:53 2025

@author: usuario
"""


print(f"Hola soy el moduloB, mi __name__ es: {__name__}")

from paquete1.moduloA import A

class B:
    def captura_mensaje(self):
        obj_a=A()
        return f"Hola desde la clase B: {obj_a.saludo()}"

#print(f"Hola soy el moduloB, mi __name__ es: {__name__}")
