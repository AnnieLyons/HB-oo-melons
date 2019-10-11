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

    def __init__(self, species, qty, order_type=None, tax=None, country_code=None):
        """Initialize melon order attributes."""
        
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax 
        if country_code:
            self.country_code = country_code


    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

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
