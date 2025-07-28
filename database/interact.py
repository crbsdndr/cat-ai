from database.connect import Database

class Users(Database):
    def index(self):
        try:
            self.cursor.execute("SELECT * FROM users")
            users = self.cursor.fetchall()
            for user in users:
                print(user)

        except Exception as e:
            print("Error fetching users:", e)

    def show(self, email: str):
        try:
            self.cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            user = self.cursor.fetchone()
            if not user:
                print("User not found.")
                return False

            else:
                print("User found:", user)
                return {
                    "name": user[0],
                    "email": user[1],
                    "password": user[2],
                    "role": user[3]
                }

        except Exception as e:
            print("Error fetching user:", e)

    def insert(self, name: str, email: str, password: str, role: str):
        try:
            self.cursor.execute("""
                INSERT INTO users (name, email, password, role)
                VALUES (%s, %s, %s, %s)
            """, (name, email, password, role))
            self.commit()
            print("Successfully inserted user into the database.")
            return {
                "name": name,
                "email": email,
                "password": password,
                "role": role
            }

        except Exception as e:
            print("Error insert:", e)
            self.rollback()
            return False

user = Users()