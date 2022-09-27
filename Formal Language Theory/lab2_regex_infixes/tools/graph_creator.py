class Graph_creator():
    def __init__(self, filepath, buffer):
        self.buffer = buffer
        self.strings_buffer = ['digraph G {', '\n}']
        self.filepath = filepath

    def add_edge(self, d):
        self.strings_buffer.insert(
            -1,
            f'\n{d["parent"]} [label = "{d["parent_label"]}"]'
        )

        self.strings_buffer.insert(
            -1,
            f'\n{d["child"]} [label = "{d["child_label"]}"]'
        )

        self.strings_buffer.insert(
            -1,
            f'\n{d["parent"]} -> {d["child"]} [label = "{d["label"]}"]'
        )

    def write_to_file(self):
        for d in self.buffer:
            self.add_edge(d)

        with open(self.filepath, 'w') as f:
            f.writelines(self.strings_buffer, )
