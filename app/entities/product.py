from dataclasses import dataclass


@dataclass
class ProductEntity:
    id: int
    name: str
    description: str
    stock: int
    
    