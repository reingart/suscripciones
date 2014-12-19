# coding: utf8
# try something like
def index(): 
    pagos = db(db.pagos.id>0).select()
    response.view="generic.html"
    return dict(pagos=pagos)
