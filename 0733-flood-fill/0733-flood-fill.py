class Solution:
    def floodFill(self, image, sr, sc, newColor):
        def dfs(r, c, originalColor):
            if (
                r < 0
                or r >= len(image)
                or c < 0
                or c >= len(image[0])
                or image[r][c] != originalColor
            ):
                return

            image[r][c] = newColor  # Change the color of the current pixel
            # Explore the 4-directionally connected pixels
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(r + dr, c + dc, originalColor)

        originalColor = image[sr][sc]
        if originalColor != newColor:  # Avoid unnecessary recursion
            dfs(sr, sc, originalColor)

        return image
