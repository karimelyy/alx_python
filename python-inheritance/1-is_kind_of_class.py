"""Define a function to check if the obcject is an instance of
    or if the object is an instance of class that interited from
    the specified class
"""
def is_kind_of_class(obj, a_class):
    """Args:
            - obj: the object to check
            - a_class: the class to compare against
        returns:
            - true if obj is an instance of a_class or a subclass of a_class; otherwise, false
    """
    return isinstance(obj, a_class)