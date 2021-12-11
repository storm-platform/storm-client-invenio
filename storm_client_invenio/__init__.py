# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-client-invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""InvenioRDM client library."""


from .invenio import InvenioRDM
from .version import __version__


__all__ = ("InvenioRDM", "__version__")
