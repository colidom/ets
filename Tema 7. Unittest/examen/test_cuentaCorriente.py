#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from cuentaCorriente import *
from dni import *

new_dni = Dni(cadena='00000000t')
nombre = "Carlos"
apellido = "Oliva"
direccion = "Calle prueba"
telefono = "666666666"
saldo = "12345"

def test_setNombre(self, nombre):
        self.nombre = nombre

def test_getNombre(self):
    assert CuentaCorriente.setNombre == nombre

def test_setApellido(self, apellido):
    assert CuentaCorriente.setApellido == apellido

def test_getApellido(self):
    assert CuentaCorriente.getApellido == apellido

def test_setDireccion(self, direccion):
    assert CuentaCorriente.setDireccion == direccion

def test_getDireccion(self):
    assert CuentaCorriente.getDireccion == direccion

def test_setTelefono(self, telefono):
    assert CuentaCorriente.setTelefono == telefono

def test_getTelefono(self):
    return self.telefono

def test_setNif(self, nif):
    self.nif = nif

def test_getNif(self):
    return self.nif

def test_setSaldo(self, saldo):
    self.saldo = saldo

def test_getSaldo(self):
    self.saldo == saldo
