import pandas as pd

# Load the dataset
df = pd.read_csv("amazon_reviews.csv")  # update this if the file name is different

# Show first 5 rows
print(df.head())
import logging

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a file handler and stream handler
file_handler = logging.FileHandler('amazon_reviews.log')
stream_handler = logging.StreamHandler()

# Create a formatter and set it for the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# Load the dataset
logger.info('Loading the dataset...')
df = pd.read_csv("amazon_reviews.csv")  # update this if the file name is different
logger.info('Dataset loaded successfully.')

# Show first 5 rows
logger.info('Showing first 5 rows...')
print(df.head())
logger.info('First 5 rows shown successfully.')