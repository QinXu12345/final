from __future__ import annotations
from abc import ABC, abstractmethod
from numpy.typing import NDArray

class EnergyBase(ABC):
    """Base class for energy expression.
    """
    def __init__(self, data: NDArray) -> None:
        super().__init__()
        self._data = data
    
    @abstractmethod   
    def entropy(self, )