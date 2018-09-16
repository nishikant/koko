from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from ..models import Library
from ..models import Category
from ..models import Books
from ..models import RentalPolicy


@view_config(route_name='rent', renderer='../templates/rent.jinja2')
def books_view(request):
    rent_list = {}
    try:
        query = request.dbsession.query(Books).filter_by(id = request.GET['book'])
        for row in query:
            book_list[row.name] = row.id
    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return dict(book_list=book_list)


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
