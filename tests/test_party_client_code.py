from trytond.tests.test_tryton import ModuleTestCase, with_transaction
from trytond.pool import Pool
from trytond.model.exceptions import ValidationError

class Party_client_code_TestCase(ModuleTestCase):
    "Test Party client_code"
    module = 'charging_tel'
        
    @with_transaction()
    def test_invalid_entry_should_throw_error(self):
        pool = Pool()
        Party = pool.get('party.party')

        party, = Party.create([{'name': 'TEL'}])

        with self.assertRaises(ValidationError):
            party.client_code = '123546'
            party.save()

        with self.assertRaises(ValidationError):
            party.client_code = '3515ABC'
            party.save()

        with self.assertRaises(ValidationError):
            party.client_code = '_535'
            party.save()

        with self.assertRaises(ValidationError):
            party.client_code = 'A535.'
            party.save()

    @with_transaction()
    def test_valid_entry_dont_throw_error(self):
        pool = Pool()
        Party = pool.get('party.party')

        party, = Party.create([{'name': 'TELO'}])

        party.client_code = 'AB123'
        party.save()

        party.client_code = 'CP535'
        party.save()

del ModuleTestCase