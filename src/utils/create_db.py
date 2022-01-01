import sqlalchemy
import src.config as config
import src.objects.models

# Run this code to create the DB tables (if absent)
engine = sqlalchemy.create_engine(config.uri)
config.metadata.create_all(engine)
