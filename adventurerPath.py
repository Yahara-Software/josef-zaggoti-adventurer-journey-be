import math
import sys

def get_adventurer_path(directions: str) -> float:
    """
    Calculates the Euclidean distance from the starting point after following a series of directions.

    Parameters:
    directions (str): A string of directions where 'F' is forward, 'B' is backward, 'R' is right,
                      and 'L' is left. Each direction should be preceded by a number indicating the
                      number of steps in that direction.

    Returns:
    float: The Euclidean distance between the final position and the starting point.
    """
    x, y = 0, 0
    numStepsStr= ''
    for c in directions:
        if c.isdigit():
            numStepsStr += c
        else:
            steps = 1 # assume 1 step if no number precedes the direction
            if numStepsStr:
                steps = int(numStepsStr)
                numStepsStr = ''
            if c == 'F':
                y += steps
            elif c == 'B':
                y -= steps
            elif c == 'R':
                x += steps
            elif c == 'L':
                x -= steps
    dist = float(math.sqrt(x**2 + y**2))
    return dist

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Use path provided as a command-line argument if provided
        path = sys.argv[1]
    else:
        # Default path
        path = "15F6B6B5L16R8B16F20L6F13F11R"
    
    print("Directions:\t", path)
    print("Distance:\t", get_adventurer_path(path))