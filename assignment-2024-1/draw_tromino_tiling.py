from PIL import Image, ImageDraw

# Output of backtracking
targetFile = "./tromino_tiling_grid_4x4.txt"
generatedImage = "./tromino_tiling_visual.png"


def create_image(grid, filename):
    """
     Create an image using letters of R G B with the equivalent color 
    """  
    color_map = {'R': (255, 0, 0), 'G': (0, 255, 0), 'B': (0, 0, 255), 'X': (0, 0, 0)}
    cell_size = 20  # Adjust the size of each cell as needed
    image_size = (len(grid[0]) * cell_size, len(grid) * cell_size)
    image = Image.new("RGB", image_size, color=(255, 255, 255))
    draw = ImageDraw.Draw(image)

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell in color_map:  
                color = color_map[cell]
                draw.rectangle([x * cell_size, y * cell_size, (x + 1) * cell_size, (y + 1) * cell_size], fill=color)

    image.save(filename)
    image.show()




def read_grid_from_file(targetFile):
    """
    Read from txt and construct a grid for visualization purposes
    """
    with open(targetFile, "r") as file:
    # Initialize an empty array
    
        grid = []
        for line in file:
            row_array = [char for char in line.strip() if char != ' ']
            grid.append(row_array)


    # print(grid)
    return grid



grid = read_grid_from_file(targetFile)

print("Grid extracted from file:")


# Now let's call the create_image function with the grid
create_image(grid, generatedImage)