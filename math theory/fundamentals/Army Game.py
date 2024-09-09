# https://www.hackerrank.com/challenges/game-with-cells/problem?isFullScreen=true

# Luke is daydreaming in Math class. He has a sheet of graph paper with n rows and m columns,
# and he imagines that there is an army base in each cell for a total of n.m bases. 
# He wants to drop supplies at strategic points on the sheet, marking each drop point with a red dot. 
# If a base contains at least one package inside or on top of its border fence, then 
# it's considered to be supplied

def gameWithCells(n, m):
    return (n//2+n%2)*(m//2+m%2)


# Components:
    # n: Represents the number of rows.
    # m: Represents the number of columns.

# Step-by-Step Breakdown:
    # n/2 + n%2:
        # n/2: This gives the number of pairs of rows. For example, if n = 5, then n/2 = 2 because there are 2 pairs of rows.
        # n%2: This gives the remainder when n is divided by 2. It tells you whether there's an extra row after pairing. For example, if n = 5, then n%2 = 1, indicating there is one unpaired row.
    # Together, n/2 + n%2 calculates how many rows you would need if you want to cover every other row in a grid, potentially with one extra row if n is odd.

# m/2 + m%2:
    # Similar logic applies here, but for the columns.

# Combining the Two Parts:
    # The formula multiplies the number of necessary rows (n/2 + n%2) by the number of necessary columns (m/2 + m%2).

