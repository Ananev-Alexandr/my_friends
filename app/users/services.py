from data_base.models import User, db
from flask_login import login_user, logout_user

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

    @classmethod
    def login(cls, login_params: dict) -> dict:
        login = login_params.get('login')
        user_password = login_params.get('password')
        user = User.query.filter(User.login==login).one_or_none()
        if not user or not User.check_password(user, user_password):
            print('Неверный логин или пароль!')
            return False
        login_user(user)
        return 'Success'
    
    @classmethod
    def logout(cls):
        return logout_user()
    
    @classmethod 
    def return_all_users(cls):
        result = {"data": []}
        posts :list[User]= User.query.order_by(User.name, User.surname).all()
        for element in posts:
            result["data"].append(element.to_json())
        return result

    @classmethod 
    def filter_users(cls, params):
        result = {"data": []}
        if params.get('filter') is not None:
            list_filter_value = params.get('filter')
            if cls.validate_filter_user(list_filter_value) is False:
                return 'incorrect data entered'
            filter_value = cls.get_filter_value(list_filter_value)
            query = User.query
            for elem in filter_value:
                query = query.filter(elem)
            user_query = query.all()
            for user_elem in user_query:
                result["data"].append(user_elem.to_json())  
            return result
        
        
    @classmethod   
    def validate_filter_user(cls, list_filter_value):
        for filter_dict in list_filter_value:
            for key in filter_dict:
                if key not in ['name', 'surname']:
                    return False
            
    @classmethod        
    def get_filter_value(cls, list_filter_value):
        dict_asociation = {
            "name": User.name,
            "surname": User.surname
        }
        list_filter = []
        for elem in list_filter_value:
            for key in elem:
                list_filter.append(dict_asociation.get(key).ilike(f'%{elem.get(key)}%'))
        return list_filter
