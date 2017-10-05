from peek_plugin_base.storage.AlembicEnvBase import AlembicEnvBase

from peek_plugin_generic_diagram_menu._private.storage import DeclarativeBase
from peek_plugin_generic_diagram_menu._private.storage.DeclarativeBase import loadStorageTuples

loadStorageTuples()

alembicEnv = AlembicEnvBase(DeclarativeBase.DeclarativeBase.metadata)
alembicEnv.run()