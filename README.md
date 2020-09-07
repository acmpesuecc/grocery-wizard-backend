# Backend Server for Grocery Wizard App

[![Build Status](https://travis-ci.com/acmpesuecc/grocery-wizard-backend.svg?token=nxGkUYMzqzpm6xJdsDWC&branch=master)](https://travis-ci.com/acmpesuecc/grocery-wizard-backend)
[![Build Status](https://dev.azure.com/grocery-wizard/Grocery%20Wizard/_apis/build/status/acmpesuecc.grocery-wizard-backend?branchName=master)](https://dev.azure.com/grocery-wizard/Grocery%20Wizard/_build/latest?definitionId=5&branchName=master)

### Tech
1. FastAPI
2. MongoDB
3. Poetry - For python package management

### Commands
- `poetry add <package name>`
- `poetry shell`
- `uvicorn main:app --reload`
- `poetry run <normal execution command>`
- Development Server: `poetry run uvicorn main:app --reload`
- Production Server: `poetry run uvicorn main:app` or run via Docker
