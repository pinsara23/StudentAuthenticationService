# Use the official Miniconda image so we have Conda installed
FROM continuumio/miniconda3

# Set the working directory inside the container
WORKDIR /app

# Copy the environment file first (for caching purposes)
COPY environment.yml .

# Install dependencies directly into the container's 'base' environment.
# This prevents us from having to run 'conda activate' inside Docker!
RUN conda env update -n base -f environment.yml

# Copy the rest of the application code
COPY . .

# Expose the internal port FastAPI will run on
EXPOSE 8000

# Start Uvicorn bound to 0.0.0.0 (All IP addresses) so it can accept external connections
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]