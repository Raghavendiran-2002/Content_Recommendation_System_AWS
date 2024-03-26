# Use an official Node runtime as the base image
FROM node:14-alpine as build-stage

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy all files from the current directory to the working directory in the container
COPY . .

# Build the React app for production
RUN npm run build

# Stage 2: Serve the production-ready application with Nginx
FROM nginx:alpine

# Copy the build output from the build stage to the nginx html directory
COPY --from=build-stage /app/build /usr/share/nginx/html

# Expose port 80 to the outside world
EXPOSE 80

# Start Nginx server when the container starts
CMD ["nginx", "-g", "daemon off;"]