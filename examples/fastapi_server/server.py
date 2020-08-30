import logging

import fastapi
import numpy as np
from opentelemetry import trace
from opentelemetry.exporter import jaeger
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchExportSpanProcessor
from opentelemetry.sdk.trace.export import ConsoleSpanExporter
from opentelemetry.sdk.trace.export import SimpleExportSpanProcessor
from sklearn.datasets import load_iris

from opentelemetry_sklearn.instrumentation.sklearn import SklearnInstrumentor

from .sklearn_model import sklearn_model

logging.basicConfig(level=logging.DEBUG)


trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    SimpleExportSpanProcessor(ConsoleSpanExporter())
)
jaeger_exporter = jaeger.JaegerSpanExporter(
    service_name="fastapi-sklearn",
    agent_host_name="localhost",
    agent_port=6831,
)
trace.get_tracer_provider().add_span_processor(
    BatchExportSpanProcessor(jaeger_exporter)
)

app = fastapi.FastAPI()

X, y = load_iris(return_X_y=True)

SklearnInstrumentor().instrument_estimator(sklearn_model)


@app.get("/predict")
async def predict():
    rows = X.shape[0]
    random_row = np.random.choice(rows, size=1)
    prediction = sklearn_model.predict(X[random_row, :])
    return prediction.tolist()


FastAPIInstrumentor.instrument_app(app)
