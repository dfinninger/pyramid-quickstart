import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import get_appsettings, setup_logging

from .models import DBSession, Page, Base


def usage(argv):
    cmd = os.path.basename(argv[0])
    print(f"usage: {cmd} <config_uri>\nexample: {cmd} development.ini")
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)

    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)

    engine = engine_from_config(settings, "sqlalchemy.")
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)

    with transaction.manager:
        model = Page(title="Root", body="<p>Root</p>")
        DBSession.add(model)
