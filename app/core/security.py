# app/core/security.py

from jose import JWTError, jwt
from datetime import datetime, timedelta
from app.core.config import settings  # Import settings to access SECRET_KEY
from passlib.context import CryptContext

# Setting up password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Secret key for JWT encoding and decoding
SECRET_KEY = settings.SECRET_KEY  # Retrieve SECRET_KEY from the settings
ALGORITHM = "HS256"  # Algorithm used for signing JWT
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Expiry time for access tokens


def hash_password(password: str) -> str:
    """Hash a password."""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify if a password matches the hashed password."""
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    """Create an access token."""
    if expires_delta is None:
        expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    expire = datetime.utcnow() + expires_delta
    to_encode = data.copy()
    to_encode.update({"exp": expire})

    # Create the token with the SECRET_KEY and algorithm
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
