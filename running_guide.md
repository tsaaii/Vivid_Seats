### Running guide 
#### This is to demonstrate how API works with a detailed running instructions.

1. We will first create a database as discussed earlier. please run the following script

>python create_db.py

2. This should create a data.db database in your working directory

3. Lets define some data and load the data what we have in the CSV file in to the database. For this please run the following script

>python data_ingest.py

4. Lets see how the data looks like in the sqllite client on desktop which you downloaded from the README.md file. This is in your terminal

>sqlite3>/<your pwd dir here>/Desktop/vivid_seats/data.db

5. We created a table called vivid_data from our data ingestion step and the schema looks like below.
![Table and schema on our sqlite client](https://github.com/tsaaii/Vivid_Seats/blob/master/Img/pic1.png)

6. We have our database and now we will start the API part using flask. Run the followiing command

>python api_v1.py

7. This should open in local browser on port 5000. We can use postman to check the functioning. 

8. *The GET part of our API gives us the total number of tickets available for a specific event. For this you have to specify the tag event_number which is our gateway route and give the event number.*

![GET part to get ticket numbers](https://github.com/tsaaii/Vivid_Seats/blob/master/Img/GET.png)

9. *Our Second GET call will give us the best ticket. I defined the best ticket as the one with the cheapest price as I have no info about the section or row given in the dataset. The best 10 seats will be displayed sorted by the price as shown. You have to route to get_best and give the event id to see the best ticket.*
![GET part to get the best tickets given an event ID](https://github.com/tsaaii/Vivid_Seats/blob/master/Img/GET2.png)

If you give a wrong event Id it should show Null and it does show that.

![What if you give a wrong event ID](https://github.com/tsaaii/Vivid_Seats/blob/master/Img/GET3.png)

10. Lets give a chance for our partners to POST something to our database. Ofcourse this would be done with authentication. But for demo purpose lets see one. We don't have an event with ID 999 as shown by our sqlite terminal.

![No Event with ID 999 as seen on terminal](https://github.com/tsaaii/Vivid_Seats/blob/master/Img/no999.png)

11. Lets POST using the event details as shown in the body to our gateway called /add_new

![POST about the new tickets from seller](https://github.com/tsaaii/Vivid_Seats/blob/master/Img/post.png)

12. Lets confirm our POSTed new ticket using GET request which we did in step 8.

![GET shows existence of our event](https://github.com/tsaaii/Vivid_Seats/blob/master/Img/post1.png)

13. Lets design the PUT part. A PUT request is generally used to update a record.Our PUT request takes Event_Id, Quantity, Section, Availability as parameters and can change the quantity or availability. Lets add some tickets to an event and also delete some tickets to the request and see its performance.

Adding some tickets as a seller

![PUT updated the tickets to No for Event_Id 999 where we earlier had 2 tickets.](https://github.com/tsaaii/Vivid_Seats/blob/master/Img/PUTS1.png)
Revoking some tickets as a seller

![Verifying the total number of tickets for Event 999 with GET, it should be Null](https://github.com/tsaaii/Vivid_Seats/blob/master/Img/PUTSU.png)
Test case to give an erroneous input

![Lets give a weird availability apart from Yes or No](https://github.com/tsaaii/Vivid_Seats/blob/master/Img/PUTF.png)

Adding tickets to event Id 162 with our PUT
![Adding tickets to event 162. We are adding 2 tickets from the body.](https://github.com/tsaaii/Vivid_Seats/blob/master/Img/PUTS2.png)

Confirm the added tickets with GET
![Now our Get confirms incremented quantity of tickets from above request](https://github.com/tsaaii/Vivid_Seats/blob/master/Img/PUTS2G.png)



