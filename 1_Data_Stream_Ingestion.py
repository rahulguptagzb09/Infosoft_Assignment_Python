"""
Problem #1 - Data Stream Ingestion
In a data stream, data is read in consecutive chunks - so you only have access to a certain portion of data at a given time. This is in contrast to having an entire sequence available at once. For example, Netflix and Youtube use streaming to allow users to watch chunks of video, rather than have user wait for the entire video to load - before they can start watching.
Design a system that receives a stream of strings along with timestamps. Each unique string should be printed at most every 5 seconds (i.e., string printed at timestamp t will prevent the same message from being printed until t + 5 seconds have passed).
All strings will be received in chronological order. Several strings may arrive at the same time.
Implement the DataStream class:
• DataStream creates a data_stream object
• bool should_output_data_str(int timestamp, str data_str) returns true if the data_string
should be printed in the provided timestamp, otherwise returns false
Input
data_stream = DataStream()
data_stream.should_output_data_str(timestamp=0, data_string=“hello”)
data_stream.should_output_data_str(timestamp=1, data_string=“world”)
data_stream.should_output_data_str(timestamp=6, data_string=“hello”)
data_stream.should_output_data_str(timestamp=7, data_string=“hello”)
data_stream.should_output_data_str(timestamp=8, data_string=“world”)
Output
[true, true, true, false, true]

Explanation:
1. Class Initialization:
    - In the __init__ method, we initialize an empty dictionary self.data. This dictionary stores the most recent timestamp for each unique string.

2. The should_output_data_str Method:
    - This method checks if a string data_string should be printed at the given timestamp.
    - First, it checks if the data_string has been seen before in `self.data` and if the time difference between the current timestamp and the last printed timestamp is less than 5 seconds. If true, it returns False (meaning the string should not be printed).
    - If either the string is not in the dictionary or the timestamp difference is greater than or equal to 5 seconds, it updates the dictionary with the new timestamp and returns True, indicating the string should be printed.

3. Test Cases:
    - The test cases demonstrate how the system ensures a message is printed only once every 5 seconds, updating the timestamp each time a message is printed.

Time and Space Complexity:

- Time Complexity: Each operation (checking and updating the timestamp in the dictionary) takes O(1) time because dictionary lookups, updates, and insertions are O(1) on average.
- Space Complexity: In the worst case, if all messages are unique, the space complexity is O(n), where n is the number of unique messages stored in the dictionary.

"""


class DataStream:
    """
    The DataStream class is designed to manage a stream of strings, ensuring each string is printed at most once every 5 seconds.
    We use a hashmap (dictionary) to map each string to its most recent timestamp.
    The space complexity is O(n), where n is the number of unique messages, and the time complexity for retrieving and updating the hashmap is O(1) on average.
    """

    def __init__(self):
        """
        Initializes the DataStream object.
        The `data` dictionary will hold strings as keys and their corresponding last timestamp as values.
        """
        self.data = (
            {}
        )  # A dictionary to store the last timestamp when a message was printed.

    def should_output_data_str(self, timestamp: int, data_string: str) -> bool:
        """
        Determines if a message should be printed based on the given timestamp and the data string.
        - If the string has been printed in the last 5 seconds, it will not be printed again.
        - Otherwise, it will be printed and the timestamp will be updated.
        Arguments:
            timestamp -- the current timestamp for the message
            data_string -- the string data that is being checked
        Returns:
            bool -- True if the string should be printed, False if it shouldn't.
        """
        # Check if the message exists in the `data` dictionary and if the time difference between the current timestamp and
        # the stored timestamp is less than 5 seconds. If both conditions are met, we should not print the string.
        if data_string in self.data and timestamp - self.data[data_string] < 5:
            return False

        # Update the timestamp for the current message to the latest one.
        self.data[data_string] = timestamp
        return True


# Create an instance of the DataStream class
data_stream = DataStream()

# Test case 1: Message "hello" at timestamp 0 should be printed.
print(
    data_stream.should_output_data_str(timestamp=0, data_string="hello")
)  # Expected: True

# Test case 2: Message "world" at timestamp 1 should be printed.
print(
    data_stream.should_output_data_str(timestamp=1, data_string="world")
)  # Expected: True

# Test case 3: Message "hello" at timestamp 6 should be printed, as it was last printed at timestamp 0.
print(
    data_stream.should_output_data_str(timestamp=6, data_string="hello")
)  # Expected: True

# Test case 4: Message "hello" at timestamp 7 should not be printed, as it was last printed at timestamp 6.
print(
    data_stream.should_output_data_str(timestamp=7, data_string="hello")
)  # Expected: False

# Test case 5: Message "world" at timestamp 8 should be printed, as it was last printed at timestamp 1.
print(
    data_stream.should_output_data_str(timestamp=8, data_string="world")
)  # Expected: True
