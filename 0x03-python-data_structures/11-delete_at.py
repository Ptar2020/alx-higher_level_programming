#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    """Deletes at the given index, an element

    Args:
        my_list (list, optional): The original list.
        idx (int, optional): The index point from which to delete.

    Returns:
        list: new_list if idx is within range or not negative, else my_list
    """
    new_list = my_list.copy()
    if idx < 0 or idx > len(my_list):
        return (my_list)
    else:
        del new_list[idx]
        return (new_list)


if __name__ == "__main__":
    delete_at()

