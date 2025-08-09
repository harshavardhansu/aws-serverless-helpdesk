# IT Help Desk Chatbot

A modern, AI-powered IT Help Desk chatbot built with Amazon Lex V2 and deployed as a responsive web application. Features elegant design with Google Poppins font and seamless conversational AI experience.

## 🚀 Live Demo

**Try it now:** [http://my-lex-chatbot-site.s3-website-us-east-1.amazonaws.com](http://my-lex-chatbot-site.s3-website-us-east-1.amazonaws.com)

## ✨ Features

- **Modern UI/UX**: Clean black & white design with Poppins font
- **Real-time Chat**: Instant responses with typing indicators
- **Responsive Design**: Works on desktop and mobile devices
- **Amazon Lex V2**: Advanced natural language processing
- **Serverless Architecture**: Scalable and cost-effective
- **Easy Deployment**: One-click S3 static website hosting

## 🛠️ Tech Stack

- **Frontend**: HTML5, Tailwind CSS, Vanilla JavaScript
- **AI/ML**: Amazon Lex V2 for conversational AI
- **Authentication**: AWS Cognito Identity Pool
- **Hosting**: Amazon S3 Static Website
- **Infrastructure**: AWS CloudFormation/SAM

## 🏗️ Architecture

```
User → S3 Website → AWS Cognito → Amazon Lex V2 → Response
```

## 📁 Project Structure

```
├── frontend/
│   ├── index.html          # Main chatbot interface
│   └── config.js           # AWS configuration
├── templates/
│   └── template.yaml       # CloudFormation template
└── README.md
```

## 🚀 Quick Start

1. **Clone the repository**
2. **Setup environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env with your AWS credentials
   ```
3. **Update config.js** with your actual AWS values
4. **Deploy using SAM**: `sam build && sam deploy`
5. **Upload frontend files** to S3 bucket
6. **Enable static website hosting** on S3

## 🔧 Configuration

### Environment Variables

Create a `.env` file (never commit this!):

```env
AWS_REGION=us-east-1
COGNITO_IDENTITY_POOL_ID=your-identity-pool-id
BOT_ID=your-bot-id
BOT_ALIAS_ID=TSTALIASID
LOCALE_ID=en_IN
```

### Frontend Configuration

Update `frontend/config.js` with your actual values:

```javascript
const BOT_CONFIG = {
  region: "us-east-1",
  identityPoolId: "your-identity-pool-id",
  botId: "your-bot-id",
  botAliasId: "TSTALIASID",
  localeId: "en_IN"
};
```

## 🔒 Security

- Never commit `.env` files to version control
- Use `.env.example` as a template for other developers
- For production, use AWS Parameter Store or Secrets Manager

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📄 License

This project is licensed under the MIT License.