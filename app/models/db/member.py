import traceback
from .shared import db

db_instance = db.getInstance()

class Member(db_instance.Model):
    id = db_instance.Column(db_instance.Integer, primary_key=True)
    name = db_instance.Column(db_instance.String, nullable=False)
    city = db_instance.Column(db_instance.String, nullable=False)
    company = db_instance.Column(db_instance.String, nullable=False)
    email = db_instance.Column(db_instance.String, nullable=False)
    phone = db_instance.Column(db_instance.String, nullable=False)
    committee = db_instance.Column(db_instance.String, nullable=False)
    last_active = db_instance.Column(db_instance.DateTime, nullable=False)
    alumni = db_instance.Column(db_instance.Boolean, nullable=False)

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
            db_instance.session.add(new_member)
            db_instance.session.commit()
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
    #         run_query(db_instance.session.commit)
    #         return True
    #     except Exception:
    #         print("error Customer update" + " " + traceback.format_exc())
    #         return False

    @staticmethod
    def delete(id):
        try:
            member = Member.query.get(id)
            if member is not None:
                db_instance.session.delete(member)
                db_instance.session.commit()
                return True
            else:
                print(f"Member with id: {id} does not exist :: in customer.delete()")
                return False
        except Exception:
            print("error Member delete" + " " + traceback.format_exc())
            return False

class User(db_instance.Model):
    id = db_instance.Column(db_instance.Integer, primary_key=True)
    name = db_instance.Column(db_instance.String, nullable=False)
    email = db_instance.Column(db_instance.String, nullable=False)
    phone = db_instance.Column(db_instance.String, nullable=False)
    committee = db_instance.Column(db_instance.String, nullable=False)

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
            db_instance.session.add(new_user)
            db_instance.session.commit()
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
    #         run_query(db_instance.session.commit)
    #         return True
    #     except Exception:
    #         print("error Customer update" + " " + traceback.format_exc())
    #         return False

    @staticmethod
    def delete(id):
        try:
            member = Member.query.get(id)
            if member is not None:
                db_instance.session.delete(member)
                db_instance.session.commit()
                return True
            else:
                print(f"Member with id: {id} does not exist :: in customer.delete()")
                return False
        except Exception:
            print("error Member delete" + " " + traceback.format_exc())
            return False