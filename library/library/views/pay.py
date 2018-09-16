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
@view_config(route_name='pay', renderer='../templates/pay.jinja2')
def pay_view(request):

    pay_list = {}
    pay_list['total'] = 0
    pay_list['books'] = []

    try:
        rented_item = request.dbsession.query(RentalItem).filter_by(
            subscriber_id = request.GET['subscriber'])

        for row in rented_item:
            book_detail = request.dbsession.query(Books).filter_by(
                id = row.book_id).one()

            pay_list['books'].append((book_detail.id, book_detail.name, row.loan_period))

            rpol_query = request.dbsession.query(RentalPolicy).filter_by(
                id=row.rental_policy_id
            ).one()

            if row.loan_period < rpol_query.min_days:
                pay_list['total'] = pay_list['total'] + rpol_query.min_rate
            else:
                pay_list['total'] = pay_list['total'] + rpol_query.min_rate + rpol_query.loan_rate * (row.loan_period - rpol_query.min_days)

    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return dict(pay_list=pay_list)


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
