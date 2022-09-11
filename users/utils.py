class CheckEmptyFields():
    def check_empty_field(field: str):
        return not field.strip()

class CheckPassword():
    def check_password_lenght(password: str):
        return len(password) < 8

    def check_password_corresponds(password: str, password2: str):
        return password != password2