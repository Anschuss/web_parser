from app import db


class News(db.Model):
    __tablename__ = "news"
    id  = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    title = db.Column(db.String(120))
    img = db.Column(db.String(256))
    body = db.Column(db.Text())
    url = db.Column(db.Text())

    def __repr__(self):
        return f"News: {self.title}, {self.img}, {self.body}, {self.name}"