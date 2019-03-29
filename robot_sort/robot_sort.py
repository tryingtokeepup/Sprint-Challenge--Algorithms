
# You have been given a robot with very basic capabilities:

# It can move left or right.
# It can pick up an item
# If it tries to pick up an item while already holding one, it will swap the items instead.
# It can compare the item it's holding to the item in front of it.
# It can switch a light on its head on or off.
# Your task is to program this robot to sort lists using ONLY these abilities.

# Rules
# Inside the Robot_Sort directory you'll find the robot_sort.py file. Open it up and read through each of the robot's abilities.
# Once you've understood those, start filling out the sort() method following these rules:

# You may use any pre-defined robot methods.
# You may NOT modify any pre-defined robot methods.
# You may use logical operators. (if, and, or, not, etc.)
# You may use comparison operators. ( > , >= , < , <= , == , is, etc.)
# You may use iterators. (while, for, break, continue)
# You may NOT store any variables. (=)
# You may NOT access any instance variables directly. (self._anything)
# You may NOT use any Python libraries or class methods. (sorted(), etc.)
# You may define robot helper methods, as long as they follow all the rules.

# Make sure you understand the problem and all of the rules! A solution that breaks the rules will receive no credit.

# If you're unsure if an operator or method is allowed, ask.

# Lay out some numbered cards in a line and try sorting them as if you were the robot.

# Come up with a plan and write out your algorithm before coding. If your plan is sound but you don't reach a working implementation in three hours, you may receive partial credit.

# There is no efficiency requirement but you may lose points for an unreasonably slow solution. Tests should run in far less than 1 second.

# We discussed a sorting method this week that might be useful. Which one?

# The robot has exactly one bit of memory: its light. Why is this important?

# Algorithim plan:
# The algorithim necessary for this challenge seems closest to the bubble-sort algorithim. We need the light as a store for our binary
# operator, sort_occured, which will keep the robot sorting through the array until we have successfully sorted through the whole array
# We start the robot with the light on. Then, we enter the loop, and then immediately turn the light off, so if there are no swaps
# during the current traversal of the array, it stays off, and can exit the loop after its current iteration.
# We then have the robot go through the array from the left side, comparing the item on its left
# to the item on its right. If the item on the left is greater than the right, we swap, AND we turn on the `swap` light, if its not on.
# Then we move the robot to the right, and continue the process until we hit len(array - 2), or the the index right before the last index.
# Compare, swap if necessary, and then continue the loop if and ONLY if the swap light is on.
# If all goes well, after the last loop through the array, it will exit the loop and return the sorted array.
# So, that's the plan. Let's try it out!


class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"

    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"

    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # Fill this out
        # we only want to run this while the light is on
        while self.light_is_on is True:
            # we need to check if we are at the beginning of the array, if we cant move any more left, we are at the beginning
            if self.can_move_left is False:
                # turn off the light so that if we are all sorted by the end, we can exit the loop
                self.set_light_off()
                # we need to get the item at index 0, so call the swap now
                self.swap_item()
                #


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1,
         45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)
