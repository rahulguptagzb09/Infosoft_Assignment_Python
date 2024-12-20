"""
Problem #3 - Debug Calendar Design
Your teammate has implemented a calendar program, but it doesn’t work as expected.
Ideally, a user should be able to add a new event, if it does not cause a double booking. Double bookings
occur when two events overlap in time. For example, Event A lasts from Saturday 2 pm - 5 pm and Event B
lasts Saturday 3 pm - 4 pm. These events overlap and would be considered a double booking.
Events are represented as a pair of ints - start and end. Two events can be scheduled back to back, e.g.
Event A can be [2,3) and Event B can be [3, 4).
Your teammate has already implemented the Calendar class:
• Calendar() Initializes the calendar object.
• boolean schedule(int start, int end) Returns true if the event can be added without causing
a double booking. Returns false otherwise and does not add the event to the calendar.
Your teammate’s code can be found in the attached file calendar.py. Please debug the code to fix the
current issues. When submitting this portion of the assignment, please attach your fixed code and a
README.md file that explains how you debugged it step-by-step and what the underlying issue was. We
may discuss this document at the end of the evaluation.
Example Input & Output
calendar = Calendar()
calendar.book(5, 10) -> Expect True
calendar.book(8, 13) -> Expect False

Code Explanation and Debugging:

The Node Class:
- Purpose: Each node represents an event, containing:
  - start: Start time of the event.
  - end: End time of the event.
  - left_child: A child node that stores events that end earlier than this node.
  - right_child: A child node that stores events that start later than this node.
  
- insert Method:
  - If the new event's start time is after the current node's end time (node.start >= self.end), it is inserted into the right subtree. If there's no right child, it becomes the right child.
  - If the new event's end time is before the current node's start time (node.end <= self.start), it is inserted into the left subtree. If there's no left child, it becomes the left child.
  - If neither condition is met, it means the event overlaps with the current event, so we return False (indicating a double booking).

The Calendar Class:
- Purpose: The Calendar class uses a binary search tree (BST) to track events and prevent double bookings.
- book Method:
  - If the calendar is empty (i.e., the root is None), the first event is added as the root.
  - If the calendar already has events, it attempts to insert the new event using the insert method of the root node.

Issues in the Original Code:
1. Incorrect Condition in insert Method: The original code had incorrect comments and conditions, such as:
   - if node.start <= self.end: and elif node.end >= self.start:. These conditions would incorrectly allow overlapping events. The correct condition to check should be node.start >= self.end for non-overlapping events that can be inserted on the right, and node.end <= self.start for non-overlapping events that can be inserted on the left.
   
2. Missing Return for Successful Insertion: The insert method didn't always handle cases correctly when a new event could be inserted. The fixed code properly checks whether an event can be placed in the left or right subtrees based on the conditions.

Complexity:
- Time Complexity:
  - The insert method works with a binary search tree. In the worst case (if the tree is unbalanced), the time complexity is O(n), where n is the number of events already booked. If the tree is balanced, it operates in O(log n).
  
- Space Complexity:
  - The space complexity is O(n) because each event is stored in a node of the tree.

How the Debugging Was Done:
- Identified that the conditions for checking event overlap in the insert method were incorrect.
- Fixed the overlap check conditions to prevent double booking and ensure the correct event insertion behavior.
- Verified the functionality using example test cases.

This updated solution should now handle the calendar booking correctly, preventing double bookings and allowing for efficient event insertion using a binary search tree.

"""

from typing import Optional

class Node():
    """
    A Node class representing an event in the calendar. Each node contains:
    - start: the start time of the event.
    - end: the end time of the event.
    - left_child: the left child node in the binary search tree (BST), representing events that finish before this event starts.
    - right_child: the right child node in the BST, representing events that start after this event ends.
    """

    def __init__(self, start: int, end: int):
        """
        Initialize a new Node (event) with start and end times.
        Arguments:
          start -- the start time of the event
          end -- the end time of the event
        """
        self.start: int = start  # Event start time
        self.end: int = end      # Event end time
        self.left_child: Optional[Node] = None  # Left child in the BST
        self.right_child: Optional[Node] = None  # Right child in the BST
    
    def insert(self, node: 'Node') -> bool:
        """
        Attempts to insert a new event node into the calendar's binary tree while checking for conflicts.
        The method returns True if the event was successfully inserted (no conflicts), False if there's a conflict.
        Arguments:
          node -- the new event node that needs to be inserted
        """
        # if node.start <= self.end: # Incorrect Line
        # If the new event's start time is after the current node's end time, it can go to the right child (events that start later)
        if node.start >= self.end:
            if not self.right_child:
                self.right_child = node
                return True
            # return self.left_child.insert(node) # Incorrect Line
            # Recursively try to insert in the right child subtree
            return self.right_child.insert(node)
        
        # elif node.end >= self.start:  # Incorrect Line
        # If the new event's end time is before the current node's start time, it can go to the left child (events that end earlier)
        elif node.end <= self.start:
            if not self.left_child:
                self.left_child = node
                return True
            # Recursively try to insert in the left child subtree
            return self.left_child.insert(node)
        
        # Added return False
        # If neither condition is met, it means the events overlap and cannot be scheduled
        return False


class Calendar():
    """
    The Calendar class allows adding events (start, end) and ensuring there are no double bookings.
    It uses a binary search tree (BST) to store events in a way that makes it efficient to check for overlapping events.
    """

    def __init__(self):
        """
        Initializes an empty calendar (BST with no events).
        """
        self.root: Optional[Node] = None  # Root node of the binary search tree
    
    def book(self, start: int, end: int) -> bool:
        """
        Attempts to book an event in the calendar.
        Arguments:
          start -- the start time of the event
          end -- the end time of the event
        Returns:
          bool -- True if the event was successfully booked (no conflicts), False if it caused a double booking
        """
        if self.root is None:
            # If the calendar is empty, create a new root node
            self.root = Node(start=start, end=end)
            return True
        
        # If the calendar is not empty, try to insert the new event into the BST
        return self.root.insert(node=Node(start, end))


# Example usage of the Calendar class
myCalendar = Calendar()

# Try booking an event from time 5 to 10
print(myCalendar.book(5, 10))  # Expected: True (Event booked successfully)
# Try booking an event from time 8 to 13 (this overlaps with the previous event)
print(myCalendar.book(8, 13))  # Expected: False (Double booking)
# Try booking another event from time 10 to 15 (this does not overlap with any existing events)
print(myCalendar.book(10, 15))  # Expected: True (Event booked successfully)
