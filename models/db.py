db= DAL("sqlite://storage.sqlite")

from gluon.tools import Auth
auth = Auth(db)
auth.define_tables(username=False,signature=False)


db.define_table('student',
    Field('name'),
    Field('entryno', unique = True),
    Field('prof', 'reference auth_user' ),
    )

db.student.id.readable= db.student.id.writable= False




