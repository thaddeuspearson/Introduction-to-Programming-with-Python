# The following code causes an infinite loop (a loop that never stops
# iterating). Why?

counter = 0

while counter < 5:
    print(counter)

# The counter is not incrementing with each loop iteration. This will continue
# infinitely.

