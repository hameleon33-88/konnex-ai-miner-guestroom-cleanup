class CleaningRobot:
    def __init__(self, room):
        self.room = room

    def collect_trash(self):
        if self.room.trash_items:
            print("Robot is collecting trash...")
            self.room.trash_items.clear()

    def organize_items(self):
        if self.room.items_on_floor:
            print("Robot is organizing items...")
            self.room.items_on_floor.clear()

    def make_bed(self):
        if self.room.bed_needs_making:
            print("Robot is making the bed...")
            self.room.bed_needs_making = False

    def clean_guestroom(self):
        self.collect_trash()
        self.organize_items()
        self.make_bed()
