from datetime import datetime

from pydantic import BaseModel
from pydantic.v1 import validator


class Revenue(BaseModel):
    """
    Represents a revenue entry in the system.

    Attributes:
    - id (int): The unique identifier for the revenue entry.
    - user (int): The ID of the user associated with the revenue entry.
    - sum (int): The amount of money earned in the revenue entry.
    - date (datetime): The date and time when the revenue entry occurred.
    - details (str): Additional details or description about the revenue entry.

    Validators:
    - check_sum: Validates that the sum of the revenue is positive.

    Raises:
    - ValueError: If the sum of the revenue is not positive, a ValueError will be raised.
    """
    id:int
    user:int
    sum: int
    @validator('sum')
    def check_sum(self, s):
        if sum<=0:
            raise ValueError('invalid sum')
        return sum
    date: datetime
    details: str
