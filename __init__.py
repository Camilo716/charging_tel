# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from trytond.pool import Pool
from . import party

__all__ = ['register']


def register():
    Pool.register(
        party.Party,
        module='charging_tel', type_='model')
    Pool.register(
        module='charging_tel', type_='wizard')
    Pool.register(
        module='charging_tel', type_='report')
