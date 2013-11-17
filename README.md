##Problem Statement :
Given many pairs of coordinates, find the pairs that are collinear with each other.

##Logic :
* We have coordinates: p1, p2, p3.....{ Eg,  [ p1=(x1,y1) ]  }
Start with p1 and find slope of p1 with all remaining other points.Thus we get a list of slopes.
In this list, pairs having same slope are collinear with point p1.

* Same procedure is repeated to find points collinear with any pair p(i)


##TO-DO :
* The coding design is very bad, everything is "position" dependent in the list that contains the pairs of coordinates.
So change it to OOP.

