"""Classes for melon orders."""

class AbstractMelonOrder:
    

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        
    
    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True 

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species == "Christmas":
            base_price = base_price * 1.5

        if self.order_type == "international" and self.qty < 10:
            base_price = base_price + 3
        
        total = (1 + self.tax) * self.qty * base_price

        return total


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""


    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)
        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):

    tax = 0
    passed_inspection = False

    def mark_inspection(passed):
        if passed == True:
            passed_inspection = True
        
        return passed_inspection
