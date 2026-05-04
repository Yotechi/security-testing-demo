# Python Security Pipeline Demo

This is a demonstration Python project with intentional security vulnerabilities to showcase GitHub Actions security testing.

## ⚠️ WARNING

**This project contains intentional security vulnerabilities for educational purposes only!**
- SQL Injection
- Command Injection
- Hardcoded Credentials
- Unsafe Deserialization
- Template Injection
- Debug Mode in Production

## Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app (DO NOT in production)
python app.py
```

## Security Testing

The project includes a GitHub Actions workflow that runs:
- **Safety** - Checks for vulnerable Python packages
- **Bandit** - Scans code for security issues
- **TruffleHog** - Detects hardcoded secrets

View results in the Security tab of your GitHub repository.

## Learning Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Bandit Documentation](https://bandit.readthedocs.io/)
- [Safety Documentation](https://safety.readthedocs.io/)
