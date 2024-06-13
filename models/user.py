class User:
    def __init__(self, name, email, password, dob):
        self.name = name
        self.email = email
        self.password = password
        self.dob = dob
        self.account = None  # This will be set when the account is created

    def set_account(self, account):
        self.account = account
