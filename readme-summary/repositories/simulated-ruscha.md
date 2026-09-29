# simulated-ruscha

**Creating a Production Build and Deploying with Create React App**

Create React App (CRA) makes it easy to build, test, and deploy your application. Below are the steps to create a production-ready build using `npm run build` and then deploying it on various platforms such as Firebase Hosting, GitHub Pages, Heroku, Modulus, Netlify, Now, S3 with CloudFront, or Surge.

### Step 1: Build Your Application

Run the following command in your project directory:

```bash
npm run build
```

This will compile your React application into a production-ready bundle located in the `build` folder. The output includes optimized and minified JavaScript, CSS, and other assets necessary for deployment.

### Step 2: Deploying to Firebase Hosting

1. **Initialize Firebase (if not already done):**
   ```bash
   firebase init
   ```
   Follow the prompts to select your project and configure Firestore if needed.

2. **Deploy Your Application:**
   ```bash
   firebase deploy
   ```

   This command will:
   - Deploy your build files to Firebase Hosting.
   - Configure the necessary settings such as database rules, hosting configuration, etc.

### Step 3: Deploying to GitHub Pages

1. **Add `homepage` to `package.json`:**
   Open `package.json` and add a `homepage` field:

   ```json
   "homepage": "https://myusername.github.io/my-app",
   ```

2. **Install `gh-pages` and Add Deployment Script:**
   Install the necessary package and script in your `package.json`:

   ```bash
   npm install --save-dev gh-pages

   // In scripts section:
   "scripts": {
     ...
     "deploy": "npm run build && gh-pages -d build"
   }
   ```

3. **Deploy Your Site:**
   Run the deployment script:

   ```bash
   npm run deploy
   ```

4. **Configure GitHub Pages in Project Settings:**
   In your GitHub repository settings, set the source branch to `gh-pages` and ensure the root directory is set to `build`.

### Step 4: Deploying to Heroku

1. **Install Heroku CLI and Create a New App:**
   ```bash
   heroku login
   heroku create
   ```

2. **Deploy Your Application:**
   Push your build files to the Heroku app:

   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   heroku git:remote -a your-app-name
   git push heroku master
   ```

3. **Configure for Client-Side Routing (if needed):**
   Add a `404.html` file in the `build` folder with:

   ```html
   <!DOCTYPE html>
   <html>
     <head><title>Not Found</title></head>
     <body><h1>Page Not Found</h1></body>
   </html>
   ```

### Step 5: Deploying to Modulus

Follow the instructions in [Modulus's blog post](http://blog.modulus.io/deploying-react-apps-on-modulus) for deploying your React app.

### Step 6: Deploying with Netlify

1. **Create a New Netlify Project:**
   - Go to [Netlify](https://app.netlify.com/) and start a new project.
   - Select your Git hosting service (e.g., GitHub, Bitbucket) and choose the repository containing your app.

2. **Configure Continuous Deployment:**
   - Netlify will automatically detect the build command (`npm run build`) and output directory (`build`).

### Step 7: Deploying with Now

1. **Install `now` CLI (if not already installed):**
   ```bash
   npm install -g now
   ```

2. **Deploy Your Application:**
   Run:
   ```bash
   now
   ```
   This will automatically detect the build command and deploy your app to Now's CDN.

### Step 8: Deploying with S3 and CloudFront

1. **Upload Build Files to S3:**
   Use AWS CLI or an S3 client to upload the contents of the `build` folder to an S3 bucket.

2. **Configure CloudFront:**
   - Create a new CloudFront distribution.
   - Set the origin to your S3 bucket and configure the necessary settings (e.g., redirect all requests to `/index.html`).

### Step 9: Deploying with Surge

1. **Install Surge CLI:**
   ```bash
   npm install -g surge
   ```

2. **Deploy Your Application:**
   Run:
   ```bash
   surge build
   ```
   Follow the prompts to select your custom domain or use a default one.

### Troubleshooting Tips

- **`npm test` hangs on macOS Sierra:** This issue is often related to Watchman. Update Watchman to version 4.7.0 or newer, or uninstall and reinstall it.
  
- **`npm run build` silently fails:** Ensure your machine has sufficient swap space, especially in cloud environments.

### Conclusion

By following these steps, you can successfully create a production build of your React application using Create React App and deploy it on various platforms. Each platform may have specific configuration requirements (e.g., GitHub Pages for custom domain setup), so refer to the respective documentation or blog posts linked above for detailed instructions.
