import os
import sys
import transaction

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )
from pyramid.scripts.common import parse_vars

from ..models.meta import Base
from ..models import (
    get_engine,
    get_session_factory,
    get_tm_session,
    )
from ..models import MyModel
from ..models import Library
from ..models import Books
from ..models import Category
from ..models import RentalItem
from ..models import RentalPolicy
from ..models import Subscriber


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)

    engine = get_engine(settings)
    Base.metadata.create_all(engine)

    session_factory = get_session_factory(engine)

    with transaction.manager:
        dbsession = get_tm_session(session_factory, transaction.manager)

        model = MyModel(name='one', value=1)
        library = Library(name='Kids', address='Pune')

        dbsession.add(model)
        dbsession.add(library)

        rental_policy = RentalPolicy(category_id=1, active=True, version=1, max_books=2, loan_rate=1 )
        dbsession.add(rental_policy)

        category = Category(name='regular', location='rack1', rental_policy_id = 1)
        dbsession.add(category)
        category = Category(name='fiction', location='rack2', rental_policy_id = 1)
        dbsession.add(category)
        category = Category(name='novels', location='rack3', rental_policy_id = 1)
        dbsession.add(category)

