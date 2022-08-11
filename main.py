from argon2 import PasswordHasher


class Hashing(object):
    def __init__(self):
        self.hasher = PasswordHasher()
        self.hashedPassword_0 = self.hasher.hash("password")
        self.hashedPassword_1 = self.hasher.hash("password")
        self.match_0 = self.hasher.verify(self.hashedPassword_0, "password")

        try:
            self.match_1 = self.hasher.verify(self.hashedPassword_1, "wrong")
        except:
            self.match_1 = False

    def __str__(self):
        results = ""
        results += f"1'st Hashed Password {self.hashedPassword_0}\n"
        results += f"2'nd Hashed Password {self.hashedPassword_1}\n"
        results += f"Does 'password' Match {self.hashedPassword_0}: {self.match_0}\n"
        results += f"Does 'wrong' Match {self.hashedPassword_1}: {self.match_1}"
        return results


if __name__ == "__main__":
    print(Hashing())
