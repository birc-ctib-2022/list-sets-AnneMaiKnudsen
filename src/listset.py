"""List implementation of a set."""

from typing import (
    Generic, Iterable, TypeVar
)

T = TypeVar('T')


class ListSet(Generic[T]):
    """A set of elements of type T."""

    data: list[T]

    def __init__(self, init: Iterable[T]) -> None:
        """Initialise set with init."""
        
        ...  
        self.data=init

        #Måske den er lineær O(n), fordi den er afhængige af hvor mange gange vi skal lave noget self.noget

    def __contains__(self, x: T) -> bool:
        """Test if x is in set."""
        ...  
        if x in self.data:
            return True
        return False

        #den skal igennem alle indexer i self.data, så den må være lineær. Worst case må så være O(n) og best må være O(1)

    def __bool__(self) -> bool:
        """
        Return truth value of the set.

        A set is True if it is non-empty and False
        otherwise
        """
        ... 
        if self.data==():
            return False
        return True

        #enten er den tom eller også er den ikek tom. Så den er vel O(1)

    def add(self, x: T) -> None:
        """Add x to the set."""
        ...  
        if x not in self:
            self.data.append(x)
        
        #den må lave en lineær search for at finde ud af om elementet er der. Så det må bære en lineær. O(n)

    def remove(self, x: T) -> None:
        """Remove x from the set."""
        ... 
        #fra bogen
        try:
            idx=self.data.index(x)
            self.data.pop(idx)
        except ValueError:
            raise KeyError()

        #man finder indexet og gemmer det som idx, også popper man det. 
        #Jeg tænker den er lineær, med mindre index funktionen søger alt igennem. SÅ er det O(n^2)
