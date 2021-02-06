class University:
    """A Canadian University

    === Attributes ===
    name: the name of the University.

    === Sample Usage ===
    >>> u = University("University of Waterloo")
    >>> u.name
    "University of Waterloo"
    """

    name: str

    def __init__(self, name) -> None:
        """Initialize the class University
        >>> u = University("UofT")
        >>> u.name
        "UofT"
        """
        self.name = name


if __name__ == '__main__':
    import doctest

    doctest.testmod()
