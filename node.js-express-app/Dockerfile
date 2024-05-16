# Base Image
FROM node:current-alpine3.19

# Setting the Work Directory
WORKDIR /app

# Copying the package.json file
COPY package*.json ./

# Install Dependencies
RUN npm install

# Copy the rest of the application code
COPY . /app/

# Expose Port
EXPOSE 3000

# Run app.js when the container launches
CMD ["node", "app.js"]