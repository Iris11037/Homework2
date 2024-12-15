def introspection_info(obj):
    type_obj = type(obj)
    attributes_obj = dir(obj)
    methods_obj = [method for method in attributes_obj if callable(getattr(obj, method))]
    module_obj = obj.__class__.__module__
    info_obj = {'type': type_obj, 'attributes': attributes_obj, 'methods': methods_obj, 'module': module_obj}
    return info_obj

number_info = introspection_info(42)
print(number_info)
