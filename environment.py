class GuestRoom:
    def __init__(self):
        self.trash_items = ["plastic cup", "paper"]
        self.items_on_floor = ["pillow", "magazine"]
        self.bed_needs_making = True

    def is_clean(self):
        return (
            len(self.trash_items) == 0 and
            len(self.items_on_floor) == 0 and
            not self.bed_needs_making
        )
