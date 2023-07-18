from trytond.pool import PoolMeta
from tryton.model import fields

class Party(metaclass=PoolMeta):
    __name__ = 'party.party'

    client_code = fields.char('Client code', required=False)

    