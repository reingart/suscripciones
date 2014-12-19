# coding: utf8
# try something like

def index(): 

    info = mp.get_payment_info(request.vars['id'])["response"]['collection']

    db.pagos.insert(mp_id=request.vars['id'], mp_topic=request.vars.get("topic"),
                    ds=info['reason'],
                    imp_total=info['total_paid_amount'],
                    tipo_doc={"DNI": 96, "CUIT": 80}[info["payer"]["identification"]["type"]],
                    nro_doc=info["payer"]["identification"]["number"],
                    email=info["payer"]["email"],
                    first_name=info["payer"]["first_name"],
                    last_name=info["payer"]["last_name"],
                    forma_pago=info["payment_type"],
                    obs=info["status"],
                    obs_comerciales=info["status_detail"],
                  )

    return "OK"

def info():
    response.view = "generic.html"
    
    id = request.args[0]
    
    paymentInfo = mp.get_payment_info(id)
    
    # Show payment information
    if paymentInfo["status"] == 200:
        return paymentInfo["response"]
    else:
        return None
