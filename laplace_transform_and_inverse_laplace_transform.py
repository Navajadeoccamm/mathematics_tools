# -*- coding: utf-8 -*-
"""
Created on Sat Jan 17 17:17:37 2026

@author: dmonz
"""

# This file is part of the project's source code.
# Copyright (c) 2026 Daniel Monzon.
# Licensed under the MIT License. See the LICENSE file in the repository root.

# This Python scritp allows you to computes the Laplace and inverse 
# Laplace's transforms using SymPy. 
# It Supports the unit impulse (DiracDelta) and the step function (Heaviside).
# See examples of how to use it at the bottom of the script. 

# Import the necessary libraries and functions
import sympy as sp
from sympy import DiracDelta, Heaviside

# Define sympy simbols
t = sp.symbols('t', real=True)
s = sp.symbols('s', positive=True)

# Dictionary to map sympify names, including 't' to use the existing symbols
_sympy_locals = {
    'DiracDelta': DiracDelta,
    'Heaviside': Heaviside,
    'delta': DiracDelta,  # Allows to use "detla(t)". Note that ("") are required
    'H': Heaviside,       # Allows to use "H(t)". Note that ("") are required
    't': t,                # Crucial: use the `t` defined with assumptions.
    's': s                
}

# Define a Python function to compute Laplace's transform
def laplace_of(expr_str):
    """
    It receives a string representing a function (e.g., sin(2*t) or "delta(t)"
    -quotation marks required for the latter- and returns the Laplace 
    transform of the corresponding SymPy expression.
    """
    f = sp.sympify(expr_str, locals=_sympy_locals)  # Uses locals with 't'
    F = sp.laplace_transform(f, t, s, noconds=True)  # With out conditions
    return sp.simplify(F)

# Define a Python function to compute the inverse Laplace's transform
def inverse_laplace_of(F_expr):
    """Returns the inverse Laplace's transform L^{-1}{F(s)} as a
       function of s.
    """
    return sp.inverse_laplace_transform(sp.sympify(F_expr), s, t)

# Examples uses:
    # 1. laplace_of("sin(t)") must return 1/(s**2 + 1). Note quotation marks.
    # 2. laplace_of(t**2) must return 2/s**3. Quotation marks nor requiered.
    # 3. laplace_of("delta(t)") must return 1
    # 4. laplace_of("delta(t-2")) must return e**(-2*s)
    # 5. inverse_laplace_of(1/s**2) must return H(t)*t
