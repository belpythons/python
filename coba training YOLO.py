
from roboflow import Roboflow
rf = Roboflow(api_key="OlOv8PNn4jcRnACPJ7sk")
project = rf.workspace("hanif-nurkhalis-ohqsm").project("coba1-oqmby")
version = project.version(1)
dataset = version.download("yolov8")