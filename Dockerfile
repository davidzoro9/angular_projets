# Stage 1: Build the Angular application
FROM node:20-alpine AS build
WORKDIR /app

# Copy package descriptors
COPY package*.json ./

# Install dependencies (ignoring scripts for speed and safety)
RUN npm ci --ignore-scripts

# Copy code and build configuration
COPY . .

# Run the build script
RUN npm run build -- --configuration=production

# Stage 2: Serve the application with Nginx
FROM nginx:alpine

# Copy built assets from Stage 1
COPY --from=build /app/dist/angular_projets/browser /usr/share/nginx/html

# Expose container port
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
