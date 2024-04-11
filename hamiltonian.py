from __future__ import annotations
from abc import ABC, abstractmethod
from numpy.typing import NDArray

class Hamiltonian(ABC):
    """Abstract base class for Hamiltonians."""
    def __init__(
        self,
        J:NDArray | None = None,
        mu: NDArray | None = None
        ) -> None:
        super().__init__()
        if J is None:
            J = 1
        if mu is None:
            mu = 0 
        self._J = J
        self._mu = mu
        
    @abstractmethod
    def unnormalized_boltzmann(self):
        ...
        
class Gibbs(Hamiltonian):
    """Gibbs Hamiltonian."""
    def __init__(
        self,
        config: NDArray | None = None,
        J: NDArray | None = None, 
        mu: NDArray | None = None,
        ) -> None:
        super().__init__(J, mu)
        if config is None:
            self._config = self._init_config()
            
    def _init_config(self) -> NDArray:
        """Initializes the configuration."""
        