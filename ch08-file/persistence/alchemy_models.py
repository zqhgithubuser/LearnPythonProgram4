from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Person(Base):
    __tablename__ = "person"
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    age = mapped_column(Integer)
    emails = relationship(
        "Email",
        back_populates="person",  # Email 类有一个 person 字段与 Person 类对应
        order_by="Email.email",
        cascade="all, delete-orphan",  # 删除 Person 记录时，同时删除关联的 Email 记录
    )

    def __repr__(self):
        return f"{self.name}id={self.id}"


class Email(Base):
    __tablename__ = "email"
    id = mapped_column(Integer, primary_key=True)
    email = mapped_column(String)
    person_id = mapped_column(ForeignKey("person.id"))
    person = relationship("Person", back_populates="emails")

    def __str__(self):
        return self.email

    __repr__ = __str__
