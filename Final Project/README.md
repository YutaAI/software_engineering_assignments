### Installing necessary packages:  
* `pip install fastapi`
* `pip install "uvicorn[standard]"`  
* `pip install sqlalchemy`  
* `pip install pymysql`
* `pip install pytest`
* `pip install pytest-mock`
* `pip install httpx`
* `pip install cryptography`
### Run the server:
`uvicorn api.main:app --reload`
### Test API by built-in docs:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Implemented API areas
* Orders: customer order capture, order status, tracking number, payment method, and delivery details
* Order details: sandwich line items and quantities per order
* Sandwiches: menu items with price, calories, and food category
* Recipes: sandwich-to-resource ingredient mapping
* Resources: inventory items and quantities

### Available routes
* `/orders`
* `/orderdetails`
* `/sandwiches`
* `/recipes`
* `/resources`