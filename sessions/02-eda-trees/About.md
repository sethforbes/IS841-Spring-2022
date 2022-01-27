# Learning Goals

- Continue Data Wrangling and EDA
- Continue the fundamentals of visual programming and building analytics pipelines
- Tree-based Methods (Regression and Classification)

Slides:  https://docs.google.com/presentation/d/1UWQSU9qvA3vW70hWLeYT4dhkgr5T3qxGmOR5UlKUob8/edit?usp=sharing


## Warmup Exercise

Using the same `Superstore` dataset from last week:

1.  Read the Orders and Returns sheets into RapidMiner (RM)
1.  `Left join` the Returns data __onto__ the Orders dataset.  TIP:  Ensure that you have Process > Synchronize Metadata checked to help with the parameters.
1.  Review the dataset properties via Results > Statistics
1.  Replace the missing values for the Product Base Margin with the average of the valid alues.


## Data Wrangling and EDA

- Aggregations
- Select rows (Examples)
- Select columns (Attributes)
- Rename
- Generate new attributes
- Replace Missing Values
- Data transformations
- Correlations

## Tree-based Methods

![](https://miro.medium.com/max/1430/1*rSQIIAboJftqAv_BReNipg.png)

- Regression and Classification tasks
- Flexible
- No significant considerations for data
- If-this then that type rules to help explain what is going on
- Fast

## Practice Exercise

> Your Sales team is looking to better understand Returned orders

- Use the `superstore.xlsx` dataset (found in `/datasets`)
- Join the Orders data with the Return Status
- Do any necessary data pre-processing (wrangling) steps
- Fit a Tree model to predict the return status for the order

> Do the best you can!  Remember, the search within RapidMiner is pretty good.  Try to deconstruct the problem into smaller piece in order to step through the tasks needed to solve the problem.




