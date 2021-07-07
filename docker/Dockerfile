ARG STACTOOLS_VERSION=latest
FROM stacutils/stactools:$STACTOOLS_VERSION

WORKDIR /opt/stactools-ga-nlcd

# For caching purposes, install dependencies but remove the actual package
COPY pyproject.toml setup.cfg ./
COPY src/stactools/ga_nlcd/__init__.py src/stactools/ga_nlcd/
RUN pip install . \
    && rm -r /opt/conda/lib/python3.8/site-packages/stactools/ga_nlcd

COPY src ./src
RUN pip install .
