FROM python:3.12-slim

WORKDIR /app
COPY . .

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    aria2 \
    unzip \
    wget \
    git \
    cmake \
    build-essential \
    libopenjp2-7 \
    libopenjp2-7-dev \
    libjpeg-dev \
    zlib1g-dev \
    libtiff-dev \
    libxml2-dev \
    libxslt-dev \
    && rm -rf /var/lib/apt/lists/*

# Install mp4decrypt (Bento4)
RUN wget -q https://github.com/axiomatic-systems/Bento4/archive/v1.6.0-639.zip && \
    unzip v1.6.0-639.zip && \
    cd Bento4-1.6.0-639 && \
    mkdir build && cd build && \
    cmake .. && \
    make -j$(nproc) && \
    cp mp4decrypt /usr/local/bin/ && \
    cd ../.. && rm -rf Bento4-1.6.0-639 v1.6.0-639.zip

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r sainibots.txt && \
    python3 -m pip install -U yt-dlp

CMD ["sh", "-c", "gunicorn app:app & python3 main.py"]
