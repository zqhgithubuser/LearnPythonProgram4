from alchemy_models import Base, Email, Person
from sqlalchemy import create_engine, func, select
from sqlalchemy.orm import Session

engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)


def display_info(session):
    # get all emails first
    emails = select(Email)
    # display results
    print("All emails:")
    for email in session.scalars(emails):
        print(f" - {email.person.name} <{email.email}>")
    people = session.scalar(select(func.count()).select_from(Person))
    emails = session.scalar(select(func.count()).select_from(Email))
    print("Summary:")
    print(f" {people=}, {emails=}")


with Session(engine) as session:
    anakin = Person(name="Anakin Skywalker", age=32)
    obione = Person(name="Obi-Wan Kenobi", age=40)
    obione.emails = [
        Email(email="obi1@example.com"),
        Email(email="wanwan@example.com"),
    ]
    anakin.emails.append(Email(email="ani@example.com"))
    anakin.emails.append(Email(email="evil.dart@example.com"))
    anakin.emails.append(Email(email="vader@example.com"))
    session.add(anakin)
    session.add(obione)
    session.commit()

    obione = session.scalar(select(Person).where(Person.name.ilike("Obi%")))
    print(
        obione, obione.emails
    )  # Obi-Wan Kenobiid=2 [obi1@example.com, wanwan@example.com]

    anakin = session.scalar(select(Person).where(Person.name == "Anakin Skywalker"))
    print(
        anakin, anakin.emails
    )  # Anakin Skywalkerid=1 [ani@example.com, evil.dart@example.com, vader@example.com]

    anakin_id = anakin.id
    del anakin

    display_info(session)
    anakin = session.get(Person, anakin_id)
    session.delete(anakin)
    session.commit()
    display_info(session)
