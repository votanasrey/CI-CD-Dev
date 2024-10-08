from pydantic import BaseModel,Field
from typing import Union, List

class ResponseData(BaseModel):
    message: Union[str, None]
    data: Union[dict, list, str, None]
    time: Union[float, None]