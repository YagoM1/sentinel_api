import requests
from sqlalchemy.orm import Session
from app.models.models import MonitorTarget

def check_url_status(monitor_id: int, db: Session):
    """
    Função que será executada em segundo plano para testar a URL.
    """
    monitor = db.query(MonitorTarget).filter(MonitorTarget.id == monitor_id).first()
    if not monitor:
        return 
        
    try:
        # Tenta acessar o site com um timeout de 10 segundos
        response = requests.get(monitor.url, timeout=10)
        
        # Se o status for 200-299, o site está online
        monitor.is_active = response.status_code == 200
        
    except Exception:
        # Se der erro marcamos como offline
        monitor.is_active = False
        
    db.add(monitor)
    db.commit()
    