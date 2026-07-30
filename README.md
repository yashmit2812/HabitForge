# HabitForge - Vision Document

## Project Name & Overview
**HabitForge** is a gamified productivity and habit-tracking web application. It transforms daily self-improvement into an RPG-style game where users build daily streaks to level up, and lose "Health Points" (HP) if they neglect their commitments. 

## Problem it Solves
Traditional habit trackers are often clinical, boring, and fail to provide immediate dopamine or consequences. Students and young professionals often struggle with procrastination and lack the short-term motivation required to build long-term routines. HabitForge solves this by introducing immediate virtual stakes (HP) and rewards.

## Target Users (Personas)
1. **The Procrastinator (Standard User):** Needs external motivation and a sense of urgency (losing HP) to complete daily tasks like studying or exercising.
2. **The Data Achiever (Power User):** Loves seeing their progress visualized through streak counters and historical charts to validate their consistency.

## Vision Statement
To make personal growth as engaging and addictive as a video game by applying RPG mechanics to daily real-world habits.

## Key Features / Goals
* **The Daily Quest Board:** A daily checklist of active habits.
* **Health & Experience System:** Gain XP for completing habits; lose HP when failing to complete them by midnight.
* **Streak Tracking:** Visual counters showing consecutive days of success.
* **Custom Rewards:** A "shop" where users spend earned points on real-world rewards they set for themselves (e.g., "1 Hour of Gaming").
* **Progress Analytics:** Simple charts showing completion rates over time.

## Success Metrics
* **Retention:** 40% of users return to log a habit on Day 7.
* **Engagement:** Users interact with the app at least twice a day (morning review, evening check-off).
* **System Health:** 0 missed midnight cron jobs for HP deduction.

## Assumptions & Constraints
* **Assumptions:** Users will be honest when checking off habits; users understand basic RPG terminology (HP, XP).
* **Constraints:** Must be built as a responsive web app rather than a native mobile app for V1; relying on a simple server-side cron job for daily resets.

---

## Development Setup

### Branching Strategy
This project strictly follows **GitHub Flow**:
1. The `main` branch is always deployable and stable.
2. All new development happens on descriptive feature branches (e.g., `feature/hp-system`, `feature/auth-ui`).
3. Once work is complete, a Pull Request (PR) is opened against `main` for review.
4. After approval, the branch is merged into `main` and deleted.

### Local Development Tools
* **Code Editor:** Visual Studio Code
* **Version Control:** Git & GitHub
* **Containerization:** Docker Desktop
* **API Testing:** Postman / REST Client

### Quick Start – Local Development
Ensure you have [Docker Desktop](https://www.docker.com/products/docker-desktop) installed and running.

1. Clone the repository:
   `git clone https://github.com/yourusername/habitforge.git`
2. Navigate into the project directory:
   `cd habitforge`
3. Build the Docker images and start the containers:
   `docker-compose up --build`
4. Access the application:
   * **Frontend Application:** `http://localhost:3000`
   * **Backend API (Spring Boot):** `http://localhost:8080`