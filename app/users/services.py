from data_base.models import User, db


class UserService():
    @classmethod
    def creat_user(cls, params: dict) -> dict:
        name = params.get('name')
        surname = params.get('surname')
        login = params.get('login')
        password = params.get('password')
        if UserService.validate_user_data(name, surname, login, password) is False:
            return False
        user = User()
        user.name = name
        user.surname = surname
        user.login = login
        password = user.set_password(password)
        user.password_hash = password
        db.session.add(user)
        db.session.commit()
        return {'message': 'Success'}

    @classmethod
    def validate_user_data(cls, name, surname, login, password):
        params = [name, surname, login]
        for param in params:
            if param is None:
                print(f"Не заполнено поле: {param}")
                return False
        if len(password) < 8:
            print("Длина поля должна быть не меньше 8")
            return False
        user = User.query.filter(User.login==login).one_or_none()
        if user is not None:
            return False
        return True
