# Q11. Something fishy there -
# Find output of following:
def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
        print(l)
f(2)
f(3,[3,2,1])
f(3)



# f(2): This calls the function f with x=2 and the default value of l, which is an empty list []. Inside the function, a loop runs from 0 to 1 (range 2), and for each iteration, the square of the current index is appended to the list l. So, the list l becomes [0, 1], and it is printed.

# f(3, [3, 2, 1]): This calls the function f with x=3 and a provided list [3, 2, 1] as the argument for l. Again, the loop runs from 0 to 2 (range 3), and for each iteration, the square of the current index is appended to the list l. Since the provided list is used, the initial values are not present in l. So, the list l becomes [3, 2, 1, 0, 1, 4], and it is printed.

# f(3): This calls the function f with x=3 and no provided argument for l. Since the default value of l is a mutable object (an empty list), it retains its state from the previous calls. So, the loop runs from 0 to 2 (range 3), and for each iteration, the square of the current index is appended to the existing list l. Hence, the list l becomes [0, 1, 0, 1, 4], and it is printed.