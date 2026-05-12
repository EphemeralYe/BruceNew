from sqlalchemy import Column, Integer, String, DateTime, Boolean, BigInteger, Text
from datetime import datetime
from .base import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(BigInteger, unique=True, index=True)
    username = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    is_banned = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_seen = Column(DateTime, default=datetime.utcnow)

class Chat(Base):
    __tablename__ = "chats"
    
    id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(BigInteger, unique=True, index=True)
    chat_name = Column(String, nullable=True)
    chat_type = Column(String)  # group, supergroup, channel
    created_at = Column(DateTime, default=datetime.utcnow)

class FileMetadata(Base):
    __tablename__ = "file_metadata"
    
    id = Column(Integer, primary_key=True, index=True)
    file_id = Column(String, unique=True, index=True)
    file_name = Column(String, index=True)
    file_size = Column(BigInteger)
    mime_type = Column(String)
    uploader_id = Column(BigInteger)
    chat_id = Column(BigInteger, index=True)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class FilterIndex(Base):
    __tablename__ = "filter_index"
    
    id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(BigInteger, index=True)
    keyword = Column(String, index=True)
    file_id = Column(String)
    file_name = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class BroadcastLog(Base):
    __tablename__ = "broadcast_log"
    
    id = Column(Integer, primary_key=True, index=True)
    broadcast_id = Column(String, unique=True)
    message = Column(Text)
    sent_to = Column(Integer, default=0)
    failed = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

__all__ = ["User", "Chat", "FileMetadata", "FilterIndex", "BroadcastLog"]
