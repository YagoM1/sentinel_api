from fastapi import APIRouter, Depends,HTTPException, BackgroundTasks
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.models import MonitorTarget, User
from app.schemas.monitor import Monitor, MonitorBase, MonitorCreate
from app.core.tasks import check_url_status
from app.api import deps

router = APIRouter()

@router.post("/", response_model=Monitor)
def create_monitor(
    *,
    monitor_in: MonitorCreate,
    background_task: BackgroundTasks,
    db: Session = Depends(get_db),
    current_user: User = Depends(deps.get_current_user)
):
    
    db_monitor = MonitorTarget(
        name=monitor_in.name,
        url=monitor_in.url,
        owner_id=current_user.id
    )
    db.add(db_monitor)
    db.commit()
    db.refresh(db_monitor)
    return db_monitor
    
    # DISPARA A TAREFA: O usuário recebe a resposta na hora,
    # e o Python vai testar a URL logo em seguida.
    background_task.add_task(check_url_status, db_monitor.id, db)
    
    return db_monitor
    
