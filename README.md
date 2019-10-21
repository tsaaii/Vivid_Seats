# Vivid_Seats
### *Take home assessment for vivid seats*

- [x] Capturing some important metrics for a data model
- [x] Designing a realational database model
- [x] Writing an API with a database.


#### Defining metrics which are important to capture:
  1. __For seller metrics__: These are the metrics which we are going to capture from a seller who is listing tickets for sale on our platform.
        * __Seller ID__ - This will be a primary key which will help us to identify the seller by name and other details. We can use this for Analytics by listing the sellers from a specific region or can create a list ordered by sales.
        * __Event Category__ - This can be used to list the different type of events like Music, Sports, Arts and Drama, Adults only etc..We can have these Categories listed on the website and a user can look for different events in a category thus using platform more.
        * __Event ID__- This will be used to differentiate the event specific metrics and we can use this as a primiary key for the exclusive events table.
        * __Posting Date__- This is for us to see how sellers are using the platform and supplying this knowledge to our sales team would bring us more business or we can use patterns from a previous year and prepare ourselves for the next year. For example NBA, NHL are season specific and need high resources to satisfy the market demand.
        * __Posting Time__- This can also be used for the same purpose listed above.
        *  __Number of Tickets__- A seller may not necessarily sell on our platform only. There may be other options. We can use this data to offer a competitive package for seller so that they might list more tickets in the future.
        * __Price__- This is a metirc which can be used internally by our business analysts to observe the most valuable partners. We can also use this to have a filter by price feature for our customers to show them a diversified set of options to choose from.
        * __Number of Events__-We can use this to define the most valuable partner and possibly can attract some more partners for an increase in revenue.
        * __Number of Venues__- The best example in this case is NBA, NHL. These can take place in multiple countries and we can use them to improve our advertizing or marketing in other countries. We can also use this for our customer filter to show them some options around.
        * __Types of Tickets__- A sports arena usually will have a range of seats with respective prices. We can possibly pitch our prospective seller to have all types of tickets or we can also use this internally to get an estimate of how we can improve our platform. For example if NBA lists only High end tickets with us, we can probably picth them on better marketing platform which are usually targeted thus improving our conversions.

2. ____For Indirect traffic which we are capturing with a different website:____
    * ____Traffic source____ - This is a metric which would be used to estimate the traffic from different third party websites which are using our gateway to sell tickets. We can understand our audience and can possibly implement some changes to convert them to direct traffic or reach out to more third party sellers for wider business.
    * ____Visitor ID____ - We can assign a visitor ID to track the behaviour of a user who came from an indirect source.
    * ____Visitor Number____ - We can use this to estimate the total number of visitors from a specific indirect source. We can use this knowledge to reach out to more sellers who can draw visitors.
    * ____Visit Number____ - We can also get an estimation on how many times a specific user is coming from a different website.
    * ____Bounce Rate____ - We can calculate the number of users who came from a specific website but didn't buy anything. We can involve better partners based on this metric.
    * ____Visit Date____ - This can be used for general business intelligence like how many users came from a specific website on a specific date.
    * ____Visitor Device____ - We can see how a user is accessing our platform and make some UI/UX research to get more customers.
    * ____GeoNetwork____ - This is a metric on most of the web analytics platforms. This has a bunch of tags which can help us understand the customer better.
    * ____User grouping____ - We can group our customers based on age or gender or taste and target those specific indirect websites to use our platform to sell tickets indirectly.
    * ____Social Engagement____ - This is a generic metric which defines more about a users taste and we can replicate it on similar platforms to draw more customers. Example Facebook vs Instagram.
3. __For Direct traffic from our website__:
    * ____Visitor ID____ - Similar thing as above. We can also use this to see how users are buying tickets with respect to time.
    * ____Visit Number____ - Similar thing as above but this would be exclusive for our website.
    * ____Visit Date____ - Same as above for our website.
    * ____Visit Start Time____ - We can see how eager customers are for a specific event and can gear up our marketing plans accordingly.
    * ____Traffic Source____ - Some may do organic search knowing our brand name, some may find it by coincidence. This can help us do our SEO with better tags so that we will come top on similar searches.
    * ____Visitor Device____ - Same as above. This can help us do some UI/UX research.
    * ____GeoNetwork____ - Same as above.
    * ____Bounce Rate____ - Same as above.
    * ____User Grouping____ - Same as above.
    * ____Social Engagement____ - Same as above.
4. __For Customers who bought something from us__:
    * ____Event ID____ - We can see sales that happened on our platform for an event. We can use this Business intelligence to reach out similar event sellers to use our platform more.
    * ____First Signup____ - Some users may just signup and buy tickets. We can use this use this to see how many are using platform for the very first time and buying tickets. This can be useful in Fraud prevention too.
    * ____User Since____ - This can help us understand how long a specific user is using our platform.
    * ____Visitor ID____ - Similar as above.
    * ____Sale Time____ - For internal analytics to see how much sales were done at a give point.
    * ____Sale ID____ - This will be unique and a primary key to see other metrics related to a particular event.
    * ____Sale Date____ - For our analytics to see growth by date.
    * ____Number of Tickets____ - Some customers may buy single ticket, some may buy multiple. We can use this knowledge with our selling partners to get us more seats like more couple seats or more family seats etc. 
    * ____Price per unit____ - This can help us understand most valuable customers.
    * ____Address____ - This can be used to see how many customers are from a foreign country and picth them some hotel packages or we can show events specific to a location and buy some more sales.
    * ____Contact Number____ - A very important metric to prevent fraud. We can also use this to communicate with our customers or to send them remainders about the event.
    * ____Payment method____ - This can be paypal vs credit vs debit card types which we can use to give some cash back deals partnering with those providers.
    * ____Promo used____ - We can have this metric to see if a particualr customer used promotion code to buy ticket. Irrespective we can give some deals to attract them to buy tickets.

