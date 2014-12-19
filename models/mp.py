# coding: utf8

mercadopago = local_import("mercadopago")
mp = mercadopago.MP('TU_CLIENT_ID', 'TU_CLIENT_SECRET') # pruebas
#mp.sandbox_mode(True)

db.define_table("pagos",
    Field("mp_id"),
    Field("mp_topic"),
    Field("ds"),
    Field("obs"),
    Field("obs_comerciales"),
    Field("forma_pago"),
    Field("imp_total", "double"),
    Field("tipo_cbte", default=6),
    Field("pto_vta", default=4005),
    Field("cbte_nro"),
    Field("tipo_doc"),
    Field("nro_doc"),
    Field("email"),
    Field("first_name"),
    Field("last_name"),
    Field("cae"),
    Field("fecha_vto"),
    Field("fecha", "date", default=request.now),
    Field("motivo"),
    Field("resultado"),
    )
