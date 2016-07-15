"""This file should have our order classes in it."""
# AbstractMelon as a naming convention indicates that no object should be
# created with this Class itself. 
class AbstractMelonOrder(object): 
    """Any melon order"""
    # marking shipped as false for all new instances
    shipped = False


    def __init__(self, melon_species, quantity):
        """Initialize melon order attributes"""
        # When you instantiate an object, you are expecting the user to 
        # add the melon species and the quantity of the order.
        # User needs to know the name of the attribute (species and qty), 
        # not the name of the parameter.  User just needs to enter the parameter
        self.species = melon_species
        self.qty = quantity

    def get_total(self):
        """Calculate price."""
        # Sets same base price for all melon orders
        base_price = 5
        
        # Part 2 was in Progress, need to move part that only applies to 
        # International to subclass, call get_total function and add 3
        #if self.species == "christmas":
        #    base_price = 1.5 * base_price
        
        #if self.order_type == "international" and self.qty < 10:
        #    base_price = base_price + 3
        
        total = (1 + self.tax) * self.qty * base_price
        

        #Part 2: If statements for price adjustments in special cases
        return total
        # To call this method: order_name.get_total()

    def mark_shipped(self):
        """Set shipped to true."""

        # Does not run during instance.  Runs once the user calls function
        # to mark it as true
        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    # Better style may be to have the banes of parameters the same as 
    # parent class, but they do not have to be the same
    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        # Makes the parents methods available for instances of DomesticMelonOrder
        super(DomesticMelonOrder, self).__init__(species, qty)
        # order_type and tax are the things unique to DomesticMelonOrders
        self.order_type = "domestic"
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""
        super(InternationalMelonOrder, self).__init__(species, qty)
        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17


    def get_country_code(self):
        """Return the country code."""

        return self.country_code
