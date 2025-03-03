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
from src.schemas.enums.admin_roles import AdminRoleEnum
from src.schemas.enums.specializations import SpecializationEnum
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


class CoachModel(BaseIDModel):
    __tablename__ = "coaches"
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    specialization: Mapped[SpecializationEnum] = mapped_column(nullable=False)

    visits: Mapped[List["VisitModel"]] = relationship(
        "VisitModel", back_populates="coach"
    )
    clients_training_balance: Mapped[
        List["NumberOfTennisTrainingAvailableModel"]
    ] = relationship(
        "NumberOfTennisTrainingAvailableModel", back_populates="coach"
    )
    payments: Mapped[List["PaymentModel"]] = relationship(
        "PaymentModel", back_populates="coach"
    )


class NumberOfTennisTrainingAvailableModel(Base):
    __tablename__ = "number_of_tennis_training_available"
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"))
    coach_id: Mapped[int] = mapped_column(ForeignKey("coaches.id"))
    number_of_training: Mapped[int] = mapped_column(Integer)
    training_type: Mapped[TrainingTypesEnum] = mapped_column(nullable=False)

    client: Mapped["ClientModel"] = relationship(
        "ClientModel", back_populates="number_of_trainings_available"
    )
    coach: Mapped["CoachModel"] = relationship(
        "CoachModel", back_populates="clients_training_balance"
    )

    __table_args__ = (
        PrimaryKeyConstraint("client_id", "coach_id", "training_type"),
    )


class VisitModel(BaseIDModel):
    __tablename__ = "visits"
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"))
    coach_id: Mapped[int] = mapped_column(ForeignKey("coaches.id"))
    visit_datetime: Mapped[datetime] = mapped_column(DateTime)
    training_type: Mapped[TrainingTypesEnum] = mapped_column(nullable=False)

    client: Mapped["ClientModel"] = relationship(
        "ClientModel", back_populates="visits"
    )
    coach: Mapped["CoachModel"] = relationship(
        "CoachModel", back_populates="visits"
    )


class PaymentModel(BaseIDModel):
    __tablename__ = "payments"
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"))
    coach_id: Mapped[int] = mapped_column(ForeignKey("coaches.id"))
    payment_date: Mapped[datetime.date] = mapped_column(Date)
    amount: Mapped[float] = mapped_column(Float)

    client: Mapped["ClientModel"] = relationship(
        "ClientModel", back_populates="payments"
    )
    coach: Mapped["CoachModel"] = relationship(
        "CoachModel", back_populates="payments"
    )


class AdminModel(Base):
    __tablename__ = "admins"
    tg_id: Mapped[int] = mapped_column(primary_key=True)
    role: Mapped[AdminRoleEnum] = mapped_column(nullable=False)
