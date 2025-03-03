from src.schemas.response.client.client_with_training_number import (
    ClientWithTrainingNumberResponse,
)


def create_answer_about_number_training(
    data: ClientWithTrainingNumberResponse,
) -> str:
    trainings_info = "".join(
        f"{training.training_type.value}: {training.number_of_training} у тренера {training.coach_name}\n"
        for training in data.number_of_trainings_available
    )
    return f"У клиента {data.name} осталось тренировок:\n{trainings_info}"
