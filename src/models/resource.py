class Resource:
  """Represents a bookable item (eg. Hotel Room, Conference Room,seat)."""
  def __init__(self, resource_id:str, name:str, price_per_hour : float, is_avaiable : bool = True):
    self._resource_id = resource_id
    self._name = name
    self._price_per_hour = price_per_hour
    self._is_available = is_avaiable

  @property
  def resource_id(self) -> str:
    return self._resource_id

  @property
  def name(self) -> str:
    return self._name

  @property
  def price_per_hour(self) -> float:
    return self._price_per_hour

  @property
  def is_available(self) -> bool:
    return self._is_available

  def book(self) -> bool:
    """Encapsulated stae change."""
    if not self._is_available:
      raise ValueError(f"Resource '{self._name}' is already booked.")
    self._is_available = False
    return True

  def release(self) -> None:
    """ Encapsulated state change."""
    self._is_available = True

  def to_dict(self) -> dict:
    return {
      "resource_id": self._resource_id,
      "name": self._name,
      "price_per_hour": self._price_per_hour,
      "is_avaiable":self._is_available
    }
