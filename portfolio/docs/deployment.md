# Deployment Guide

## Prerequisites

- AWS account with appropriate IAM permissions
- AWS CLI installed and configured (`aws configure`)
- Node.js 18+ and npm
- Python 3.11+

---

## Frontend — AWS S3 + CloudFront

### 1. Build the React app

```bash
cd frontend
npm install
npm run build
# Output: frontend/dist/
```

### 2. Create an S3 bucket

```bash
aws s3 mb s3://cassidy-spencer-portfolio --region us-east-1
```

Enable static website hosting:

```bash
aws s3 website s3://cassidy-spencer-portfolio \
  --index-document index.html \
  --error-document index.html
```

Set bucket policy for public read:

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Sid": "PublicRead",
    "Effect": "Allow",
    "Principal": "*",
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::cassidy-spencer-portfolio/*"
  }]
}
```

### 3. Deploy to S3

```bash
aws s3 sync frontend/dist/ s3://cassidy-spencer-portfolio --delete
```

### 4. Create a CloudFront distribution

In the AWS Console:
- Origin: your S3 bucket website endpoint
- Default root object: `index.html`
- Enable HTTPS (use ACM for a custom domain)
- Add a custom error page: 404 → `/index.html` (for React Router SPA support)

---

## Backend — AWS Elastic Beanstalk

### 1. Install the EB CLI

```bash
pip install awsebcli
```

### 2. Initialize EB

```bash
cd backend
eb init portfolio-api --platform python-3.11 --region us-east-1
```

### 3. Create an environment and deploy

```bash
eb create portfolio-api-env
eb deploy
```

### 4. Update the frontend API URL

Once the EB environment URL is available, update your frontend API calls in
`frontend/src/data/cards.js` or a `.env` file:

```env
VITE_API_URL=https://your-eb-url.elasticbeanstalk.com
```

Rebuild and redeploy the frontend.

---

## Local Development

### Frontend

```bash
cd frontend
npm install
npm run dev
# → http://localhost:5173
```

### Backend

```bash
cd backend
pip install -r requirements.txt
python app.py
# → http://localhost:5000
```
