# Conways game of life on a toroidal array

Conways game of life (https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) is usually implemented without considering neigbouring cells that would be outside of the arrays range, but another way to do it is by considering the left and right edges of the array to be stitched together, and the top and bottom edges also, yielding a toroidal array and thus all cells get 8 neighbours.

Implement the function get_generation(cells, n) which takes a 2d-array cells an returns generation 'n' of game of life with the initial 'cells' and which considers the array as a toroidal array.

you can use the function print2dArr(list) to print out your array in a more readable format.

Example:
The following pattern would be considered Still life (a pattern which does not change after a generation) on a toroidal array because each live element have exactly 3 neighbours at the toroids stiched edges.


[   1,   0,   0,   1]
[   0,   0,   0,   0]
[   0,   0,   0,   0]
[   1,   0,   0,   1]
