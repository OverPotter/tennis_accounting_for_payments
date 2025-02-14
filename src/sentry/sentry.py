import sentry_sdk

from src.settings import settings_factory


def init_sentry():
    settings = settings_factory()

    sentry_sdk.init(
        dsn=settings.SENTRY_URL,
        send_default_pii=True,
        traces_sample_rate=1.0,
        _experiments={"continuous_profiling_auto_start": True},
        environment=settings.ENVIRONMENT,
    )
