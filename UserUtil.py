class UserUtil:
    @staticmethod
    def generate_user_id():
        year_prefix = str(datetime.now().year)[2:4]
        random_digits = ''.join([str(random.randint(0, 9)) for _ in range(7)])  
        return year_prefix + random_digits

    @staticmethod
    def generate_password():
        password = ''.join([random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()') for _ in range(8)])
        while not UserUtil.is_strong_password(password):
            password = ''.join([random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()') for _ in range(8)])
        return password

    @staticmethod
    def is_strong_password(password):
        return len(password) >= 8 and any(c.isupper() for c in password) and any(c.islower() for c in password) and \
               any(c.isdigit() for c in password) and any(c in '!@#$%^&*()' for c in password)

    @staticmethod
    def generate_email(name, surname, domain):
        return f"{name.lower()}.{surname.lower()}@{domain}"

    @staticmethod
    def validate_email(email):
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(email_regex, email) is not None
