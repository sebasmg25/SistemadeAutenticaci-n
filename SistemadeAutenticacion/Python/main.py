from create import Create
from usuario import Usuario

if __name__ == "__main__":
    print("Hola Mundo")

    user = Usuario("juan", "juan@gmail.com", "123")
    print(vars(Create))
    print(vars(user.email))
    print(vars(user.username))
    print(vars(user.password))
    
    