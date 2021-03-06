import logging

from peewee import *
from playhouse.sqliteq import SqliteQueueDatabase

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#
# autostart must be False if we intend to dynamically create the database.
#
db = SqliteQueueDatabase(None, autostart=False)
# db = PostgresqlDatabase('postgres',
#                         user='postgres',
#                         password='mysecretpassword',
#                         host='localhost',
#                         port=5432)


class BinaryDetonationResult(Model):
    md5 = CharField(index=True,unique=True)
    last_scan_date = DateTimeField(index=True, null=True)
    last_success_msg = CharField(default='', null=True)

    last_error_msg = CharField(default='', null=True)
    last_error_date = DateTimeField(null=True)

    score = IntegerField(default=0)

    scan_count = IntegerField(default=0)

    #
    # If There was a permanent error then set this to True
    #
    stop_future_scans = BooleanField(default=False)

    #
    # if we could not download the binary then set this to False
    # We will need to wait for alliance download
    #
    binary_not_available = BooleanField(null=True)

    #
    # Last attempt to scan this binary.  Which could have thrown an error if the binary was not available to download
    #
    last_scan_attempt = DateTimeField(index=True, null=True)

    #
    #
    #
    num_attempts = IntegerField(default=0)

    #
    from_rabbitmq = BooleanField(default=False)
    #

    #
    # copied from Cb Response Server
    #
    server_added_timestamp = DateTimeField()

    #
    # Setting this will force detonation library to rescan this binary
    #
    force_rescan = BooleanField(default=False)

    #
    # Misc use for connectors
    #
    misc = CharField(default='')

    class Meta:
        database = db
