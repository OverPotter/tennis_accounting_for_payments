from src.schemas.response.client.monthly_payments import (
    ClientWithMonthlyPaymentsResponse,
)


def create_answer_about_monthly_payments(
    data: ClientWithMonthlyPaymentsResponse,
) -> str:
    payments_info = "".join(
        f"{payment.payment_date.strftime('%d.%m.%Y')}: {payment.amount} \n"
        for payment in data.payments
    )

    return f"Клиент {data.name} оплатил за последние 3 месяца:\n{payments_info}"
