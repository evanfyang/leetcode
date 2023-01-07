def flood_fill(image, x, y, new_color):
    if image[x][y] != new_color:
        fill_pixels_dfs(image, x, y, image[x][y], new_color)
    return image

def fill_pixels_dfs(self, image, x, y, old_color, new_color):
    if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]):
        return
    if image[x][y] != old_color:
        return

    image[x][y] = new_color

    fill_pixels_dfs(image, x - 1, y, old_color, new_color)
    fill_pixels_dfs(image, x + 1, y, old_color, new_color)
    fill_pixels_dfs(image, x, y - 1, old_color, new_color)
    fill_pixels_dfs(image, x, y + 1, old_color, new_color)

def main():
    image = [
        [1,1,1], 
        [1,1,0], 
        [1,0,1]
    ] 
    x = 1
    y = 1
    new_color = 2
    print("Input: " + "image = " + str(image) + ", x = " + x + ", y = " + y + ", new_color = " + new_color)    
    print("Output: " + str(flood_fill(image)))
    
    image = [
        [0,0,0], 
        [0,0,0]
    ] 
    x = 0
    y = 0
    new_color = 0
    print("Input: " + "image = " + str(image) + ", x = " + x + ", y = " + y + ", new_color = " + new_color)    
    print("Output: " + str(flood_fill(image)))

main()
