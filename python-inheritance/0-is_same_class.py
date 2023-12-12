def is_same_class(obj, a_class):
    """Check if the object is exactly an instance of the specified class
    Args:
        - obj: the object to check
        - a_class: the class to compare against
    returns:
        - true if obj is an instance of a_class; otherwise, false
    """
    return type(obj) is a_class