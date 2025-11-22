from sqlalchemy.orm import mapped_column, Mapped


from ..database.database import Base


class Url(Base):
    __tablename__ = 'url'


    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    sketch: Mapped[str] = mapped_column(index=True, unique=True, nullable=False)
    url: Mapped[str] = mapped_column(nullable=False)
