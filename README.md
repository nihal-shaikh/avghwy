# Average of Hwy
1. import the csv module
2. define a function which will calculate the average of the hwy column according to class column. in the .csv file where the filepath is passed to the funtion as an argument
3. Open the file as a csvfile. where csvfile is an object.
4. And store the csv file as a dictionary in a list i.e [{key:value}] which link all the attributes with the corresponding tuples
5. then we store the tuples of 'class' of the vehicles using using set which will provide an unordered set of items which will be unique and by using set comprehension we traverse through the entire class column.
6.initialize an empty list which will store the average of the hwy and to their coressponding class
7. use a for loop which will iterate over all the vehicle classes
8. initialize two counters 
	1. which will add the tuples of the hwy column .
	2. the other one will count the count the no. of tuples that r to be added in a 	   particular class
9. then append the average of hwy according to the class 
10. sort the list in an lambda construct in an ascending order.
11. and display the average of the hwy according to class.
