from sqlmodel import SQLModel, Session, create_engine

DATABASE_URL = "sqlite:///./rangmanch.db"

engine = create_engine(DATABASE_URL, echo=True)


def cretae_tables():
    """Create the database tables based on the defined models."""
    SQLModel.metadata.create_all(engine)


def get_session():
    """Get a new database session."""
    with Session(engine) as session:
        yield session
