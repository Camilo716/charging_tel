from trytond.pool import PoolMeta
from trytond.model import fields

class Party(metaclass=PoolMeta):
    __name__ = 'party.party'

    client_code = fields.Char('Client Code', required=False)

    