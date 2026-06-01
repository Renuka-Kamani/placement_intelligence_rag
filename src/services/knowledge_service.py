from src.database.company_repository import (
    CompanyRepository
)


class KnowledgeService:

    def __init__(self):

        self.repo = (
            CompanyRepository()
        )

    def get_dataframe(
        self
    ):

        return (
            self.repo
            .get_all_data()
        )