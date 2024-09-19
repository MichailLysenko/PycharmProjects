def berechtigung_erforderlich(funktion):
    def wrapper(user):
        if not user['is_admin']:
            print("Zugriff verweigert!")
        else:
            return funktion(user)
    return wrapper

@berechtigung_erforderlich
def admin_bereich(user):
    print(f"Willkommen Admin {user['name']}")

user1 = {'name': 'John', 'is_admin': True}
user2 = {'name': 'Jane', 'is_admin': False}

admin_bereich(user1)  # Erfolgreicher Zugriff
admin_bereich(user2)  # Zugriff verweigert