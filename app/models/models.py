from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base

class User(Base):
    """
    Representa o usuário do sistema.
    Utiliza RBAC (Role-Based Access Control) básico para diferenciar planos.
    """
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_premium = Column(Boolean, default=False) # Define limites de monitoramento
    is_active = Column(Boolean, default=True)
    
    # Relacionamento 1:N - Um usuário pode monitorar vários alvos
    monitors = relationship("MonitorTarget", back_populates="ower")
    
class MonitorTarget(Base):
    """ 
    Entidade principal para o serviço de monitoramento.
    Armazena URLs e critérios de alerta(como o preço desejado)
    """
    __tablename__ = "monitor_targets"
    
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, nullable=False)
    product_name = Column(String)
    target_price = Column(Float, nullable=True) # Alerta se o preço cair abaixo disso
    last_price = Column(Float)
    is_active = Column(Boolean,default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user_id = Column(Integer, ForeignKey("users.id"))
    
    # Back-refenrece para o dono do monitoramento
    ower = relationship("User", back_populates="monitors")
    # Histórico de notificações disparada para esse alvo
    notifications = relationship("NotificationHistory", back_populates="target")
    
class NotificationHistory(Base):
    """
    Log de auditoria de notificações enviadas.
    Essencial para garantir que o usuário foi avisado e evitar spans.
    """
    
    __tablename__ = "notification_history"
    
    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, nullable=False)
    sent_at = Column(DateTime, default=datetime.utcnow)
    
    target_id = Column(Integer, ForeignKey("monitors_targets.id"))
    target = relationship("MonitorTarget", back_populates="notifications")
    
