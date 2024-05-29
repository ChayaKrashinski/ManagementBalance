from datetime import datetime

from pydantic import BaseModel
from pydantic.v1 import validator


class Revenue(BaseModel):
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
