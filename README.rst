Example opentelemetry sklearn implementation
============================================

Setup the environment using asdf and poetry with the command ``make setup``.

Run jaeger using ``make jaeger``. This will run jaeger at http://localhost:16686

Run the example server using ``make example``. This will train a machine learning model and host a predict endpoint at http://localhost:8000/predict

Send a request to the server using ``make request``.

.. image:: https://raw.githubusercontent.com/crflynn/opentelemetry-sklearn/master/example.png
