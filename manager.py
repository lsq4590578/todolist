# 做脚本迁移使用
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
# from backend.__init__ import create_app
from backend.run import create_app
from backend.models import *
app = create_app


manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)


if __name__ == '__main__':
    manager.run()
