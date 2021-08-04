class SingleElement:

    def __init__(self, by, search_identifier):
        self.by = by
        self.search_identifier = search_identifier

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.driver.find_element(self.by, self.search_identifier)


class MultiElement(SingleElement):

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.driver.find_elements(self.by, self.search_identifier)
