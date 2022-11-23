from passlib.context import CryptContext

crypt = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_password_hash(password: str) -> str:
    return crypt.hash(password)
