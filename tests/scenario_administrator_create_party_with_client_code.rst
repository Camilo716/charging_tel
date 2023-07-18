Dependencias::

    >>> from proteus import Model, Wizard
    >>> from trytond.tests.tools import activate_modules

Activacion de modulos::

	>>> config = activate_modules('charging_tel')

Party con client_code::

    >>> Party = Model.get('party.party')
	>>> party = Party()
    >>> party.client_code = 'AB123' # valor real uno de los entregados
    >>> party.save()
    >>> party.client_code
    'AB123'