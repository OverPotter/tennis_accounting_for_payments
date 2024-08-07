from datetime import datetime
from typing import List

from sqlalchemy import DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.models.base import Base, BaseIDModel


class UserModel(BaseIDModel):
    __tablename__ = "users"
    name: Mapped[str] = mapped_column(String)

    number_of_trainings_available: Mapped[
        List["NumberOfTennisTrainingAvailable"]
    ] = relationship("NumberOfTennisTrainingAvailable", back_populates="user")
    visits: Mapped[List["VisitModel"]] = relationship(
        "VisitModel", back_populates="user"
    )
    payments: Mapped[List["PaymentModel"]] = relationship(
        "PaymentModel", back_populates="user"
    )


class TennisTrainingTypeModel(BaseIDModel):
    __tablename__ = "tennis_training_type"
    name: Mapped[str] = mapped_column(String)

    number_of_trainings_available: Mapped["NumberOfTennisTrainingAvailable"] = (
        relationship(
            "NumberOfTennisTrainingAvailable",
            uselist=False,
            back_populates="tennis_type",
        )
    )
    visits: Mapped["VisitModel"] = relationship(
        "VisitModel", uselist=False, back_populates="tennis_type"
    )


class NumberOfTennisTrainingAvailable(Base):
    __tablename__ = "number_of_tennis_training_available"
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), primary_key=True
    )
    tennis_type_id: Mapped[int] = mapped_column(
        ForeignKey("tennis_training_type.id"), primary_key=True
    )
    number_of_training: Mapped[int] = mapped_column(Integer)

    user: Mapped["UserModel"] = relationship(
        "UserModel", back_populates="number_of_trainings_available"
    )
    tennis_type: Mapped["TennisTrainingTypeModel"] = relationship(
        "TennisTrainingTypeModel",
        back_populates="number_of_trainings_available",
    )


class VisitModel(BaseIDModel):
    __tablename__ = "visits"
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    tennis_type_id: Mapped[int] = mapped_column(
        ForeignKey("tennis_training_type.id")
    )
    visit_datetime: Mapped[datetime] = mapped_column(DateTime)

    user: Mapped["UserModel"] = relationship(
        "UserModel", back_populates="visits"
    )
    tennis_type: Mapped["TennisTrainingTypeModel"] = relationship(
        "TennisTrainingTypeModel", back_populates="visits"
    )


class PaymentModel(BaseIDModel):
    __tablename__ = "payments"
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    payment_date: Mapped[datetime] = mapped_column(DateTime)
    amount: Mapped[float] = mapped_column(Float)

    user: Mapped["UserModel"] = relationship(
        "UserModel", back_populates="payments"
    )
