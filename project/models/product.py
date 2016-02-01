########################################################################
#####  Product                     #####################################
########################################################################
#####                                                      #############
#####                                                      #############
#####  Basic product model for development.                #############
#####                                                      #############
#####                                                      #############
#####  Classes:                                            #############
#####     Product                                          #############
#####     ProductFactory                                   #############
#####                                                      #############
#####                                                      #############
#####                                          2016-02-01  #############
#####                                                      #############
########################################################################

class ProductFactory(object):
    # TODO:
    # Create a getter by category id for products
    def __init__(self):
        self.name = 'Lençol com estampa florida c/ tecido importado'
        self.description = (
                'FEITO COM PERCAL 7000 FIOS DA ÍNDIA ORIENTAL',
                'IDEAL PARA CASAS DE CAMPO, SÍTIOS, FAZENDAS ETC.')
        self.price = 450.00

    def getProducts(self):
        return [
                Product(
                    id_ = i,
                    name = self.name,
                    description = self.description,
                    price = self.price) \
                for i in range(8)]


class Product(object):
    def __init__(self, id_, name, description, price):
        self.id_ = id_
        self.name = name
        self.description = description
        self.price = price


if __name__ == '__main__':
    pass
