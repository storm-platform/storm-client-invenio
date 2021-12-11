# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-client-invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Module tests."""

from flask import Flask

from storm_client_invenio import InvenioClient


def test_version():
    """Test version import."""
    from storm_client_invenio import __version__
    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask('testapp')
    ext = InvenioClient(app)
    assert 'storm-client-invenio' in app.extensions

    app = Flask('testapp')
    ext = InvenioClient()
    assert 'storm-client-invenio' not in app.extensions
    ext.init_app(app)
    assert 'storm-client-invenio' in app.extensions


def test_view(base_client):
    """Test view."""
    res = base_client.get("/")
    assert res.status_code == 200
    assert 'Welcome to storm-client-invenio' in str(res.data)
