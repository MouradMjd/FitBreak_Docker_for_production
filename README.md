# FitBreak 🚀

_Turn Your Breaks into Energizing Wellness Moments._

![FitBreak Application Screenshot](img.png)

> **Main Tech Stack:** Python | Flask | React (via CDN) | SQLAlchemy | PostgreSQL | Docker

---

## 📚 Table of Contents

- [Overview](#-overview)
- [Getting Started (with Docker)](#-getting-started-with-docker)
  - [1. Prerequisites](#1-prerequisites)
  - [2. Clone the Repository](#2-clone-the-repository)
  - [3. Environment Setup](#3-environment-setup)
  - [4. Launch the Application](#4-launch-the-application)
  - [5. Verify and Access](#5-verify-and-access)
  - [6. Stack Management](#6-stack-management)

---

## 🧩 Overview

**FitBreak** is a web application designed to seamlessly integrate fitness into daily routines, promoting well-being and productivity in sedentary work or study environments.

This project transforms breaks into revitalizing moments through personalized exercise routines and email reminders. Its core features include:

- **🗃️ Database Management:** Efficient user data handling with SQLAlchemy and PostgreSQL.
- **📧 Email Notifications:** Keeps users informed and engaged with automated communication.
- **⏱️ Background Task Scheduling:** Executes notifications efficiently without blocking the main application, powered by APScheduler.
- **🧭 Dynamic Content:** Smooth navigation and an interactive user interface thanks to React and React Router.

---

## 🚀 Getting Started (with Docker)

This guide explains how to run the entire "FitBreak" application in a containerized environment managed by Docker Compose.

### 1. Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Git:** to clone the repository. ([Download Git](https://git-scm.com/downloads))
- **Docker Desktop:** to run the application. Docker Desktop includes Docker Engine, the Docker CLI, and Docker Compose. ([Download Docker Desktop](https://www.docker.com/products/docker-desktop/))

### 2. Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/MouradMjd/FitBreakDocker.git
```

Once the download is complete, **navigate to the project's root directory**:

```bash
cd BF
```
**Important Note:** All subsequent commands must be run from this root directory, where the `docker-compose.yml` file is located.

### 3. Environment Setup

The application uses a `.env` file to manage database credentials securely, without hardcoding them into configuration files.

**Required Action:** In the project's root directory (`BF/`), create a new file named `.env` and copy the following content into it:

```
# .env file - Credentials for the PostgreSQL database
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=mydatabase
```

### 4. Launch the Application

Once the `.env` file is configured, the entire architecture (web application + database) can be launched with a single command.

```bash
docker compose up --build
```

**What happens during this process:**
- `--build`: This flag instructs Docker Compose to (re)build the image for the `web` service based on the `Dockerfile` in the `BF/` directory. This is necessary on the first launch or after modifying the code.
- Docker will download the required images, create a network and a volume, and start the containers in an orchestrated order to ensure the database is ready before the application starts.

**Note:** The first launch may take a few minutes. Subsequent launches using `docker compose up` will be almost instantaneous.

### 5. Verify and Access

Once the logs in your terminal stabilize, the application is ready.

- **Open your web browser** and navigate to: **[http://localhost:5000](http://localhost:5000)**
- You should see the "FitBreak" application's homepage.
- You can now register a new user or log in with the pre-seeded sample users:
  - **Email:** `marco@gmail.com`, **Password:** `123456`
  - **Email:** `mourad@gmail.com`, **Password:** `123456`

### 6. Stack Management

To stop and remove all containers, networks, and other resources created by Compose, run:

```bash
docker compose down
```

For a complete cleanup that also removes the database volume (useful for a fresh start), use:

```bash
docker compose down --volumes
```






