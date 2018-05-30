from peewee import *
from playhouse.sqliteq import SqliteQueueDatabase
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


#
# autostart must be False if we intend to dynamically create the database.
#
db = SqliteQueueDatabase(None, autostart=False)


class BinaryDetonationResult(Model):
    md5 = CharField()
    last_scan_date = DateField(null=True)
    last_success_msg = CharField(default='', null=True)

    last_error_msg = CharField(default='', null=True)
    last_error_date = DateField(null=True)

    score = IntegerField(default=0)

    #
    # If There was a permanent error then set this to True
    #
    stop_future_scans = BooleanField(default=False)

    #
    # if we could not download the binary then set this to False
    # We will need to wait for alliance download
    #
    binary_not_available = BooleanField(default=False, null=True)

    #
    # Last attempt to scan this binary.  Which could have thrown an error if the binary was not available to download
    #
    last_scan_attempt = DateField(null=True)

    #
    # copied from Cb Response Server
    #
    server_added_timestamp = DateField()

    class Meta:
        database = db