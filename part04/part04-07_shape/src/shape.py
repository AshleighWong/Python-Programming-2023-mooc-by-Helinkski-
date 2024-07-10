# Copy here code of line function from previous exercise and use it in your solution
def line(integer, string):
    if string == "":
        string = "*"
    else:
        string = string[0]
    print(string*integer)
    
def shape(t_size, t_shape, r_size, r_shape):
    i=1
    while i <= t_size:
        line(i, t_shape)
        i+=1
    i=0
    while i < r_size:
        line(t_size, r_shape)
        i+=1
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")