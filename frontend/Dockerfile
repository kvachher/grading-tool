FROM node:14-alpine

WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the code
COPY . .

# Add environment variable for API connection
ENV REACT_APP_API_URL=http://localhost:8000

# Expose port and start the app
EXPOSE 3000
CMD ["npm", "start"]
