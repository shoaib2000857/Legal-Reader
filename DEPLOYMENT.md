# Deployment Guide for Legal Reader

## 🚀 Streamlit Cloud Deployment

### Prerequisites
1. GitHub account with the Legal-Reader repository
2. Google API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

### Step-by-Step Deployment

#### 1. Prepare Repository
Ensure your repository has:
- ✅ `app.py` (main application file)
- ✅ `requirements.txt` (dependencies)
- ✅ `.streamlit/config.toml` (configuration)
- ✅ All source files in `src/` directory

#### 2. Deploy to Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "New app"
3. Connect your GitHub account
4. Select repository: `legal-reader`
5. Set main file path: `app.py`
6. Click "Deploy"

#### 3. Configure Secrets
1. In your Streamlit Cloud app dashboard, click "⚙️ Settings"
2. Go to "Secrets" tab
3. Add your Google API key:
   ```toml
   GOOGLE_API_KEY = "your_actual_api_key_here"
   ```
4. Save the secrets

#### 4. Test Deployment
- Your app will be available at: `https://your-app-name.streamlit.app`
- Test document upload and AI analysis functionality
- Verify all features work correctly

### 🔧 Local Development

#### Setup for Local Testing
```bash
# Clone repository
git clone https://github.com/your-username/legal-reader.git
cd legal-reader

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo "GOOGLE_API_KEY=your_api_key_here" > .env

# Run application
streamlit run app.py
```

### 📝 Environment Variables

#### For Streamlit Cloud
Set in the Streamlit Cloud dashboard under "Secrets":
```toml
GOOGLE_API_KEY = "your_google_api_key"
```

#### For Local Development
Create `.env` file:
```env
GOOGLE_API_KEY=your_google_api_key
```

### 🛠️ Troubleshooting

#### Common Issues

**1. Dependencies Not Installing**
- Check `requirements.txt` for version conflicts
- Ensure all packages are compatible with Python 3.9+

**2. API Key Not Found**
- Verify secrets are set correctly in Streamlit Cloud
- Check for typos in secret key names

**3. Import Errors**
- Verify all source files are in the correct directories
- Check that `src/` directory structure is preserved

**4. Module Not Found Errors**
- Ensure all imports use relative paths
- Check that `sys.path.append()` is working correctly

### 📊 Performance Considerations

#### Streamlit Cloud Limits
- **CPU**: Shared resources, may be slower than local
- **Memory**: Limited RAM available
- **Storage**: No persistent storage between sessions
- **Concurrent Users**: Limited on free tier

#### Optimization Tips
- Use caching with `@st.cache_data` for expensive operations
- Minimize API calls to Google Gemini
- Optimize document processing for larger files

### 🔒 Security Best Practices

#### API Key Management
- ✅ Never commit API keys to repository
- ✅ Use Streamlit secrets for cloud deployment
- ✅ Use `.env` files for local development (add to `.gitignore`)
- ✅ Rotate API keys regularly

#### Data Privacy
- ✅ Documents processed in memory only
- ✅ No persistent storage of user data
- ✅ Sessions are isolated between users

### 📈 Monitoring & Analytics

#### Streamlit Cloud Analytics
- View app usage statistics in dashboard
- Monitor performance and error rates
- Track user engagement metrics

#### Custom Monitoring
- Add logging for important events
- Monitor API usage and costs
- Track document processing success rates

### 🔄 Updates & Maintenance

#### Updating the Application
1. Make changes to your GitHub repository
2. Streamlit Cloud will automatically redeploy
3. Monitor deployment logs for any issues
4. Test functionality after updates

#### Version Control
- Use semantic versioning for releases
- Tag important versions in Git
- Maintain changelog for updates

### 📞 Support & Resources

#### Documentation Links
- [Streamlit Cloud Docs](https://docs.streamlit.io/streamlit-cloud)
- [Google Gemini API](https://ai.google.dev)
- [Streamlit Components](https://docs.streamlit.io)

#### Getting Help
- Check Streamlit Cloud logs for errors
- Review GitHub Issues for known problems
- Test locally to isolate cloud-specific issues

---

**Successfully deployed? 🎉**
Your Legal Reader app should now be live and accessible to users worldwide!
