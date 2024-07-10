# Write your solution here
def spruce(layers):
    row = "*"
    i=layers
    print("a spruce!")
    while layers > 0:
        print(" " * (layers-1) + row)
        row+="**"
        layers-=1
    print(" "*(i-1) + "*" )
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)