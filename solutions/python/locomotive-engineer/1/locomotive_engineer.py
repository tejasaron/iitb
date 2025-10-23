"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return [*args]


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    f_1,f_2,f_3,*f_rem = each_wagons_id
    

    return [f_3,*missing_wagons,*f_rem,f_1,f_2]


def add_missing_stops(routing,**kwargs):
    """Add missing stops to route dict.
    

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    routing["stops"] = [val for val in kwargs.values()]
    return routing
    


def extend_route_information(route,details):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route,**details}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    a , b, c = wagons_rows[0],wagons_rows[1],wagons_rows[2]
    a_1, a_2, a_3 = a
    b_1, b_2, b_3 = b
    c_1, c_2, c_3 = c

    return[[a_1,b_1,c_1],[a_2,b_2,c_2],[a_3,b_3,c_3]]
