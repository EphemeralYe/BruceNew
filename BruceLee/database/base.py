from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DB_URI
from logger import logger
from datetime import datetime

# Database setup
engine = create_engine(DB_URI, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

async def init_db():
    """Initialize database tables"""
    try:
        Base.metadata.create_all(bind=engine)
        logger.info("✅ Database initialized successfully")
    except Exception as e:
        logger.error(f"❌ Database initialization failed: {e}")
        raise

def get_db():
    """Get database session"""
    db = SessionLocal()
    try:
        return db
    except Exception as e:
        logger.error(f"❌ Database session error: {e}")
        raise
    finally:
        db.close()

__all__ = ["engine", "SessionLocal", "Base", "init_db", "get_db"]
