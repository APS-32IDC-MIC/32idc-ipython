print(__file__)

# set up the data broker (db)

import os

#os.environ['MDS_HOST'] = 'localhost'
os.environ['MDS_HOST'] = '32idcws.xray.aps.anl.gov'
os.environ['MDS_PORT'] = '27017'
os.environ['MDS_DATABASE'] = 'metadatastore-production-v1'
os.environ['MDS_TIMEZONE'] = 'US/Central'
os.environ['FS_HOST'] = os.environ['MDS_HOST']
os.environ['FS_PORT'] = os.environ['MDS_PORT']
os.environ['FS_DATABASE'] = 'filestore-production-v1'

# Connect to metadatastore and filestore.
from metadatastore.mds import MDS, MDSRO
from filestore.fs import FileStore, FileStoreRO
from databroker import Broker
mds_config = {'host': os.environ['MDS_HOST'],
              'port': int(os.environ['MDS_PORT']),
              'database': os.environ['MDS_DATABASE'],
              'timezone': os.environ['MDS_TIMEZONE']}
fs_config = {'host': os.environ['FS_HOST'],
             'port': int(os.environ['FS_PORT']),
             'database': os.environ['FS_DATABASE']}
mds = MDS(mds_config)
# For code that only reads the databases, use the readonly version
#mds_readonly = MDSRO(mds_config)
#fs_readonly = FileStoreRO(fs_config)
fs = FileStore(fs_config)
db = Broker(mds, fs)

#------------------------------------------------------------------
# NOTE: this is a do-at-least-once per beam line to avoid creating a new file store
try:
    from filestore.utils import install_sentinels
    install_sentinels(fs.config, version=1)
except Exception as exc:
    pass
#------------------------------------------------------------------


from databroker.core import register_builtin_handlers
register_builtin_handlers(fs)

# Subscribe metadatastore to documents.
# If this is removed, data is not saved to metadatastore.
from bluesky.global_state import gs
RE = gs.RE  # convenience alias
RE.subscribe('all', mds.insert)
