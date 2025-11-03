FROM node:18

WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install --legacy-peer-deps

# Copy the rest of the code
COPY . .

# Ensure local binaries like react-scripts are on PATH
ENV PATH /app/node_modules/.bin:$PATH

EXPOSE 3000

CMD ["npm", "start"]
