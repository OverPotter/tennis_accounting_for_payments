from src.schemas.enums.training_types import TrainingTypesEnum

PRICE_LIST = {
    45.0: (1, TrainingTypesEnum.GROUP_TRAINING),
    160.0: (4, TrainingTypesEnum.GROUP_TRAINING),
    310.0: (8, TrainingTypesEnum.GROUP_TRAINING),
    55.0: (1, TrainingTypesEnum.SPLIT_TRAINING),
    110.0: (1, TrainingTypesEnum.INDIVIDUAL_TRAINING),
}
