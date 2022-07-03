import traceback
from .shared import db


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    company = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    committee = db.Column(db.String, nullable=False)
    last_active = db.Column(db.DateTime, nullable=False)
    alumni = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, city, company, email, phone, committee, last_active):
        self.name = name
        self.city = city
        self.company = company
        self.email = email
        self.phone = phone
        self.committee = committee
        self.last_active = last_active

    def __repr__(self) -> str:
        return "<Member %r>" % self.id

    @staticmethod
    def create(name, city, company, email, phone, committee, last_active):
        try:
            new_member = Member(name, city, company, email, phone, committee, last_active)
            db.session.add(new_member)
            db.session.commit()
            return True
        except Exception:
            print("error Member create" + " " + traceback.format_exc())
            return False

    @staticmethod
    def read_all():
        try:
            query_result = Member.query.all()
            members = [
                {
                    "id": member.id,
                    'name' : member.name,
                    'city' : member.city,
                    'company' : member.company,
                    'email' : member.email,
                    'phone' : member.phone,
                    'committee' : member.committee,
                    'last_active' : member.last_active
                }
                for member in query_result
            ]
            return members
        except Exception:
            print("error Member read_all" + " " + traceback.format_exc())
            return "[]"

    @staticmethod
    def read_one(id):
        try:
            member = Member.query.get(id)
            return member
        except Exception:
            print("error Member read_one" + " " + traceback.format_exc())
            return '[]'

    # @staticmethod
    # def update(id, name):
    #     try:
    #         customer_to_update = run_query(Customer.query.get, *[id])
    #         customer_to_update.name = name
    #         run_query(db.session.commit)
    #         return True
    #     except Exception:
    #         print("error Customer update" + " " + traceback.format_exc())
    #         return False

    @staticmethod
    def delete(id):
        try:
            member = Member.query.get(id)
            if member is not None:
                db.session.delete(member)
                db.session.commit()
                return True
            else:
                print(f"Member with id: {id} does not exist :: in customer.delete()")
                return False
        except Exception:
            print("error Member delete" + " " + traceback.format_exc())
            return False

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    committee = db.Column(db.String, nullable=False)

    def __init__(self, name, city, company, email, phone, committee, last_active):
        self.name = name
        self.email = email
        self.phone = phone
        self.committee = committee

    def __repr__(self) -> str:
        return "<User %r>" % self.id

    @staticmethod
    def create(name, email, phone, committee):
        try:
            new_user = Member(name, email, phone, committee)
            db.session.add(new_user)
            db.session.commit()
            return True
        except Exception:
            print("error User create" + " " + traceback.format_exc())
            return False

    @staticmethod
    def read_all():
        try:
            query_result = User.query.all()
            users = [
                {
                    "id": user.id,
                    'name' : user.name,
                    'email' : user.email,
                    'phone' : user.phone,
                    'committee' : user.committee,
                }
                for user in query_result
            ]
            return users
        except Exception:
            print("error User read_all" + " " + traceback.format_exc())
            return "[]"

    @staticmethod
    def read_one(id):
        try:
            user = User.query.get(id)
            return user
        except Exception:
            print("error User read_one" + " " + traceback.format_exc())
            return '[]'

    # @staticmethod
    # def update(id, name):
    #     try:
    #         customer_to_update = run_query(Customer.query.get, *[id])
    #         customer_to_update.name = name
    #         run_query(db.session.commit)
    #         return True
    #     except Exception:
    #         print("error Customer update" + " " + traceback.format_exc())
    #         return False

    @staticmethod
    def delete(id):
        try:
            member = Member.query.get(id)
            if member is not None:
                db.session.delete(member)
                db.session.commit()
                return True
            else:
                print(f"Member with id: {id} does not exist :: in customer.delete()")
                return False
        except Exception:
            print("error Member delete" + " " + traceback.format_exc())
            return False