import logging

from .services.services import recreate_database, record_event

logging.basicConfig(level=logging.INFO)

recreate_database()

# Populate data
record_event(type = 'PACOTE_INTEGRADO', package_id = 100, attributes = { "company_id": "shopee", "integrado": True } )
record_event(type='PACOTE_BIPADO', package_id=100, attributes = { "local": "FCA" });
record_event(type='PACOTE_SEPARADO', package_id=100, attributes = { "local": "FCA", "position": 1234 })
record_event(type='TRANSFERENCIA_INICIADA', 
    package_id=100, 
    attributes = { 
        "moving": True, 
        "destination": "SMT",
        "place": "exm0c0123"
    }
)
record_event(type='TRANSFERENCIA_TERMINADA', 
    package_id=100, 
    attributes = { 
        "moving": False
    }
)
      
record_event(type='PACOTE_INTEGRADO', package_id=200, attributes = { "company_id": "shopee", "integrado": True } )
record_event(type='PACOTE_BIPADO', package_id=200, attributes = { "local": "SMT" })
record_event(type='PACOTE_SEPARADO', package_id=200, attributes = { "local": "SMT", "position": 6000 })



# # Popular tabelas
# with Session(db) as session:
#         # Eventos do pacote #100
#         E_100_1 = PackageEvent(type='PACOTE_INTEGRADO', package_id=100, attributes = { "company_id": "shopee", "integrado": True } )
#         E_100_2 = PackageEvent(type='PACOTE_BIPADO', package_id=100, attributes = { "local": "FCA" })
#         E_100_3 = PackageEvent(type='PACOTE_SEPARADO', package_id=100, attributes = { "local": "FCA", "position": 1234 })
#         E_100_4 = PackageEvent(type='TRANSFERENCIA_INICIADA', package_id=100, 
#             attributes = { 
#                 "moving": True, 
#                 "destination": "SMT",
#                 "place": "exm0c0123"
#             })
#         E_100_5 = PackageEvent(type='TRANSFERENCIA_TERMINADA', package_id=100, 
#             attributes = { 
#                 "moving": False
#             })        
#         session.add_all([E_100_1, E_100_2, E_100_3, E_100_4, E_100_5])
#         # Eventos do pacote #200
#         E_200_1 = PackageEvent(type='PACOTE_INTEGRADO', package_id=200, attributes = { "company_id": "shopee", "integrado": True } )
#         E_200_2 = PackageEvent(type='PACOTE_BIPADO', package_id=200, attributes = { "local": "SMT" })
#         E_200_3 = PackageEvent(type='PACOTE_SEPARADO', package_id=200, attributes = { "local": "SMT", "position": 6000 })
#         session.add_all([E_200_1, E_200_2, E_200_3])
#         # Commit all
#         session.commit()

logging.info("PackageEvent populated.")