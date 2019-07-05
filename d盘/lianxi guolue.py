# def upper(method):
#     print("请输入数据")
#
#     def wrappeer(*args, **kwargs):
#         new_args = []
#         new_kwargs = {}
#         for a in args:
#             if isinstance(a, str):
#                 new_args.append(a.upper())
#             else:
#                 new_args.append(a)
#         for key, vaule in kwargs.items():
#             if key =='name':
#                 raise EnvironmentError
#             else:
#                 if isinstance(vaule, str):
#                     new_kwargs[key] = vaule.upper()
#                 else:
#                     new_kwargs[key] = vaule
#
#         return method(*new_args, **new_kwargs)
#
#     return wrappeer
# class async:
#     def __init__(self, method):
#         self.methon =method
#     def __call__(self, *args, **kwargs):
#         new_args = []
#         new_kwargs = {}
#         for a in args:
#             if isinstance(a, str):
#                 new_args.append(a.upper())
#             else:
#                 new_args.append(a)
#         for key, vaule in kwargs.items():
#             if key == 'name':
#                 raise EnvironmentError
#             else:
#                 if isinstance(vaule, str):
#                     new_kwargs[key] = vaule.upper()
#                 else:
#                     new_kwargs[key] = vaule
#
#             return self.methon(*new_args, **new_kwargs)
#
#
# @async
# def siyan(*args, **kwargs):
#     print(args, kwargs)
#
#
# siyan(n=2)

def argument_validator(**kwargs_template):
    template = {}
    for k, v in kwargs_template.items():
        arg_name, arg_type = k.split("__")
        arg_required = v
        template[arg_name] = (arg_type, arg_required)

    def method_func(method):
        def wrapper(*args, **kwargs):
            new_kwargs = {}
            new_kwargs.update(kwargs)

            for arg_name, (arg_type, arg_required) in template.items():
                if arg_required and arg_name not in kwargs:
                    raise Exception("Required argument: " + arg_name)
                new_kwargs[arg_name] = eval(arg_type)(kwargs[arg_name])

            return method(*args, **new_kwargs)

        return wrapper

    return method_func



