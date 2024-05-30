from datetime import datetime

from pydantic import BaseModel
from pydantic.v1 import validator


class Expenditure(BaseModel):
    """
      Represents an expenditure in the system.

      Attributes:
      - id (int): The unique identifier for the expenditure.
      - user (int): The ID of the user associated with the expenditure.
      - sum (int): The amount of money spent in the expenditure.
      - date (datetime): The date and time when the expenditure occurred.
      - details (str): Additional details or description about the expenditure.

      Validators:
      - check_sum: Validates that the sum of the expenditure is negative.

      Raises:
      - ValueError: If the sum of the expenditure is not negative, a ValueError will be raised.
      """
    id:int
    user:int
    sum:int
    @validator('sum')
    def check_sum(self, s):
        if sum>=0:
            raise ValueError('invalid sum')
        return sum
    date: datetime
    details:str