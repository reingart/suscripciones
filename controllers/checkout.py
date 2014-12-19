# coding: utf8
# try something like
def index(): 

    form = SQLFORM.factory(
        Field("descripcion", "string", default="Barrilete multicolor"),
        Field("cantidad", "integer", default=1),
        Field("precio", "float", default=1.00),
        )
        
    if form.accepts(request.vars, session):
        preference_data = {
            "items": [
               {
                   "title": form.vars.descripcion,
                   "quantity": int(form.vars.cantidad),
                   "currency_id": "ARS",
                   "unit_price": float(form.vars.precio),
               }
            ]  
        }
        
        preference = mp.create_preference(preference_data)

        #return str(preference)
        return """<!DOCTYPE html>
    <html>
        <head>
            <title>Pagar</title>
        </head>
        <body>
            <a href="%s">Pagar</a>
        </body>
    </html>""" % preference['response']['init_point']
    else:
        response.view = "generic.html"
        return {'form': form}
