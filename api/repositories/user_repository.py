from api.database.models.user import User
from api.repositories.base import SqlAlchemyRepository


class UserRepository(SqlAlchemyRepository):
    model = User