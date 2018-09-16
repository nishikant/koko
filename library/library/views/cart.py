from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError
from sqlalchemy import and_

from ..models import Library
from ..models import Category
from ..models import Books
from ..models import RentalPolicy
from ..models import RentalItem
import re
import datetime

# Make entries in rental_item with books seleted for rent
@view_config(route_name='cart', renderer='../templates/cart.jinja2')
def cart_view(request):

    lib_query = request.dbsession.query(Library).filter_by(id = request.GET['library']).one()
    cat_query = request.dbsession.query(Category).filter_by(id = request.GET['category']).one()
    rental_policy = cat_query.rental_policy_id
    rpol_query = request.dbsession.query(RentalPolicy).filter_by(id=rental_policy).one()

    cart_list = {}
    for item, value in request.GET.items():
        if re.search('book_[0-9]$', item):  #find better way
            try:
                book = request.dbsession.query(Books).filter_by(
                   id = value
                ).one()

                rental_item = RentalItem(
                    subscriber_id = 1, #hardcoded
                    category_id = cat_query.id,
                    book_id = book.id,
                    rental_policy_id = rpol_query.id,
                    borrowed_date = datetime.datetime.now(),
                    loan_period = request.GET[item + '_days'],
                    status = 1, #hardcoded
                )
                request.dbsession.add(rental_item)

            except DBAPIError:
                return Response(db_err_msg, content_type='text/plain', status=500)


    try:
        query = request.dbsession.query(RentalItem).filter_by(subscriber_id = 1 ) #hardcoded
        cart_list['total'] = query.count()
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return dict(cart_list=cart_list)


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_library_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
