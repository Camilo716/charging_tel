import re as regex
from trytond.i18n import gettext
from trytond.pool import PoolMeta
from trytond.model import fields
from trytond.model.exceptions import ValidationError


class Party(metaclass=PoolMeta):
    __name__ = 'party.party'

    client_code = fields.Char('Client Code', required=False)

    @classmethod
    def validate_fields(cls, records, field_names):
        super().validate_fields(records,field_names)
        cls.check_fields(records, field_names)


    @classmethod
    def check_fields(cls, records, field_names):
        if field_names and not (field_names & {'client_code'}):
            return

        for record  in records:
            if not cls.is_allowed_client_code(record.client_code):
                raise ValidationError(gettext('charging_tel.client_code_invalid'))
            
    @classmethod
    def is_allowed_client_code(cls, code):
        if code is None:
            return True

        return bool(regex.match("^[A-Z]{2,10}[0-9]{2,8}$", code))
    