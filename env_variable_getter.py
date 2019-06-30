import os
from dotenv import load_dotenv


class EnvVariableGetter():
    def get_variable(self, variable_name):
        project_folder = os.getcwd()  # gets the project directory
        # overwrites env file with your .env file that you should have made in the root of this project
        load_dotenv(os.path.join(project_folder, '.env'))
        return os.getenv(variable_name)
