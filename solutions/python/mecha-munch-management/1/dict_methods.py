"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    cart = current_cart.copy()

    # Loop through each item in the list-like iterable
    for item in items_to_add:
        if item in cart:
            cart[item] += 1
        else:
            cart[item] = 1

    return cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    user_cart = {}
    for item in notes:
        if item in user_cart:
            user_cart[item] += 1
        else:
            user_cart[item] = 1

    return user_cart


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    ideas.update(dict(recipe_updates))
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    return sorted(cart.items())

def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """# Combine the info for each item
    fulfillment_cart = {}

    for item, quantity in cart.items():
        aisle, refrigeration = aisle_mapping.get(item, ['Unknown', False])
        fulfillment_cart[item] = [quantity, aisle, refrigeration]

    # Sort in reverse alphabetical order
    return dict(sorted(fulfillment_cart.items(), reverse=True))
    pass


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    updated_inventory = store_inventory.copy()

    for item, (order_qty, aisle, refrigeration) in fulfillment_cart.items():
        if item in updated_inventory:
            # assign current qty with the value from store inventory
            current_qty = updated_inventory[item][0]

            # Subtract ordered quantity from stock
            new_qty = current_qty - order_qty

            # If zero or below → mark as 'Out of Stock'
            if new_qty <= 0:
                updated_inventory[item][0] = 'Out of Stock'
            else:
                updated_inventory[item][0] = new_qty

    return updated_inventory

