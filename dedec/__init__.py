# -*- coding: utf-8 -*-
#
from .__about__ import (
    __version__,
    __author__,
    __author_email__,
    __website__
    )

from .main import identify, findpoly

import pipdate
if pipdate.needs_checking(__name__):
    print(pipdate.check(__name__, __version__))
