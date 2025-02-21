from src.schemas.enums.training_types import TrainingTypesEnum

PRICE_LIST = {
    50.0: (1, TrainingTypesEnum.GROUP_TRAINING),
    100.0: (2, TrainingTypesEnum.GROUP_TRAINING),
    180.0: (4, TrainingTypesEnum.GROUP_TRAINING),
    350.0: (8, TrainingTypesEnum.GROUP_TRAINING),
    70.0: (1, TrainingTypesEnum.SPLIT_TRAINING),
    130.0: (1, TrainingTypesEnum.INDIVIDUAL_TRAINING),
}
PAYMENT_CURRENCY = "BYN"
