########################################################################
#####  Category                    #####################################
########################################################################
#####                                                      #############
#####                                                      #############
#####  Memory models for category class.                   #############
#####  For development only.                               #############
#####                                                      #############
#####  Classes:                                            #############
#####     Category                                         #############
#####     CategoryFactory                                  #############
#####                                                      #############
#####                                                      #############
#####                                          2016-01-30  #############
#####                                                      #############
########################################################################

class CategoryFactory(object):
    def __init__(self):
        self.names = {
                'Duvet': 4,
                'Lençol': 1,
                'Colcha': 5,
                'Cobertor': 2,
                'Peseira': 6,
                'Toalha de mesa': 7,
                'Acessorio': 3,
        }
        self.picture = "http://placehold.it/400x300"

    def getCategories(self):
        return [Category(c_id=v, name=k, picture=self.picture) \
                for k,v in self.names.items()]


class Category(object):
    def __init__(self, c_id, name, picture):
        self.id_ = c_id
        self.name = name
        self.picture = picture

if __name__ == '__main__':
    cf = CategoryFactory()
    cf.getCategories()
