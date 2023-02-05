#!/usr/bin/env python3.7
# create a an empty list
aws_services = []

# add the objects to the list using the append method
aws_services.append('Lambda')
aws_services.append('Xray')
aws_services.append('SQS')
aws_services.append('EC2')
aws_services.append('DynamoDB')
aws_services.append('Route 53')

#print the list
print (aws_services)

#print the length of the list
print ("The length of the first list is: ", len(aws_services))

# remove 2 services from the list by name
aws_services.remove('EC2')
aws_services.remove('Lambda') 
# remove 2 services from the list by index
del aws_services[4]
del aws_services[1]

#print the new list
print (aws_services)

#print the length of the new list
print ("The length of the updated list is: ", len(aws_services))
