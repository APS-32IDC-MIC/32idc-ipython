from ophyd.commands import setup_ophyd


setup_ophyd()  # this does low-level stuff to get pyepics talking

from bluesky import RunEngine
from bluesky.plans import *
from bluesky.callbacks import *


def custom_callback_example(name, doc):
    """
    a very simple example: print document name each time one is
    generated

    Example
    -------
    >>> RE(plan, custom_callback_example)  # single use
    >>> RE.subscribe('all', custom_callback_example)  # use always
    """
    # name is a string; doc is a dict
    print(name)


def data_writer(filename, field):
    "make a callback function that writes data to an h5 file"
    def cb(name, doc):
        if name != 'event':
            return
    # We have an event document. Extract the measurement of interest.
        data = doc['data'][field]
        with h5py.File(filename) as f:
            pass
            # etc


RE = RunEngine({'owner': '32-id', 'group': '32-id', 'beamline_id': '32-id'})
