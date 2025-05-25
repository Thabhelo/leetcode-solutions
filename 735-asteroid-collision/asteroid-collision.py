class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        
        for asteroid in asteroids:
            # If result is empty or asteroid is moving right, just add it
            if not result or asteroid > 0:
                result.append(asteroid)
            else:  # asteroid is moving left (negative)
                # Check collisions with right-moving asteroids
                while result and result[-1] > 0:
                    if abs(asteroid) > result[-1]:
                        # Current asteroid is bigger, destroy the right-moving one
                        result.pop()
                    elif abs(asteroid) == result[-1]:
                        # Same size, both explode
                        result.pop()
                        break
                    else:
                        # Current asteroid is smaller, it explodes
                        break
                else:
                    # This else belongs to the while loop
                    # Executes only if loop completes without breaking
                    # (meaning asteroid survived all collisions)
                    result.append(asteroid)
                    
        return result