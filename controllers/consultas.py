# coding: utf8
# try something like

def index(): 
    # Create an instance with your MercadoPago credentials (CLIENT_ID and CLIENT_SECRET): 
    # Argentina: https://www.mercadopago.com/mla/herramientas/aplicaciones 
    # Brasil: https://www.mercadopago.com/mlb/ferramentas/aplicacoes
    
    
    filters = {
        "site_id": "MLA", # Argentina: MLA; Brasil: MLB
        "external_reference": None,
    }

    # Search payment data according to filters
    searchResult = mp.search_payment(filters)
    
    # Show payment information
    output = """
    <!doctype html>
    <html>
        <head>
            <title>Search payments</title>
        </head>
        <body>
            <table border='1'>
                <tr><th>id</th><th>external_reference</th><th>status</th></tr>"""
    for payment in searchResult["response"]["results"]:
        output += "<tr>"
        output += "<td>"+str(payment["collection"]["id"])+"</td>\n"
        output += "<td>"+str(payment["collection"]["external_reference"])+"</td>\n"
        output += "<td>"+payment["collection"]["status"]+"</td>\n"
        output += "</tr>"
    output += """
            </table>
        </body>
    </html>
    """
    
    response.view = "generic.html"
    return {"search_result": searchResult}
    #return output
