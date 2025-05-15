from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(50),unique = True, nullable = False)
    email = db.Column(db.String(120),unique = True,nullable = False)
    password = db.Column(db.String(100),nullable = False)

    def set_password(self,password):
        self.password = generate_password_hash(password)

    def check_password(self,password):
        return  check_password_hash(self.password,password)

    def __repr__(self):
        return f"<User {self.username}>"

    def to_dict(self, include_password=False):
        user_data = {
            "id": self.id,
            "username": self.username,
            "email": self.email,
        }
        if include_password:
            user_data["password"] = self.password  # hashed password
        return user_data

