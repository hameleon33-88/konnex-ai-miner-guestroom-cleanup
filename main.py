from environment import GuestRoom
from robot import CleaningRobot

def run_simulation():
    print("Starting guestroom cleanup task...\n")

    room = GuestRoom()
    robot = CleaningRobot(room)

    robot.clean_guestroom()

    if room.is_clean():
        print("\nGuestroom is clean and ready.")
    else:
        print("\nGuestroom cleanup not finished.")

if __name__ == "__main__":
    run_simulation()
