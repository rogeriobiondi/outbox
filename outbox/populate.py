import logging

from .services.services import recreate_database, record_event

logging.basicConfig(level=logging.INFO)

# Truncate data
recreate_database()

# Populate data
logging.info("Populating events...")
record_event(type = 'INTEGRATED', package_id = 100, attributes = { "company_id": "my_company", "integrated": True } )
record_event(type='CHECKED', package_id=100, attributes = { "local": "FCA" });
record_event(type='SEPARATED', package_id=100, attributes = { "local": "FCA", "position": 1234 })
record_event(type='TRANSFER_INITIATED', 
    package_id=100, 
    attributes = { 
        "moving": True, 
        "destination": "DEST",
        "license_plate": "exm0c0123"
    }
)
record_event(type='TRANSFER_FINISHED', 
    package_id=100, 
    attributes = { 
        "moving": False
    }
)
      
record_event(type='INTEGRATED', package_id=200, attributes = { "company_id": "shopee", "integrado": True } )
record_event(type='CHECKED', package_id=200, attributes = { "local": "SMT" })
record_event(type='SEPARATED', package_id=200, attributes = { "local": "SMT", "position": 6000 })
logging.info("PackageEvent populated.")
logging.info("")