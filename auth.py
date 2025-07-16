from passlib.context import CryptContext

# Using passlib for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# In a real app, this would be in a secure config or a User model in the database
# For this demo, we'll use a hardcoded username and a hashed password.
# The plain text password is "admin123"
# The security question answer is "blue"
HARDCODED_ADMIN_USER = {
    "username": "admin",
    "hashed_password": "$2b$12$EixZaYVK1p7.wK3n1Xar..vU3Jg2GgRk3q1C6zNPfM3v0.f.pQb6y",
    "security_question": "What is your favorite color?",
    "hashed_answer": "$2b$12$N9.pA8h1yF/A5wY4g1c0/uJg8Qz2qB6c.sRk2l.h7Vz3d.pS0n5yW" # "blue"
}

def verify_password(plain_password, hashed_password):
    """Verifies a plain password against a hashed one."""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    """Hashes a password."""
    return pwd_context.hash(password)

def verify_security_answer(plain_answer, hashed_answer):
    """Verifies a plain security answer against a hashed one."""
    return pwd_context.verify(plain_answer, hashed_answer)

# Example of how the hashes were generated:
# print(get_password_hash("admin123"))
# print(get_password_hash("blue"))