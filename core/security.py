from passlib.context import CryptContext

crypt = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_password_hash(password: str) -> str:
    return crypt.hash(password)


def password_verify(password: str, password_hash: str) -> bool:
    return crypt.verify(password, password_hash)
