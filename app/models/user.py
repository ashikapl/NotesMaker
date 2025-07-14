class SignUp:
    def __init__(self, user_id, username, email, password):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password

    def to_dict(self):
        return{
            "user_id":self.user_id,
            "email":self.email,
            "password":self.password
        }
    
class Login:
    def __init__(self, id, user_id, email, password):
        self.id = id
        self.user_id = user_id
        self.email = email
        self.password = password

    def to_dict(self):
        return{
            "id":self.id,
            "user_id":self.user_id,
            "email":self.email,
            "password":self.password
        }
        
    