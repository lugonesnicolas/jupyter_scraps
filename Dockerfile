FROM quay.io/jupyter/minimal-notebook:notebook-7.2.2
COPY requirements.diff requirements.diff
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.diff --no-cache-dir