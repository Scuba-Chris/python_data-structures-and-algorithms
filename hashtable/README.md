# Hashtables
We are to create the methods needed to create a hashtable. A hashtable is basically an array keys. Each key can have multiple values that are stored in a linked list. This linked list is often refered to at a bucket.

## Challenge
The challenge for today was to build out methods for working with a hashtable. The methods that are needed are add, get, contains, and a hash function.

## Approach & Efficiency
The approach I took was to create a hashtable class that contains all of the methods. Within that hash class there is a hash function that takes in a key and returns the placememt for the key within the array. The add, get, and contains methods do exactly what they are called. The Big O for time is close to O(1) and for space it is also O(1)

## API
In the init method a bucket is used to contain the linked list of values. A dictionary of all of the keys is also created.
The hash function was create to handle the placement of the key with in the array. The add method handles the traversal of the list to see if there is already a bucket for the key. If not the key is added at that location within the list. The get method treverses the list and goes through each bucket to look for the key value. If the key value excises, it is returned. Contains just loops through the list and the bucket to key and value exists. 