from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.orm import relationship


Base = declarative_base()


class Artist(Base):
    __tablename__ = 'artists'

    id = Column('ArtistId', Integer, primary_key=True)
    name = Column('name', String)


class Album(Base):
    __tablename__ = 'albums'

    id = Column('AlbumId', Integer, primary_key=True)
    title = Column('Title', String)
    artist_id = Column('ArtistId', Integer, ForeignKey('artists.ArtistId'))

    artist = relationship('Artist')
