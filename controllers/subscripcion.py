# coding: utf8
# try something like
import datetime

def index(): 

    #class TZ(tzinfo):
    #    def utcoffset(self, dt): return timedelta(minutes=-3*60)

    #, tzinfo=TZ()

    #return str((datetime.datetime.utcnow() + datetime.timedelta(seconds=60)).isoformat())
    preapproval_data = {
        "payer_email":  "test_user_41704623@testuser.com",
        "back_url": "http://www.web2py.com.ar/mp",
        "reason": "Monthly subscription to premium package",
        "external_reference": "OP-1234",
        "auto_recurring": {
            "frequency": 1,
            "frequency_type": "days",
            "transaction_amount": 1,
            "currency_id": "ARS",
            "start_date": (datetime.datetime.utcnow() + datetime.timedelta(seconds=60)).strftime("%Y-%m-%dT%H:%M:%S.000-03:00"),
            "end_date": "2015-06-10T14:58:11.778-03:00"
        }
    }
    
    preapproval = mp.create_preapproval_payment (preapproval_data)
    
    #return str(preapproval)
    return """<!DOCTYPE html>
<html>
    <head>
        <title>Suscribirme</title>
    </head>
    <body>
            <a href="%s">Suscribirme</a>
    </body>
</html>""" % preapproval['response']['init_point']
