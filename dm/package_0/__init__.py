
import digital_machine
import digital_machine.templates as tmpl
from digital_machine import dmCompile

from .workshop import workshop
from .shop import shop
from .equipment import equipment
from .fabric import fabric
from .warehouse import warehouse
from .Цех import Цех
from .inventory import inventory


try:
    from ._legacy import models as legacy_models
except ModuleNotFoundError:
    legacy_models = {}

py_model_collection = tmpl.PyModelCollection()



workshop().generate_model(digital_machine.digital_twin_model("package_0", "workshop"), py_model_collection)
shop().generate_model(digital_machine.digital_twin_model("package_0", "shop"), py_model_collection)
equipment().generate_model(digital_machine.digital_twin_model("package_0", "equipment"), py_model_collection)
fabric().generate_model(digital_machine.digital_twin_model("package_0", "fabric"), py_model_collection)
warehouse().generate_model(digital_machine.digital_twin_model("package_0", "warehouse"), py_model_collection)
Цех().generate_model(digital_machine.digital_twin_model("package_0", "Цех"), py_model_collection)
inventory().generate_model(digital_machine.digital_twin_model("package_0", "inventory"), py_model_collection)


models = py_model_collection.models
models.update(legacy_models)
