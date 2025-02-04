from controller.user import User

data = {
    'firstname': 'Andrea',
    'lastname': 'Diaz Covarrubias',
    'username': 'Andy',
    'password_user': 'andrea'
}
user = User(data)
user.create_user()