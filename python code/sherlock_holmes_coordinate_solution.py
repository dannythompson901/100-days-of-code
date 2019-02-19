import turtle
import time
wn = turtle.Screen()  # set wn to the window object
wn.bgcolor("yellow")  # set the window background color

mike = turtle.Turtle()
mike.fillcolor('#2c2e30')
mike.pencolor('#2c2e30')
mike.pensize(2)
mike.speed(0)
mike.begin_fill()
mike.penup()
mike.goto(81, -22) #starting point of the drawing
mike.pendown()

sherlock_coordinates = [
    231, 172, 228, 160, 229, 154, 231, 150, 234, 148, 237, 144, 241, 141, 244, 139, 248, 138, 253, 137, 257, 135,
    263, 134, 267, 132, 272, 130, 277, 126, 281, 124, 283, 122,
    281, 120, 281, 117, 279, 115, 277, 113, 275, 111, 271, 108, 267, 105, 262, 103, 259, 100, 257, 98, 258, 88,
    256, 75, 254, 66, 251, 59, 246, 49, 242, 41, 237, 35, 233, 33, 229, 28, 224, 26, 222, 23, 216, 21, 211, 20,
    209, 18, 207, 16, 206, 12, 204, 10, 201, 8, 197, 6, 193, 5, 189, 6, 186, 8, 183, 10, 180, 12, 177, 13, 173,
    14, 167, 14, 162, 16, 156, 18, 151, 19, 147, 22, 144, 23, 140, 26, 135, 29, 130, 32, 127, 37, 124, 40, 120,
    46, 116, 49, 113, 53, 110, 56, 109, 59, 107, 60, 105, 63, 102, 64, 99, 66, 93, 67, 89, 68, 84, 70, 80, 70, 75,
    71, 71, 72, 68, 72, 65, 74, 62, 74, 60, 74, 70, 83, 74, 86, 79, 88, 83, 89, 87, 90, 91, 90, 96, 90, 100, 90,
    100, 94, 99, 98, 97, 101, 96, 103, 96, 108, 97, 111, 99, 113, 101, 116, 100, 118, 98, 120, 95, 123, 93, 128,
    91, 132, 88, 138, 85, 144, 83, 149, 81, 152, 80, 157, 79, 159, 81, 161, 83, 162, 85, 163, 88, 163, 91, 163,
    95, 166, 95, 171, 93, 176, 92, 179, 89, 181, 86, 184, 82, 185, 80, 188, 77, 191, 76, 193, 72, 196, 72, 200,
    71, 204, 70, 207, 69, 210, 69, 214, 68, 217, 67, 220, 66, 226, 65, 229, 62, 224, 61, 222, 60, 218, 61, 214,
    61, 212, 59, 209, 56, 208, 53, 207, 49, 208, 47, 207, 44, 209, 41, 210, 38, 212, 36, 214, 35, 219, 34, 222,
    35, 225, 38, 226, 41, 227, 43, 230, 46, 234, 47, 239, 47, 245, 50, 245, 53, 247, 59, 247, 63, 248, 65, 244,
    68, 239, 70, 235, 71, 229, 73, 223, 74, 218, 75, 214, 77, 210, 77, 207, 78, 204, 79, 202, 79, 198, 81, 194,
    84, 194, 86, 191, 90, 189, 94, 189, 98, 191, 101, 192, 103, 195, 104, 198, 102, 200, 101, 205, 99, 210, 99,
    214, 97, 219, 99, 221, 102, 223, 104, 223, 106, 222, 110, 222, 113, 220, 118, 220, 122, 219, 126, 218, 130,
    217, 133, 217, 136, 218, 139, 221, 137, 225, 136, 227, 134, 229, 132, 229, 129, 231, 124, 234, 121, 237, 117,
    240, 114, 242, 111, 246, 108, 250, 106, 255, 105, 258, 108, 258, 111, 260, 112, 262, 113, 264, 111, 269, 107, 274,
    103, 277, 100, 283, 96, 287, 93, 293, 90, 302, 86, 312, 86, 316, 93, 310, 106, 301, 123, 290, 135, 283,
    167, 267, 193, 256, 226, 248, 256, 244, 277, 246, 279, 246, 281, 245, 279, 243, 274, 234, 268, 224, 258, 217,
    250, 210, 253, 205, 266, 190, 268, 184, 265, 179, 261, 179, 257, 179, 254, 180, 246, 182, 241, 184, 235, 185, 231,
    172]

#launchcodes window wont allow me to resize it so this is to change the coordinates
sherlock_coordinates = [x - 150 for x in sherlock_coordinates]

#this has the list pass through and turn into tuple. which is the (x,y) coordintes
new_list = [tuple(sherlock_coordinates[i:i + 2]) for i in range(0, len(sherlock_coordinates), 2)]

#draw function only occurs if the condition is met of Dr watson or Inspector Lestrade coming to see Sherlock.
#otherwise sherlock will reply with "Go away!" and hide away in his home.
#The drawing represents Sherlock presenting himself to Watson and Lestrade
def draw(x):
    mike.goto(x)


def sherlock(guests):
    for guest in guests:
        if guest == ("Dr Watson") or guest == ("Inspector Lestrade"):
            for x, y in new_list:
                draw((x, -y)) #the drawing continued to come out upside down, so change y coordinates to negative to make the drawing come out correct
            mike.end_fill()
            wn.bgcolor('#555')

            return ("Enter")
        else:
            return ("Go Away! (sound of violin music...)")


def main():
    press = ["a reporter from the Times", "a reporter from the Observer"]
    time.sleep(1)
    family_etc = ["Mycroft Holmes", "Mrs. Hudson"]
    enemies = ["Professor Moriarty", "Charles Augustus Milverton", "John Woodley"]
    potential_love_interest = ["Irene Adler"]
    friends = ["Inspector Lestrade", "Dr. Watson"]
    print(sherlock(press))
    print(sherlock(family_etc))
    print(sherlock(enemies))
    print(sherlock(potential_love_interest))
    print(sherlock(friends))


if __name__ == "__main__":
    main()
