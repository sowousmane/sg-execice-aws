import os

# Provide a default database URL for tests when not set in the environment
os.environ.setdefault("DATABASE_URL", "sqlite:///./test.db")
