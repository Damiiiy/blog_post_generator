# blog_post_generator



# AI-Powered Blog Generator API

A powerful, scalable backend service for generating AI-written blog posts using Django Rest Framework and OpenAI's GPT. Users can create and manage blog content by simply entering a topic and desired tone.



## Features
```
- JWT Authentication (Register/Login)
- Blog generation using OpenAI GPT
- Generation history per user
- Export blogs to Markdown, HTML, or PDF
- Usage tracking & quota limits
- Optional Stripe integration for billing
- Async processing with Celery (optional)
```


## Project Structure
```bash
ai_blog_api/
├── bloggen/                # Django project config
│   ├── settings.py
│   ├── urls.py
├── apps/
│   ├── users/              # Auth and user management
│   ├── generator/          # Blog generation logic
│   ├── billing/            # Stripe billing (optional)
├── core/                   # Shared utilities, tasks, etc.
├── manage.py
├── requirements.txt
├── .env
└── README.md
```


<!-- ``` -->

## Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-blog-generator-api.git
cd ai-blog-generator-api
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory and add:

```bash
DEBUG=True
SECRET_KEY=your_django_secret_key
OPENAI_API_KEY=your_openai_api_key
STRIPE_SECRET_KEY=your_stripe_key  # Optional
DATABASE_URL=sqlite:///db.sqlite3

```

### 5. Apply Migrations
```bash
python manage.py migrate
```

### 6. Run the Development Server
```bash
python manage.py runserver
```



## API Endpoints

| Endpoint                         | Method | Description                      |
|----------------------------------|--------|----------------------------------|
| `/api/auth/register/`           | POST   | Register a new user              |
| `/api/auth/login/`              | POST   | Get JWT token                    |
| `/api/generate/`                | POST   | Generate a blog post             |
| `/api/posts/`                   | GET    | List user's generated blogs      |
| `/api/posts/{id}/`              | GET    | Retrieve a specific blog         |
| `/api/posts/{id}/download/`     | GET    | Export blog (HTML, MD, PDF)      |
| `/api/usage/`                   | GET    | Track user usage/quota           |
| `/api/stripe/webhook/`          | POST   | Stripe payment webhook (optional)|


---

## Tech Stack

- **Backend:** Django + DRF
- **AI:** OpenAI GPT API
- **Auth:** JWT (via `djangorestframework-simplejwt`)
- **Payments (optional):** Stripe API
- **Async Tasks (optional):** Celery + Redis
- **Database:** PostgreSQL or SQLite (dev)

---

## Example Generation Request

**POST** `/api/generate/`

```json
{
  "topic": "How to Stay Productive as a Remote Developer",
  "tone": "Conversational",
  "length": "Medium",
  "keywords": ["productivity", "remote work", "tips"]
}

```

---

## Run Tests

```bash
python manage.py test
```

---

## Development Tips

- Use `drf-yasg` or `drf-spectacular` to auto-generate Swagger docs
- Secure API keys and secret settings using `python-decouple` or `django-environ`
- Create a reusable `services.py` for AI interactions
- Use pagination for listing posts

---

## License

This project is licensed under the **MIT License**.

---

## Contributing

Got a cool idea or found a bug? PRs and Issues are welcome!

---

## Author

Built by **Ndifreke Umoh Macauley**  
GitHub: [github.com/damiiiy](https://github.com/damiiiy)  
Twitter: [@damiiiy1](https://x.com/damiiiy1)






