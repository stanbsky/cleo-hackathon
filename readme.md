# Project

## Idea

Every money/budget tracking company right now, tracks, where you spend your money and using that data, helps you to make a budget and set some limitations so you always stay within a limit and do not overspend which is a good thing but it does not help you spend your money smartly. They might give some offers, but that's pretty much it, and by that, you are restricted to use some of their provided portals, but what if the company helps you to spend your money smartly? what if they help you to find the best deals on the market, gives you various information about the product and hopefully even sort those products using cost, or even ratings. If they stick with this ideology then the users will be no longer restricted to the limited atmosphere and can compare various products online with just a simple text, which was also the core principle of Cleo, help people do complicated things with just a text message.

## Implementation

We started by checking out what the URLs are for the different products, the first product was finding how to search for a product without actually clicking the search boss. The URL looks similar to: `https://morrisons.co.uk/?product=product%20name&sort=ASC` so we could replace \`product%20name\` with the URL encoded version of our product name, We used urllib for the URL encoding instead of implementing in case we forgot to account for edge cases, and we used requests to fetch the data.
The next problem was parsing the data, we have had plenty of experience before with the module \`BeautifulSoup\` so we threw in the response text from our request above and got to work. In conjunction with chrome dev tools to get the classes and locations of the values, we were requiring it made implementation slightly easier. Each of the parsers is similar to others making it somewhat intuitive for other developers to come in and replicate what we have done for other shopping sites. This was done in the name of open source love 🖤.
The final problem was putting all the data together, for this we used dictionaries as they are easy to manipulate and the retrieving of values is O(1) time! We used built python functions to sort the data and get it in the format we needed.
For the frontend, We used plain CSS/HTML/Javascript combined with jinja2. Jinja2 is a templating language that was made for Python. We used XMLHttpRequest to interact with our backend that we wrote in FastAPI (a fast new-ish python framework). Then parse the JSON response the backend passed us and used it for replying with the Bot.

## Requirements

Please refer to [cleo2/requirements.txt](https://github.com/stanbsky/cleo-hackathon/blob/master/cleo2/requirements.txt)

## Conclusion

Given this was started about halfway through the hackathon due to the struggles mentioned about the original idea [below](https://github.com/stanbsky/cleo-hackathon#what-went-wrong) we think it went very well. We have given our best and the speed was incredible as well, it is extremely beneficial for anyone that does not only grocery shopping (most people) but also any type of online shopping and is a great little tool. Given more time we would have cleaned up the frontend as there are some visual issues with it (not major) and add more places to scrape from.

## Screenshot(s)

![The Final Product](https://i.snipboard.io/NfKU6e.jpg)

# Directory

```
├───backend
├───cleo2
├───custom_data
├───dataset
├───frontend
├───plaid_data
├───screenshots
└───ui
```

-   cleo2 - this is where our submitted product is, the idea we pivoted to
-   backend - the original backend folder of the original idea
-   frontend - the original frontend folder of the original idea
-   dataset - smartly generated dataset using statistical data to make it realistic using nodeJs
-   custom_data - even more custom data generated via numpy and pandas
-   plaid_data - Plaid API data, scraping scripts, jupyter notebooks analysing it
-   ui - initial ui for the prediction model

# Initial Project

## Idea

With the power of machine learning, we can find the trends and casual behaviours shared between some class of certain users in terms of their expenditure, frequency of purchase, type of transaction, etc., which could potentially be used to train the model, and predict if whether the user is spending the money under the mentioned budget cap or not. This idea can be elaborated further by predicting of user's pay off their credit card and show them the visualized data to make them more familiar with their future predicted budget, so they can be more aware of what they should be doing in the present to improve their future, and avoid fines and thus, overall enhance their credit score.

## Implementation

We decided to gather sample user data from the Plaid API used by Cleo, then build data science models to analyse the user spending on several factors:

-   Is the user frequently spending more than they earn by relying on credit cards? `sum(total_spending) >= sum(total_income)`
-   Are their credit card payments keeping up with the interest accumulating on their balance? `sum(cc_payments) >= get_compounded_balance(starting_balance, apr, months=12)`
-   Do they put money into savings that could be applied to pay down high-interest-rate debts?
-   What patterns are present in their interest rate repayments? Are they trending down? Are there seasonal variations to be aware of?

## Data Set and Backups

Since we are working on Cleo's work atmosphere, using the same API's which are currently being used by Cleo would make the most sense, thus Plaid API was used to extract data set of people monthly expenditure, which then was well prepared, sieved and then finally was ready for processing.

> **Note:** Even though we managed to extract the data but in the meantime, we created the scripts which could generate and mock the real-life data of money expenditure done by the average US person, which was well categorized and matched with the statistical data available for average US citizen.

## What went wrong?

It took time to get to grips with the Plaid sandbox API and deal with timeouts/empty responses due to data being generated.
Finally, it turned out the data was not representative of real spending habits, i.e. spending 10x greater than earnings, credit transactions not adding up to liabilities balance, etc.
We began working on generating our sample data addressing the project aims, however, this left us too little time to address our objectives.

## Learning and Conclusion

When looking for third party data on users credit card debt and related data, we found that the data we found using plaid was not very relevant. It generated models which were quite very ineffective to predict the future levels of budget. Even though we had backup mass-produced data, we did not want to jeopardise the whole hackathon and thus we split the team and started exploring different ideas, which would be having the same impact as our original idea, and which led to our core project.

#

### Languages Used

-   Python
-   NodeJs
-   JavaScript
-   HTML/CSS (not actually a programming language)
-   SCSS

### Technologies Used

-   FastAPI
-   Jinja2
-   Selenium
-   BeautifulSoup
-   Jupyter Notebooks
-   Numpy/Pandas
-   Vue.js
-   Faker.js

### Contributors

-   Stan (stanbsky) - Data science
-   Morgan (morgs5656) - Data science
-   Charlie (scxr) - Backend | Data science | Frontend
-   Harsh (harshonyou) - Frontend | Data set
