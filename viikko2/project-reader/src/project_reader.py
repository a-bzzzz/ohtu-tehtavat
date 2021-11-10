from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        # print(content)    # 1. alkuperäisen muotoilun mukainen tulostus
        # print("------------------------")
        toml_loads = toml.loads(content)
        # print(toml_loads) # 2. toml-serialisoinnin mukainen tulostus
        # print("------------------------")
        # 3. Project-olion palautus
        return Project(toml_loads['tool']['poetry']['name'], toml_loads['tool']['poetry']['description'], toml_loads['tool']['poetry']['dependencies'], toml_loads['tool']['poetry']['dev-dependencies'])