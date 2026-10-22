def requires_login(func):
    def wrapper(*args, **kwargs):

        if user_logged_in:
            func(*args, **kwargs)

        else:
            raise ValueError("Usuario no autenticado")

    return wrapper


user_logged_in = False


@requires_login
def view_profile():

    print("Mostrando perfil del usuario")


try:
    view_profile()
except ValueError as error:
    print(error)
