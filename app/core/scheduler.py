from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy.orm import Session
import datetime

from app.db.session import SessionLocal
from app.models.models import MonitorTarget
from app.core.tasks import check_url_status

def check_all_monitors():
    """
    Busca todos os monitores no banco e testa um por um.
    """
    db: Session = SessionLocal()
    try:
        monitors = db.query(MonitorTarget).all()
        for monitor in monitors:
            check_all_monitors_logic(monitor.id, db)
    finally:
         db.close()
         
def check_all_monitors_logic(monitor_id: int, db: Session):
    check_url_status(monitor_id, db)
    
scheduler = BackgroundScheduler(timezone=datetime.timezone.utc)
# Aqui definimos o intervalo (ex: a cada 10 minutos)
scheduler.add_job(check_all_monitors, 'interval', minutes=10)