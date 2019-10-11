"""Classes for melon orders."""

"""pseudocode:

- AbstractMelonOrder __init__:
    self.species = species
    same with quantity, shipped status, order type, tax

- in addition, International will have in __init__: 
    self.country_code = country_code

- variables on DomesticMelonOrder:
    tax = 0.08
    order_type = "domestic"

- variables on InternationalMelonOrder:
    tax = 0.17
    order_type = "international"

- get_total in Abstract


item specific atts

"""

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty, country_code=None, order_type=None, tax=None):
        """Initialize melon order attributes."""
        
        self.species = species
        self.qty = qty
        self.shipped = False
        if country_code:
            self.country_code = country_code
        if order_type:
            self.order_type = order_type
        if tax:
            self.tax = tax


    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        if self.species == 'Christmas':
            base_price * 1.5
        total = (1 + self.tax) * self.qty * base_price

        if self.qty < 10 and self.order_type == 'international':
            total += 3

        return total


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08 


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

""" Pseudocode!!!

class GovernmentMelonOrder it'll inherit from AbstractMelonOrder

order_type is "government" 

tax = 0

passed_inspection = False


method mark_inspection(passed) 
if it passes
self.passed_inspection = true 

"""

class GovernmentMelonOrder(AbstractMelonOrder):
    """An government melon order."""

    order_type = "government"
    tax = 0
    passed_inspection = False

    def mark_inspection(self, passed):
        """If a successful melon inspection, update passed_inspection."""
        if passed:
            self.passed_inspection = True

# gov_melon = GovernmentMelonOrder("Christmas", 13)
# print(gov_melon.passed_inspection)
# gov_melon.mark_inspection(True)
# print(gov_melon.passed_inspection)
# print(gov_melon.get_total())

