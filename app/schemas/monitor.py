from pydantic import BaseModel, HttpUrl
from typing import Optional

class MonitorBase(BaseModel):
    name: str
    url: str
    is_active: Optional[bool] = True
    
class MonitorCreate(MonitorBase):
    pass
    
class Monitor(MonitorBase):
    id: int
    owner_id: int
    
    class Config:
        from_attributes = True
    