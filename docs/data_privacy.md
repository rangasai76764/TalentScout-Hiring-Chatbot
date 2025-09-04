# Data Privacy & Handling

This demo saves candidate data in `candidate_data.json` (local, not committed). Guidelines:

- **Do not** commit `.env` or files with production API keys.
- For production:
  - Store sensitive data in an encrypted database.
  - Use field-level encryption (e.g., AES-GCM or cloud-provider KMS).
  - Limit access via IAM/ACLs and log all access.
  - Provide a data retention policy and deletion mechanism.
  - Ensure compliance with GDPR / local laws when handling PII.

This project includes `.gitignore` to prevent accidental commits of `candidate_data.json`.
