"""Define a function to check if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class
"""
def inherits_from(obj, a_class):
    """Args:
            - obj: the object to check
            - a_class: the class to compare against
        returns:
            - true if obj is an instance of class that inherited
                from a_class; otherwise, false
    """
    return issubclass(type(obj), a_class)