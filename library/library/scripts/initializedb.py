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
        dbsession.add(model)

        library = Library(name='Kids', address='Pune')
        dbsession.add(library)
        lib_id = dbsession.query(Library).filter_by(name = 'Kids').one()

        subscriber = Subscriber(
            fname = 'Nishikant',
            lname = 'Sevalkar',
            email = 'gattusevalkar@gmail.com',
            phone = '+919405183224',
            address = 'Pune',
            city = 'Pune',
            status = 1,
            library_id = lib_id.id
        )
        dbsession.add(subscriber)

        # ['book_type', 'rental_policy_name', 'location']
        supported_type = [
            ('regular', 'regular', 'rack1'),
            ('fiction', 'regular', 'rack2'),
            ('novel', 'regular', 'rack3'),
        ]

        for (cat, policy, loc)  in supported_type:

            if not dbsession.query(RentalPolicy).filter_by(name=policy).first():
                rental_policy = RentalPolicy(
                    name = policy,
                    active = True,
                    version = 1,
                    max_books = 2,
                    loan_rate = 1
                )
                dbsession.add(rental_policy)
                transaction.manager.commit()

            rental_p_id = dbsession.query(RentalPolicy).filter_by(name=policy).one()
            category = Category(
                name = cat,
                location = loc,
                rental_policy_id = rental_p_id.id,
            )
            dbsession.add(category)
            transaction.manager.commit()

        reg_cat_id = dbsession.query(Category).filter_by(name='regular').one()
        fiction_cat_id = dbsession.query(Category).filter_by(name='fiction').one()
        novel_cat_id = dbsession.query(Category).filter_by(name='novel').one()

        books = [
            (reg_cat_id.id, '8183071007', 'Word Power Made Easy', 'A english book', 2, 'Norman Lewis', 'paperback', 10, 200, True),
            (reg_cat_id.id, '0062312685', 'The Intelligent Investor', 'A investment book', 1, 'Benjamin Graham', 'paperback', 10, 500, True),
            (fiction_cat_id.id, '1408894638', 'The Chamber of Secrets', 'harry potter 2', 2, 'JK Rowling', 'paperback', 10, 400, True),
            (fiction_cat_id.id, '1408855674', 'Harry Potter and the Prisoner of Azkaban', 'harry potter 3', 3, 'JK Rowling', 'paperback', 10, 400, True),
            (novel_cat_id.id, '8172234988', 'The Alchemist', 'Paulo Coelho enchanting novel', 1, 'Paulo Coelho', 'paperback', 10, 300, True),
            (novel_cat_id.id, '8172234937', 'The Other Side of Midnight', 'novel', 1, 'Sidney Sheldon', 'paperback', 10, 200, True),
        ]

        for item  in books:
            books = Books (
                category_id = item[0],
                isbn = item[1],
                name = item[2],
                overview = item[3],
                edition = item[4],
                author = item[5],
                format = item[6],
                count = item[7],
                max_price = item[8],
                instock = item[9],
            )
            dbsession.add(books)
            transaction.manager.commit()
