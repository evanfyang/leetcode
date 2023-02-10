def flipping_an_image(image):
    row_length = len(image[0])

    for row in image:
        for index in range((row_length + 1) // 2):
            row[index], row[row_length - index - 1] = row[row_length - index - 1] ^ 1, row[index] ^ 1

    return image 

def main():
    image = [
        [1,0,1],
        [1,1,1],
        [0,1,1]
    ]
    print("Input: image = " + str(image))
    print("Output: " + str(flipping_an_image(image)))
    print()
    
    image = [
        [1,1,0,0],
        [1,0,0,1],
        [0,1,1,1], 
        [1,0,1,0]
    ]
    print("Input: image = " + str(image))
    print("Output: " + str(flipping_an_image(image)))
    print()

    image = [
        [1,1,0],
        [1,0,1],
        [0,0,0]
    ]
    print("Input: image = " + str(image))
    print("Output: " + str(flipping_an_image(image)))
    print()

    image = [
        [1,1,0,0],
        [1,0,0,1],
        [0,1,1,1],
        [1,0,1,0]
    ]
    print("Input: image = " + str(image))
    print("Output: " + str(flipping_an_image(image)))
    print()

main()