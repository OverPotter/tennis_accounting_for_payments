from src.schemas.response.visit.monthly_visits import (
    ClientWithMonthlyVisitsResponse,
)


def create_answer_about_monthly_visits(
    data: ClientWithMonthlyVisitsResponse,
) -> str:
    visits_info = "".join(
        f"{visit.visit_datetime.strftime('%d.%m.%Y')}: {visit.training_type.value}\n"
        for visit in data.monthly_visits
    )

    return f"Клиент {data.name} был на тренировках:\n{visits_info}"
