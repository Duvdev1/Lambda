
from sqlalchemy import MetaData, create_engine, Table, Integer, String, Column, Identity, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from homeworkP3_20_12_2021_db_config import Base, create_all_entities,local_session
from homeworkP3_20_12_2021_db_repo import DbRepo

# create tables
class Kita(Base):
    __tablename__ = 'kita'
    id = Column(Integer, primary_key=True, autoincrement=True)
    floor = Column(Integer, nullable=False)
    num_of_students = Column(Integer, nullable=False)
    class_avg = Column(Integer, nullable=False)

    def inc_num_of_student(self):
        self.num_of_students+=1

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True,  autoincrement=True)
    fname = Column(String, nullable=False)
    lname = Column(String, nullable=False)
    grade_avg = Column(Integer, nullable=False)
    kita_id = Column(Integer, ForeignKey(Kita.id), nullable=False)

    def get_kita_id(self):
        return self.kita_id

create_all_entities()

repo = DbRepo(local_session)

meta = MetaData()


# kita1 = Kita(floor=2, num_of_students=0,class_avg = 0)
# kita2 = Kita(floor=4, num_of_students=0,class_avg = 0)
# repo.add(kita1)
# repo.add(kita2)

def add_student_to_class(student):
    kita = repo.get_by_id(Kita ,student.kita_id)
    kita.class_avg = ((kita.num_of_students*kita.class_avg) + student.grade_avg) / (kita.num_of_students + 1)
    kita.num_of_students += 1
    repo.add(kita)
    repo.add(student)


s1=Student(fname='s', lname = 'a', grade_avg = 6, kita_id = 1)
s2=Student(fname='B', lname = 'S', grade_avg = 5, kita_id = 2)

add_student_to_class(s1)


'''
def __repr__(self):
    return f'\n<User id={self.id} username={self.username} email={self.email} date_created={self.date_created}>'


def __str__(self):
    return f'<User id={self.id} username={self.username} email={self.email} date_created={self.date_created}>'
'''