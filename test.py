import sys
import os


env_dir = os.environ.get("DB_CONTROL_PATH")
print(env_dir)
sys.path.append(env_dir)