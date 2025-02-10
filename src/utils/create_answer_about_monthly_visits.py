from src.schemas.response.client.monthly_visits import (
    ClientWithMonthlyVisitsResponse,
)


def create_answer_about_monthly_visits(
    data: ClientWithMonthlyVisitsResponse,
) -> str:
    visits_count = len(data.visits)
    visits_info = "".join(
        f"{visit.visit_datetime.strftime('%d.%m.%Y')}: {visit.training_type.value}\n"
        for visit in data.visits
    )
    times_word = _pluralize_times(len(data.visits))

    return f"Клиент {data.name} был на тренировках за последние 3 месяца был {visits_count} {times_word}:\n{visits_info}"


def _pluralize_times(count: int) -> str:
    if count % 10 == 1 and count % 100 != 11:
        return "раз"
    elif 2 <= count % 10 <= 4 and (count % 100 < 10 or count % 100 >= 20):
        return "раза"
    else:
        return "раз"
