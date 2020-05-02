# Pizza Project

## Installation and running
Install all files and run **main.py** to open the application.\
this application has several pages such as **_login page_**,      **_registration_**, **_admin page_**,  **_order_**, **_add extension_** and the **_confirmation page_**.


## Login page
First page of this application is **login page**. If you already have registered user:
1. Enter username and password (be careful about Uppercases)
2. Click the **LOGIN** button to switch to *order page*

If you don't have any user yet , click the **REGISTER** button to switch to **_registration_** page

> ADMIN:\
> To open the configuration mode you should login as admin. So you need do the following steps:
>1. Enter **"admin"** as *username* and *password* 
>2. Click the **LOGIN** button to switch to *admin page*
## Registration
There you can enter the *username* and *password* .
> WARNING:
> 1. Be careful, you can not use the username which is already used. 
> 2. Username with uppercases and lowercases are different
> 3. Username admin is already used for administrator so try to avoid it!

After you entered both *username* and *password* click **REGISTER** button to create a new account. 

There will be *notification* at the bottom of this page to inform whether your registration is successful or not.

After successful registration or if you want to go back to the **_login page_** click the **Go Back** button. In any case you will switch back to the **_login page_**.

## Admin page
### Creating new pizza
There you can add new pizza just by filling blanks with *"Pizza name"* ,*Status* and *Price*. Then you should click **Create new pizza** button to confirm your addition 
>WARNING:\
>You *can not* add the pizza which you have already added or is default in this app.

After confirmation of your new pizza there will be notification at the bottom of this page whether your addition is successful or not.

### Get information
There you can get **purchase info (cart)** and **password** of a any user.\
To get this information you should follow simple steps:
1. Enter the *username* whom information you want to get
2. Click **GET INFO** button to get information
>If there is no such username in database ,there will be no output

When you finished with configure mode click the **LOG OUT** button. You will switch back to the **_login page_**.

## Order page
There you can choose pizza form the list of existing pizzas by clicking on the name of the pizza. After your clicking on the pizza name the page will be switched to **_add extension page_**.

At the upper part there will be notification about *new pizza* if **ADMIN** added it.
>### Purchase info
>Just by clicking **PURCHASE INFO** button you will get *information (your purchase, price, date/time)* about all of your purchases on this user which you are logged in.

If you want to change the user just click the **LOG OUT** button. You will switch back to the **_login page_**.


## Add extension page
There you can add ingredients to your selected pizza.\
There are 3 default ingredients: cheese, beef, tomato.Each ingredient has its own **buttons** to **_ADD_** or **_REMOVE_** it from your pizza. At the bottom of this page there is an *text information* about your pizza and ingredients in it just to inform you.
>WARNING!\
>You can not remove default ingredients from pizza, it is possible if you added one of ingredients before .

### Order button
To order your purchase click on **Order** button at the right-bottom corner. The page will be switched to the **_confirmation page_**.

### Go Back button
 If you want change anything(pizza, user) you should click on the **Go Back** button to switch to the **_order page_** and then *log out* or *choose another pizza*. 

## Confirmation page
There you can *add new pizza to your purchase list*, *remove last pizza* or *confirm your purchase*.\
There will be your order list and price of it.
### One More Pizza 
By clicking **One More Pizza** you will be switched again to the **_order page_** where you can do the same operations listed before  with *another pizza* and *ingredients*. You can do this operation till you **confirm** it.
### Remove last PIZZA
If you are not satisfied with last pizza you can remove it just by clicking **Remove last PIZZA** or clicking **Go Back** to switch to the **_add extension page_** to *edit your extension* or click **Go Back** again to *change pizza itself*

### Confirm 
To confirm your order just click on the **Confirm** button at the right-top corner.
You will be automatically switched to the **_order page_** and your purchase will be added to *purchase info (cart)*.
