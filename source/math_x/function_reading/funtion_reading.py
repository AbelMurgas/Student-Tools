class AlgebraicFunctionReading:
    """
        This class is for working with algebraic function, validate and break down the attributes of the function
    """

    def __init__(self, *args, **kwargs) -> None:
        """
        #   args:
            2 args refers to a lineal funtion example: (2,3) = fx = 2x + 3
            3 args refers to a cuadratic funtion example: (2,3,4) = fx = 2x2 + 3x + 4
            therefor the more arguments increase the grade of the function

        #   Keyword arguments:
        #  lineal example:
            string_function -- string ot the function example: "fx=2x+30"

            diccionary_function -- dictionary of the function example: {xc=2,c=30}  c -> constant

            list_function -- list of the function example: =[2,30]

        # cuadratic example:
            string_function -- string ot the function example: "fx=x2+2x+4"

            diccionary_function -- dictionary of the function example: {x2=1,xc=2,c=30}  c -> constant

            list_function -- list of the function example: =[1,2,30]
        """
        self.__verify_arg(args, kwargs)
        # ---- default attribute ----
        self.list_function = []
        self.dict_function = {}
        self.str_function = ""
        self.grade = 0

    def __verify_arg(self, args, kwargs):
        """
            This funtion verify the args or the Kwargs and send error if some validation fail
        """
        kwargs_allows = ['str_function',
                         'dict_function', 'list_function']
        if args and kwargs:
            raise Exception(self.__sed_errors(4))
        if args:
            if not all(isinstance(n, (int, float)) for n in list(args)):
                raise Exception(self.__sed_errors(
                    3, f"Your arguments:\033[1m {args}"))
            self.grade = len(args)-1
            self.list_function = list(args)
        else:
            if not len(kwargs) == 1:
                raise Exception(self.__sed_errors(
                    2, f"and You put\033[1m {len(kwargs)}:{list(kwargs.keys())}"))
            else:
                if not list(kwargs.keys())[0] in kwargs_allows:
                    raise Exception(self.__sed_errors(
                        1, f"And you use\033[1m {list(kwargs.keys())[0]}"))
                index = kwargs_allows.index(list(kwargs.keys())[0])
                if index == 2:
                    if not type(list(kwargs.values())[0]) == list:
                        raise Exception(self.__sed_errors(
                            5, f", Expected \033[1m <class 'list'> \033[0;91m Obtained \033[1m {type(list(kwargs.values())[0])}"))
                    self.list_function = list(kwargs)
                elif index == 1:
                    if not type(list(kwargs.values())[0]) == dict:
                        raise Exception(self.__sed_errors(
                            5, f", Expected \033[1m <class 'dict'> \033[0;91m Obtained \033[1m {type(list(kwargs.values())[0])}"))
                    self.dict_function = kwargs[list(kwargs.keys())[0]]

                else:
                    if not type(list(kwargs.values())[0]) == str:
                        raise Exception(self.__sed_errors(
                            5, f", Expected \033[1m <class 'str'> \033[0;91m Obtained \033[1m {type(list(kwargs.values())[0])}"))
                    self.str_function = kwargs[list(kwargs.keys())[0]]

    def __sed_errors(self, n_error, extra_message=""):
        """
        This function is to send different error, in the process. \n
        Errors:\n
        1 - Only Allowed this representation of a funtion - string_function - diccionary_function - list_function -\n
        2 - Only Allowed one representacion of a funtion\n
        3 - Only Allowed numbers (int and float) as arg\n
        4 - Only can use args o kwargs(to access the others method of representation of a function) , but can't use both at same time\n
        5 - The type of the data is not what was expected 
        Args:
            name_e (int): Number of error
            extra_message (str): Extra message with the error.
        """
        error = {
            1: "Only Allowed these representation of a function - string_function - diccionary_function - list_function -",
            2: "Only Allowed 1 representacion of a function ",
            3: "Only Allowed numbers (int and float) as arg ",
            4: "Only can use args o kwargs(to access the others method of representation of a function) , but can't use both at same time ",
            5: "The type of the data is not what was expected "
        }
        if error.get(n_error):
            return '\033[91m' + error.get(n_error) + extra_message + '\033[0m'
        else:
            return print("Error not found")

    def __validate_dict_functio():
        pass
    def __validate_list_functio():
        pass
    def __validate_str_functio():
        pass


new = AlgebraicFunctionReading(str_function="2")
