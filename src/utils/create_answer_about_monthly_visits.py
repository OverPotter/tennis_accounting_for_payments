from src.schemas.response.client.monthly_visits import (
    ClientWithMonthlyVisitsResponse,
)


def create_answer_about_monthly_visits(
    data: ClientWithMonthlyVisitsResponse,
) -> str:
    visits_info = "".join(
        f"{visit.visit_datetime.strftime('%d.%m.%Y')}: {visit.training_type.value}\n"
        for visit in data.visits
    )

    return f"Клиент {data.name} был на тренировках за последние 3 месяца:\n{visits_info}"
