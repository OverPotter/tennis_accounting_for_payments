# Tennis Accounting For Payments

if __name__ == "__main__":
    import asyncio

    async def a():
        from src.database.repositories.manager import (
            orm_repository_manager_factory,
        )

        repository_manager = orm_repository_manager_factory()
        async with repository_manager:
            service = RepositoryGetClientVisitsService(
                visit_repository=repository_manager.get_visits_repository()
            )
            data = await service.get_monthly_client_visits(client_id=3)
            print(data)
            print(len(data))

    asyncio.run(a())
