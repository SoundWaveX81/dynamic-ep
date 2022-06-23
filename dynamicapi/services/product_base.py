from abc import ABC, abstractmethod


class ProductType(ABC):
    
    @abstractmethod
    def get_price(self):
        pass