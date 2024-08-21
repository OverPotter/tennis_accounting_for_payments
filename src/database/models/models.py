import datetime
from typing import List

from sqlalchemy import (
    Date,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    PrimaryKeyConstraint,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.base import Base, BaseIDModel
from src.schemas.enums.training_types import TrainingTypesEnum


class ClientModel(BaseIDModel):
    __tablename__ = "clients"
    name: Mapped[str] = mapped_column(String(255))

    number_of_trainings_available: Mapped[
        List["NumberOfTennisTrainingAvailableModel"]
    ] = relationship(
        "NumberOfTennisTrainingAvailableModel", back_populates="client"
    )
    visits: Mapped[List["VisitModel"]] = relationship(
        "VisitModel", back_populates="client"
    )
    payments: Mapped[List["PaymentModel"]] = relationship(
        "PaymentModel", back_populates="client"
    )


class NumberOfTennisTrainingAvailableModel(Base):
    __tablename__ = "number_of_tennis_training_available"
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"))
    number_of_training: Mapped[int] = mapped_column(Integer)
    training_type: Mapped[TrainingTypesEnum] = mapped_column(nullable=False)

    client: Mapped["ClientModel"] = relationship(
        "ClientModel", back_populates="number_of_trainings_available"
    )

    __table_args__ = (PrimaryKeyConstraint("client_id", "training_type"),)


class VisitModel(BaseIDModel):
    __tablename__ = "visits"
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"))
    visit_datetime: Mapped[datetime] = mapped_column(DateTime)
    training_type: Mapped[TrainingTypesEnum] = mapped_column(nullable=False)

    client: Mapped["ClientModel"] = relationship(
        "ClientModel", back_populates="visits"
    )


class PaymentModel(BaseIDModel):
    __tablename__ = "payments"
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"))
    payment_date: Mapped[datetime.date] = mapped_column(Date)
    amount: Mapped[float] = mapped_column(Float)
    client: Mapped["ClientModel"] = relationship(
        "ClientModel", back_populates="payments"
    )


class AdminModel(Base):
    __tablename__ = "admins"
    tg_id: Mapped[int] = mapped_column(primary_key=True)
