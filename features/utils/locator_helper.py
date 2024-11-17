def get_locator(context, locator_name, locators_modules):

    for module in locators_modules:
        if hasattr(module, locator_name):
            return getattr(module, locator_name)

    raise ValueError(f"Locator '{locator_name}' not found in any of the provided locator modules.")