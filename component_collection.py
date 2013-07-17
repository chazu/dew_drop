from moka import *

def uniq(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]

def listify(gen):
    "Convert a generator into a function which returns a list"
    def patched(*args, **kwargs):
        return list(gen(*args, **kwargs))
    return patched

@listify
def flatten(container):
    for i in container:
        if isinstance(i, list) or isinstance(i, tuple):
            for j in flatten(i):
                yield j
        else:
            yield i

class ComponentCollection:

    def __init__(self, collection=None):
        if collection == None:
            self.data = []
        else:
            if hasattr(collection, 'data'):
                self.data = collection.data
            else:
                self.data = collection

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, index):
        return self.data[index]

    def append(self, value):
        "Delegates to underlying list"
        self.data.append(value)

    def list(self):
        # TODO Rename or get rid of this method
        for item in self.data:
            print(item.name)

    def with_flag(self, flag):
        """
        Return a ComponentCollection with all the components
        containing the flag
        """
        return ComponentCollection(List(self.data) \
            .keep(lambda x: x.state.has_flag(flag)))

    def is_empty(self):
        return len(self.data) == 0

    def recursively_collect_components(self, collection='components'):
        """
        Wrap recursively gathered components
        in a ComponentCollection
        """
        if collection == 'item_inputs':
            func = self.recursively_collect_item_inputs_to_list
        elif collection == 'item_outputs':
            func = self.recursively_collect_item_outputs_to_list
        else:
            func = self.recursively_collect_components_to_list
        return ComponentCollection(func())

    def recursively_collect_components_to_list(self):
        """
        Get all components recursively
        """
        if self.is_empty():
            return []
        else:
            return flatten(List(self.data) + List(self.data).map(lambda x: x.components.recursively_collect_components_to_list()))

    # def recursively_collect_item_inputs_to_list(self):
    #     """
    #     Get all item_inputs recursively
    #     """
    #     if self.is_empty():
    #         return []
    #     else:
    #         return flatten(List(self.data) + List(self.data).map(lambda x: x.item_inputs.recursively_collect_item_inputs_to_list()))

    # def recursively_collect_item_outputs_to_list(self):
    #     """
    #     Get all item_outputs recursively
    #     """
    #     if self.is_empty():
    #         return []
    #     else:
    #         return flatten(List(self.data) + List(self.data).map(lambda x: x.item_outputs.recursively_collect_item_outputs_to_list()))

    def inputs(self):
        """
        Return a ComponentCollection with all the components of
        this collection's inputs
        """
        return ComponentCollection(
            flatten(
                List(self.data) \
                    .map(lambda x: x.inputs)
                )
            )

    def outputs(self):
        """
        Return a ComponentCollection with all the components of
        this collection's outputs
        """
        return ComponentCollection(
            flatten(
                List(self.data) \
                    .map(lambda x: x.outputs)
                )
            )

    def duplexes(self):
        """
        Return a list with all the duplexes for the
        components in this collection
        """
        return ComponentCollection(
            uniq(
                List(
                    flatten(
                        self.data.map(lambda x: x.duplexes())
                    )
                )
            )
        )

if __name__ == "__main__":
    pass
