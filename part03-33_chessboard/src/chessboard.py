# Write your solution here
# def chessboard(x):
#     i = 0
#     while i < x:
#         j=0
#         one_beginning = (i%2 == 0)
#         while j < x:
#             if (one_beginning and j%2 == 0) or (not one_beginning and j%2 != 0):
#                 print("1", end = "")
#             else: 
#                 print("0", end = "")
#             j+=1
#         print()
#         i+=1
def chessboard(x):
    i = 0
    while i < x:
        if i%2==0:
            row = ("10"*x)
        else:
            row = ("01"*x)
        print(row[0:x])
        i+=1

# Testing the function
if __name__ == "__main__":
    chessboard(3)
