import asyncio
import locale

import src.commands  # noqa: F401
from src.dispatcher.dispatcher import bot, dp
from src.sentry.sentry import init_sentry


async def main():
    init_sentry()
    locale.setlocale(locale.LC_TIME, "ru_RU.UTF-8")

    await dp.start_polling(bot, skip_updates=True)


def run_bot():
    asyncio.run(main())


if __name__ == "__main__":
    run_bot()
