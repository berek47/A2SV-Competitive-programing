class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return (ord(coordinates[1]) ^ ord(coordinates[0])) & 1
