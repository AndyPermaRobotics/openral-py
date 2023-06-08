from abc import ABC, abstractmethod
from typing import Callable, List, Optional, TypeVar

from openral_py.model.specific_properties import SpecificProperties
from openral_py.ral_object import RalObject

#todo generics
S = TypeVar('S', bound=SpecificProperties)

class RalRepository(ABC):
    """
    Interface for a repository to store and retrieve [RalObject]s from a database.
    """

    @abstractmethod
    async def getRalObjectByUid(self, uid: str, specificPropertiesTransform: Optional[Callable] = None) -> RalObject:
        """
        Returns the [RalObject] with the given uid. Looks for 'identity.UID' == uid in the database.
        If [specificPropertiesTransform] is not null, the [SpecificProperties] of the [RalObject] will be transformed to the given type.
        """
        pass
    
    @abstractmethod
    async def getRalObjectsWithContainerId(self, containerId: str) -> List[RalObject]:
        """
        Returns all [RalObject]s with the given containerId. Looks for 'currentGeolocation.container.UID' == containerId in the database.
        """
        pass
