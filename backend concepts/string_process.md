Client
  │
  │  HTTP Request
  │  POST /users
  │  {"name": "  Shakil  "}
  ▼
Backend / FastAPI
  │
  ├── 1. Receive string
  │
  ├── 2. Validate
  │      "Shakil" → valid?
  │
  ├── 3. Normalize
  │      "  Shakil  " → "Shakil"
  │
  ├── 4. Process
  │      search / split / replace / parse / transform
  │
  ├── 5. Business logic
  │      compare with existing data
  │
  ├── 6. Database
  │      store/retrieve string
  │
  └── 7. Response
         {"name": "Shakil"}
