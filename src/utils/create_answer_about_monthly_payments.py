from src.constants.prices import PAYMENT_CURRENCY
from src.schemas.response.client.monthly_payments import (
    ClientWithMonthlyPaymentsToCoachesResponse,
)


def create_answer_about_monthly_payments(
    data: ClientWithMonthlyPaymentsToCoachesResponse,
) -> str:
    payments_info = "".join(
        f"{payment.payment_date.strftime('%d.%m.%Y')}: {payment.amount} {PAYMENT_CURRENCY} выплачено тренеру {payment.coach_name}\n"
        for payment in data.payments
    )

    return f"Клиент {data.name} оплатил за последние 3 месяца:\n{payments_info}"
