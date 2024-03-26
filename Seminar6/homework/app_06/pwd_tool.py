from passlib.context import CryptContext

__all__ = ['get_password_hash']
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def password_validator(password) -> str:
    if len(password) < 8:
        raise ValueError('Пароль должен содержать как минимум 8 символов')
    return password


async def hash_password(password: str) -> str:
    await password_validator(password)
    return pwd_context.hash(password)