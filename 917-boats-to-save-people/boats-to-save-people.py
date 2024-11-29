class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        light, heavy = 0, len(people) - 1
        boats = 0

        while light <= heavy:
            # If the lightest and heaviest person can share a boat
            if people[light] + people[heavy] <= limit:
                light += 1  # Move the light pointer to the next lightest person
            # In all cases, the heaviest person gets a boat
            heavy -= 1
            boats += 1

        return boats

