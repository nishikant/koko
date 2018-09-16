from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from ..models import Library
from ..models import Category
from ..models import Books


@view_config(route_name='books', renderer='../templates/books.jinja2')
def books_view(request):
    book_list = {}

    lib_query = request.dbsession.query(Library).filter_by(id = request.GET['library']).one()
    cat_query = request.dbsession.query(Category).filter_by(id = request.GET['category']).one()
    book_list['category'] = (request.GET['category'], cat_query.name)
    book_list['library'] = (request.GET['library'], lib_query.name)

    try:
        query = request.dbsession.query(Books).filter_by(category_id = request.GET['category'])
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
