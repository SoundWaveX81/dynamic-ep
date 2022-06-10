####################
Dynamic Api approach
####################

This is the approach to make a dynamic endpoint to get prices of different product types.

I've mock a couple of products price logic located in dynamicapi/services/ dir, each one has its own serializer to simulate diferent params (pass as querystrings due to this endpoints is uses GET method) and validate those params with its proper serializer file.

*************************************************
example of success request/response (status: 200)
*************************************************

.. code:: bash

    curl --location --request GET 'http://localhost:8000/dynamic-api/product_two/?char_2=sometext&int_2=1' \
    --data-raw ''


.. code:: json

    {
        "detail": "ok"
    }


**************************************************************
example of missing/wrong params request/response (status: 400)
**************************************************************

.. code:: bash

    curl --location --request GET 'http://localhost:8000/dynamic-api/product_two/?char_1=sometext&int_2=1' \
    --data-raw ''


.. code:: json

    {
        "char_2": [
            "This field is required."
        ]
    }


*********************************************
example of unknown product type (status: 404)
*********************************************

.. code:: bash

    curl --location --request GET 'http://localhost:8000/dynamic-api/product_three/?char_1=sometext&int_2=1' \
    --data-raw ''


.. code:: json
    {
        "msg": "product_three no pricing calculation for this product type"
    }










