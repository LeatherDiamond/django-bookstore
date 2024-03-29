# Navigation
 
* ***[Project description](#project-description)***
   * ***[Note](#note)***
* ***[Software version](#software-version)***
* ***[Detailed functionality description](#detailed-functionality-description):***
   * ***[Shop roles and users](#1-shop-roles-and-users)***
   * ***[User profiles](#2-user-profiles)***
   * ***[Product card](#3-product-card)***
   * ***[Scheme of the ordering process](#4-scheme-of-the-ordering-process)***
   * ***[Cart](#5-cart)***
   * ***[Product search](#6-product-search)***
   * ***[Ordering](#7-ordering)***
   * ***[Administrative portal](#8-administrative-portal)***
   * ***[Built-in administrative portal](#9-built-in-administrative-portal)***
   * ***[Home page](#10-home-page)***
   * ***[Directories](#11-directories)***
* ***[How to start?](#how-to-start)***
   * ***[Notes](#notes)***
* ***[Creating superuser](#creating-superuser)***
* ***[Database administration](#database-administration)***
* ***[Code formatting and Quality checking tools](#code-formatting-and-quality-checking-tools)***
* ***[Running tests inside the container](#running-tests-inside-the-container)***
* ***[Running tests locally](#running-tests-locally)***
* ***[Why should you try it?](#why-should-you-try-it)***
* ***[License](#license)***


# Project description

Web applicaton of a bookstore intended for the sale of paper books online. 
The bookstore is a showcase of available products (catalogue) and provides all necessary information and tools for choosing and ordering goods.
The bookstore enables shop personnel to receive and process orders and provides the possibility for the customers to follow the status of their orders.

> ###### NOTE:
> * *You can familiarize with deployed version of the project by the following [link](https://alexanderdovguchits.pythonanywhere.com/).*

# Software version:
- Python: 3.11.3, 
- Pip: 23.3.1,
- Poetry: 1.7.1,
- Django: 4.1.1, 

# Detailed functionality description

## 1. Shop roles and users

   * ***1.1*** *User groups:*
      * ***1.1.1*** *Customers - buyers;*
      * ***1.1.2*** *Managers - shop employees;*
      * ***1.1.3*** *"Admin" - as a user with access to any part of the system. Has access to built-in administrative portal;*
      * ***1.1.4*** *Unregistered users;*

   * ***1.2*** *Buyer:*
      * ***1.2.1*** *Registered user in the system;*
      * ***1.2.2*** *Belongs to the Customers group;*
      * ***1.2.3*** *Main user of the services provided by the Shop:*
           * ***1.2.3.1*** *Selects the Goods from the available catalogue using:*
               * ***1.2.3.1.1*** *Search;*
               * ***1.2.3.1.2*** *Offers on the home page (novelties, most popular etc.);*
               * ***1.2.3.1.3*** *Viewing the catalogue;*
           * ***1.2.3.2*** *Adding goods to cart;*
           * ***1.2.3.3*** *Making orders;*
           * ***1.2.3.4*** *Monitors the status of the order;*
           * ***1.2.3.5*** *Cancels the order;*
       * ***1.2.4*** *Edits the details of own profile;*
       * ***1.2.5*** *Comments on the products;*
       * ***1.2.6*** *Creates comments on own orders;*

   * ***1.3*** *Shop employee:*
       * ***1.3.1*** *Registered user;*
       * ***1.3.2*** *Belongs to the group of Managers;*
       * ***1.3.3*** *Processes the incoming orders on the special administrative portal;*
       * ***1.3.4*** *Receives notifications by email about new orders;*
       * ***1.3.5*** *Reviews the order;*
       * ***1.3.6*** *Changes the status of the order;*
       * ***1.3.7*** *Makes comments on shop goods and orders;*
       * ***1.3.8*** *Views and edit the product catalogue;*
        
   * ***1.4*** *Unregistered user:*
       * ***1.4.1*** *Unregistered user;*
       * ***1.4.2*** *Not belonging to any group;*
       * ***1.4.3*** *Performs actions specified in paragraphs 1.2.3.1. 1.2.3.1, 1.2.3.2, 1.2.3.3;*


## 2. User profiles

   * ***2.1*** *Customer profile:*
       * ***2.1.1*** *Consists of fields:*
           * ***2.1.1.1*** *Login;*
           * ***2.1.1.2*** *Password;*
           * ***2.1.1.3*** *E-mail;*
           * ***2.1.1.4*** *Name;*
           * ***2.1.1.5*** *Last name;*
           * ***2.1.1.6*** *Phone number ;*
           * ***2.1.1.7*** *Group - not available for editing.  Affiliation is assigned automatically;*
           * ***2.1.1.8*** *Home address:*
               * ***2.1.1.8.1*** *Country;*
               * ***2.1.1.8.2*** *City;*
               * ***2.1.1.8.3*** *Index;*
               * ***2.1.1.8.4*** *Address1;*
               * ***2.1.1.8.5*** *Address2;*
           * ***2.1.1.9*** *Additional information;*
       * ***2.1.2*** *Information displayed in the profile:*
           * ***2.1.2.1*** *All data from paragraph 2.1.1;*
           * ***2.1.2.2*** *Order history;*
       * ***2.1.3*** *Profile features for the owner:*
           * ***2.1.3.1*** *Edit profile data (except 2.1.1.8);*
           * ***2.1.3.2*** *Modify own order data;*
           * ***2.1.3.3*** *Cancel/Restore own orders;*
            
   * ***2.2*** *Employee and administrator profile:*
       * ***2.2.1*** *Consists of fields:*
           * ***2.2.1.1*** *Contains the same fields as the Customer profile;*
       * ***2.2.2*** *Information displayed in profile:*
           * ***2.2.2.1*** *All data from paragraph 2.2.1;*


## 3. Product card

   * ***3.1*** *Fields:*
       * ***3.1.1*** *Book title;*
       * ***3.1.2*** *Photo;*
       * ***3.1.3*** *Price (BYN);*
       * ***3.1.4*** *Author of the book (may contain several authors) - directory;*
       * ***3.1.5*** *Series - directory;*
       * ***3.1.6*** *Genre (one or several genres) - directory;*
       * ***3.1.7*** *Year of publication;*
       * ***3.1.8*** *Pages;*
       * ***3.1.9*** *Binding;*
       * ***3.1.10*** *Format;*
       * ***3.1.11*** *ISBN;*
       * ***3.1.12*** *Weight (grams);*
       * ***3.1.13*** *Age restriction;*
       * ***3.1.14*** *Publisher - directory;*
       * ***3.1.15*** *Quantity of books available;*
       * ***3.1.16*** *Active (available to order, Yes/No);*
       * ***3.1.17*** *Rating (0 - 10);*
       * ***3.1.18*** *Date of addition to the catalogue;*
       * ***3.1.19*** *Date when the product card was modified last time;*
        
        
## 4. Scheme of the ordering process

![Diagram of the ordering process](https://github.com/LeatherDiamond/ITacademy/blob/d827cf1173d5f6a7e579be41d17365d2dcdb83ef/Diagram%20of%20the%20ordering%20process.svg)


## 5. Cart

   * ***5.1*** *Contains the Buyer's chosen products and their quantities;*
   * ***5.2*** *Shows to the Buyer the list of the chosen products, their quantities and price;*
   * ***5.3*** *Allows the Buyer to edit the goods in the cart: remove goods from the cart, change the quantity of goods;*
   * ***5.4*** *Contains the "Order" button to proceed to the checkout of the chosen products;*
   * ***5.5*** *Cart is implemented as a separate app;*
   * ***5.6*** *The content of the cart stored in the corresponding database table of the application;*
   * ***5.7*** *Cart fields:*
       * ***5.7.1*** *Buyer - registered user or anonymous user;*
       * ***5.7.2*** *Goods - Goods in cart entity;*
       * ***5.7.3*** *Date of creation;*
       * ***5.7.4*** *Date of last editing;*
   * ***5.8*** *Goods in cart entity:*
       * ***5.8.1*** *Stored in a separate table in the application's database;*
       * ***5.8.2*** *Fields of Goods in cart:*
           * ***5.8.2.1*** *Cart - indicates the cart to which this order item belongs;*
           * ***5.8.2.2*** *Goods;*
           * ***5.8.2.3*** *Quantity of items;*
           * ***5.8.2.4*** *Date of creation;*
           * ***5.8.2.5*** *Date of last edit;*
           * ***5.8.2.6*** *Cart and Goods fields form a unique key - cart can't have two same products;*


## 6. Product Search


## 7. Ordering

   * ***7.1*** *Ordering process;*
   * ***7.2*** *Entity fields Order;*


## 8. Administrative portal

   * ***8.1*** *Accessible only to employees and administrators;*
   * ***8.2*** *Provides the ability to edit existing directories of the system;*
   * ***8.3*** *Provides the possibility of editing product cards;*
   * ***8.4*** *Provides possibility of editing/processing orders;*


## 9. Built-in administrative portal

   * ***9.1*** *Accessible at /s-admin/;*
   * ***9.2*** *Used by Administrator as a low-level interface to all web-site data;*
   * ***9.3*** *Other users do not have access to the built-in administrative portal;*


## 10. Home page

   * ***10.1*** *Contains a navigation bar:*
       * ***10.1.1*** *For the Buyer:*
           * ***10.1.1.1*** *Provides navigation through the website sections (Goods, Groups of products, Profile, Cart, Login/Logout section (login with Google is available), Registration section, Some directories);*
           * ***10.1.1.2*** *Products search;*
           * ***10.1.1.3*** *Displayes USD/BYN exchange rates;*
       * ***10.1.2*** *For Employee:*
           * ***10.1.2.1*** *Provides navigation through website sections (Goods, Groups of products, Profile, Administrative portal);*
           * ***10.1.2.2*** *Products search;*
       * ***10.2*** *Products showcase:*
           * ***10.2.1*** *Web-site proposals (new arrivals, bestsellers etc.);*


## 11. Directories

   * ***11.1*** *Elements of the directories are used as standard values to be substituted into the forms fields;*
   * ***11.2*** *Implemented a separate module for directories;*
   * ***11.3*** *Elements of the directories can be edited by users having the "Employee" role in the administrative portal ([paragraph 8](#8-administrative-portal));*
   * ***11.4*** *Each directory stores in a separate table in the database of directories module;*


# How to start?

**1. Install [Docker](https://docs.docker.com/engine/install/) on your local machine, if it wasn't done yet, and launch it;**

**2. Clone current repository on your local machine:**
```
git clone https://github.com/LeatherDiamond/Django_bookstore.git
```
***3. Navigate to the root directory of the project;***

***4. Configure `.env` file by assigning values to the variables defined in `.env.sample`;***

***5. In the project directory, run `docker-compose up --build` to start the services;***

***After completing all the steps, the project will be launched and available at `http://localhost:8000/`.***

> ###### **NOTES:**
> The values for *"SOCIAL_AUTH_GOOGLE_OAUTH2_KEY"*, *"SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET" and "COURIER_AUTH_TOKEN"* will be available only after completting a few steps in the Google and Courier API consoles.
> For more details, please refer to [GOOGLE](https://developers.google.com/identity/protocols/oauth2?hl=en) and [COURIER](https://www.courier.com/docs/) documentation.
> 
> *The project contains a database dump ---> ***src/proj/datadump.json***. This dump is just an example and contains 10 products as a demonstration of the functionality of the web application.*
> 
> *You can import the dump by processing the following command inside the ***container*** or just in the ***root*** directory of the project if you are going to launch it locally:*
> ```
> python src/manage.py loaddata datadump.json
> ```


# Creating superuser

If you already followed the **[How to start](#how-to-start)** section steps, superuser will be automatically created in webapp container with the credentials provided in `.env` variables `DJANGO_SUPERUSER_USERNAME` and `DJANGO_SUPERUSER_PASSWORD`.

This superuser can be used to get access to the django admin panel while the project is launched in containers.
If you want to create superuser locally you can also see how to do it in  **[Running tests](#running-tests-locally)** section below.


# Database administration

To administer the `PostgreSQL` database, you can use pgAdmin, which runs in a separate container. To access pgAdmin, follow these steps:

1. Open a browser and go to `http://localhost:5050/`;
2. Enter the login and password from your `.env` file to log in to pgAdmin;
3. Create a new connection to the necessary database;
4. Connect to the database and perform the necessary operations;


# Code formatting and Quality checking tools

1. Run `poetry shell` to activate environment if it's not active yet;
2. Run `black . --check` to check if the code needs to be reformatted;
3. Run `black .` to reformat the code;
4. Run `flake8` to identify potential issues, such as syntax errors, code style violations, and other coding inconsistencies during the development process;


# Running tests inside the container:
1. Make sure that points 1-4 from ***[How to start](#how-to-start)*** section are already completed;
2. Build images and run containers:
```
docker compose up --build
```
3. As soon as all containers started, enter the webapp container:
```
docker exec -it bookstore.webapp bash
```
4. After you entered the webapp container, launch tests:
```
pytest
``` 

# Running tests locally:
1. Make sure that repository is already cloned on your computer, docker is launched, images already built and are ready for use and containers are not started yet;
2. Navigate to the root derictory of the project;
3. Configure `.env` file by assigning values to the variables defined in `.env.sample`;
 > ###### **NOTE:**
 > Set in **PRIMARY_DATABASE_URL** configuration for your local database (for example PRIMARY_DATABASE_URL=postgres://admin:admin@localhost:5432/testbase)
4. Activate virtual environment:
```
poetry shell
```
5. Install all dependencies:
```
poetry install
```
6. Apply all migrations:
```
python src/manage.py migrate
```
7. Create default superuser in your database with credentials provided in your `.env` file:
```
python src/create_default_db_data.py
```
8. Launch the server:
```
python src/manage.py runserver
```
9. Start tests with the following command in console:
```
pytest
```
> ###### **NOTE:**
> If you will try to put the command in another console, make sure that virtual environment is active - *point 4* of the current instruction.


# Why should you try it?

***It's a powerful application that allows you in a few easy steps to set up a full-scale online shop that has an intuitive and concise interface and will satisfy most customers and owners needs cause it's easy-to-use and has the rich functionality that an online shop so desperately needs.***


# License

***This project is licensed under the MIT License - see the [LICENSE](https://github.com/LeatherDiamond/Django_bookstore/blob/master/LICENCE) file for details.***
