# REST API for Inventory Management System

## Steps for running the application

1.  Run the app.py file .
2.  Use '/register' for Registering yourself into the system by providing.
    {
        "username" : <username>,
        "password" : <password>
    }
3. Use '/auth' for logging in. You will get an access token for using in the methods that are jwt_required.
4. After logging in add the items to the database by using POST '/item/<name>' and also provide,
    {
        "price" :<price>
    }
    This will create an item with no orders yet.

5. Similarly use GET '/item/<name>' for getting the particular item details, DELETE '/item/<name>' for deleting    the particular item and PUT 'item/<name>' for modifying the price(Provide the modified value for price).

For all the above requests use Authorization as header and set the value as 'JWT <access_token>'

6. For adding the data of the suppliers of various items in our store, use POST '/supplier/<name>' and also provide,
    {
        "mobile_no" : <10_digit_number>
    }
    Similarly for all other operations as described in step 5 use '/supplier/<name>

7. For purchasing the items from a added supplier use '/purchase/<id>' and also provide,
    {
        "supplier_id":<iid_of_supplier>,
        "item_id":<item_id>,
        "received": <boolean_value_for_item_recieved>,
        "date": <date> (In the form: "2012-01-01T23:30:00+02:00")
    }
    You will recieve back the all the detalils of items and supplier along with the purchase information.
    Similarly for all the other operations described in step 5 use '/purchase/<id>'

8. For Placing the order of the items use '/order/<id>' and also provide,
    {
        "item_id": <item_id_to_order>,
        "date": <date> (In the form: "2012-01-01T23:30:00+02:00")
    }
    After Placing the order the items table will have it appended in its order list.
    Similarly for all the other operations described in step 5 use '/order/<id>'

9. For viewing all the records of items, suppliers, purchaese and orders table use '/items', '/suppliers', '/purchases' and '/orders' respectively.


