from simplewebtools import db


class Entry(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    text = db.Column(db.Text)

    def __repr__(self):
        return '<Entry id={id} title={title!r}>'.format(id=self.id, title=self.title)


class SqlResult(db.Model):
    __tablename__ = 'sqlresults'
    id = db.Column(db.Integer, primary_key=True)
    original_sql = db.Column(db.Text)
    beautified_sql = db.Column(db.Text)
    entry_user = db.Column(db.Text)
    entry_date = db.Column(db.Date)
    update_user = db.Column(db.Text)
    update_date = db.Column(db.Date)

    def __repr__(self):
        return '<SqlResult id={id} original_sql={original_sql!r}>'.format(id=self.id, original_sql=self.original_sql)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    login_id = db.Column(db.Text)
    login_pass_hash = db.Column(db.Text)
    email_address = db.Column(db.Text)
    entry_user = db.Column(db.Text)
    entry_date = db.Column(db.Date)
    update_user = db.Column(db.Text)
    update_date = db.Column(db.Date)

    def __repr__(self):
        return '<User id={id} login_id={login_id!r}>'.format(id=self.id, login_id=self.login_id)


def init():
    db.create_all()
