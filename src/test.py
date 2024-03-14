import os
import dotenv
import pandas as pd

project_dir = os.path.join(os.path.dirname(__file__), os.pardir)
dotenv_path = os.path.join(project_dir, '.env')
dotenv.load_dotenv(dotenv_path)

data_path = os.getenv("DATA_PATH")
print(data_path)


data = pd.read_csv(data_path)

print(data.head())