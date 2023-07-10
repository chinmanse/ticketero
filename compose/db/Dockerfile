FROM postgres:15.2

ENV LANG=en_US.utf8 \
    TZ=UTC

# Install additional packages
RUN apt-get update
RUN apt-get install -y \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy and execute SQL scripts
# COPY init.sql /docker-entrypoint-initdb.d/

# Set timezone
RUN echo "UTC" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata

WORKDIR /home/dbs
