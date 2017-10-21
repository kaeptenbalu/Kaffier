import os
from flask_script import Manager
from flask_migrate import MigrateCommand
from app import create_app


config_name = os.getenv('FLASK_CONFIG')
manager = Manager(create_app(config_name))
manager.add_option("-c", "--config", dest="config_module", required=False)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
