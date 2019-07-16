class User():
    def __init__(self,login_attempts):
        self.login_attempts = login_attempts

    def increment_loginattempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

usertest = User(1)
usertest.increment_loginattempts()
usertest.reset_login_attempts()
print(usertest.login_attempts)

    