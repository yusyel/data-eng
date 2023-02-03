FROM prefecthq/prefect:2.7.7-python3.9

COPY req.txt .

RUN pip install -r req.txt --trusted-host pypi.python.org --no-cache-dir

COPY gcp /opt/prefect/flows
COPY gcp/data /opt/prefect/data

