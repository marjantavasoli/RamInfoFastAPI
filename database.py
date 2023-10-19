from sqlmodel import Session, SQLModel, create_engine, Field, select

sqlite_url = "sqlite:///test.db"
engine = create_engine(sqlite_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


class RamInfo(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    total: int
    free: int
    used: int

    def add(self):
        with Session(engine) as session:
            session.add(self)
            session.commit()

    @staticmethod
    def get_all():
        with Session(engine) as session:
            ram_info = session.exec(select(RamInfo)).all()
            return ram_info


create_db_and_tables()


d = RamInfo.get_all()
a = 1