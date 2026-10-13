# Use official Nginx image as base
FROM nginx:alpine

# Set working directory inside container
WORKDIR /usr/share/nginx/html

# Remove default Nginx static files
RUN rm -rf ./*

# Copy your frontend files into Nginx html directory
COPY index.html .
COPY style.css .
COPY script.js .

# Expose port 80 for HTTP traffic
EXPOSE 80

# Nginx will automatically serve files from /usr/share/nginx/html
