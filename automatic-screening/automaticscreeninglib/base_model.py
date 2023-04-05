from abc import ABC
import inspect
import numpy as np

def sig_to_param(signature):
    return {
        key: value.default
        for key, value in signature.parameters.items()
        if value.default is not inspect.Parameter.empty
    }

class Base_Model(ABC):

    @property
    def default_param(self):
        cur_classs = self.__class__
        default_parameters = sig_to_param(inspect.signature(self.__init__))
        while cur_classs != Base_Model:
            signature = inspect.signature(super(cur_classs, self).__init__)
            new_parameters = sig_to_param(signature)
            default_parameters.update(new_parameters)
            cur_classs = cur_classs.__bases__[0]
        return default_parameters
    
    @property
    def get_parameters(self):
        parameters = self.default_param
        for param in list(parameters):
            try:
                parameters[param] = getattr(self, param)
            except AttributeError:
                del parameters[param]
                continue
            if isinstance(parameters[param], np.integer):
                parameters[param] = int(parameters[param])

        return parameters
    
    