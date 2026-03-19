Product Requirements Document (PRD)
Project Name
Personal Portfolio – Card Table Interface

1. Overview
This project is a single-page personal portfolio website designed as a table of playing cards. Each card represents a part of my professional experience, technical interests, projects, or personal life.
The interface allows visitors to explore my portfolio by interacting with cards that:
flip when clicked
expand to reveal detailed information
visually organize my experience into themed categories ("hands")
The goal is to create a memorable, interactive portfolio that demonstrates:
frontend engineering skills
backend API design
cloud deployment
thoughtful UI design
personality and interests
The visual theme uses a natural color palette inspired by playing cards, combined with a dark wooden table background.

2. Goals
Primary Goals
Showcase my professional experience and technical projects
Demonstrate full-stack engineering skills
Build a unique, memorable portfolio experience
Deploy the application using cloud infrastructure
Maintain a well-structured, documented GitHub repository
Secondary Goals
Demonstrate UI/UX design thinking
Present my engineering philosophy
Include personal interests and hobbies
Build a platform that can support future AI features

3. Target Audience
Primary Users
engineering hiring managers
technical recruiters
software engineers
Secondary Users
friends and collaborators
general visitors interested in my work

4. Core Concept
The portfolio appears as a table of cards laid out in four hands. Each hand represents a category of content.
Cards resemble green playing cards and use suit icons for visual organization.
When the page first loads, the cards appear face down, showing a decorative green card back pattern.
When a card category is clicked:
The cards flip to reveal the front side
The cards expands toward the center of the screen 
The rest of the page becomes slightly blurred and darkened
The front of the cards display detailed information
This interaction mimics physically picking up a hand from a table and turning it over.

5. Visual Design
Color Palette
Color
Purpose
Dark Natural Brown
wooden table background
Emerald Green
primary card color
Sage Green
secondary accents
Cream
text background or content sections
Gold
borders, suit icons, decorative accents

Example palette:
#3E2A1F – dark wood brown
#0F3D2E – emerald green
#8FAF9A – sage green
#F5F1E8 – cream
#C9A94D – gold

Background Design
The page background resembles a dark natural wooden table surface.
Design characteristics:
subtle wood grain texture
deep brown tones
soft lighting to create depth
Cards appear slightly raised above the surface with soft shadows to simulate cards placed on a table.
Cards are grouped in four hands, each hand creates a slight arc, as if they would be if someone was fanning out the cards. 

Card Appearance
Cards resemble custom playing cards with a green theme.
Card Back (default state)
Cards start face down.
The back design includes:
Cream colored background
Emerald green and sage green decorative pattern
gold accents
This resembles the back of a traditional deck of cards. The back of the card displays the title of the card over the decorative back.

Card Front (revealed when flipped)
The front of the card displays content with:
emerald green and sage green design elements
gold accents and borders
cream sections for readable text
Cards include small suit icons in the corners, similar to real playing cards.
Cards are rectangular with slightly rounded edges.

6. Page Layout
The homepage is organized into four hands, representing different aspects of my life and work.
Each hand corresponds to a suit.

Work (♠)
Cards:
PNC Software Engineer
CGI Software Developer
CGI Internships
Computer Science Tutor and lab assistant 

Personal (♥)
Cards:
Passions
Hobbies
Cats
Volunteer Work

Tech (♦)
Cards:
Languages and Tech Stack
Coding Style
Why I Code

Projects (♣)
Cards:
Portfolio Website
Cost of Living Project

7. Card Interaction Design
Default State
Cards appear face down showing the card back design.
Cards are arranged in hands (light arc) under each hand heading.

Hover Behavior
When hovering over a card hand or tabbing to a hand:
the cards lift slightly
shadow increases
subtle scale animation
This creates a feeling that the cards can be picked up.

Click Behavior
When a card hand is clicked (or users can tab and press enter on a hand):
The hand rotates on the Y-axis (flip animation)
The cards expand toward the center of the screen
Background become blurred and dimmed
The front of the cards display detailed information
The expanded cards occupies roughly 70-80% of the screen width. Proportion of the hand stays exactly the same.

Closing a Card
Users can close the cards by:
clicking a close icon
clicking outside the card
pressing the escape key
The card then shrinks and flips back to its original position.

8. Animations
Page Load Animation
When the site first loads:
Cards animate onto the screen like a shuffled deck.
Cards slide or scatter into position to simulate a shuffle.

Fan-Out Animation
Cards within a hand slightly fan out horizontally, creating the visual effect of a hand of cards being held.

Hover Animation
Cards lift upward slightly with:
subtle scale increase
shadow expansion

Flip Animation
Cards flip using a 3D rotation effect.
The flip reveals the front side containing the card details.

9. Card Content Structure
The front side of each card contains structured information.
Example structure for experience cards:
Title
Company / Role
Dates
Key Contributions
accomplishment 1
accomplishment 2
accomplishment 3
Technologies Used
Python
React
APIs
SQL

Special Cards
Cats Card
Displays a short description and opens a gallery of cat photos.

Projects Cards
Include:
project overview
technologies used
link to live site
link to GitHub repository

10. Technical Architecture
Frontend
Built with:
React
Vite
Responsibilities:
card rendering
animations
layout
user interaction
API requests

Backend
API built with:
Flask
Responsibilities:
serve card content
provide project data
support future features
Example endpoints:
GET /cards
GET /cards/{id}

11. Cloud Infrastructure
Deployment will use Amazon Web Services (AWS).
Frontend Hosting
React application deployed to:
AWS S3 (static hosting)
Content distributed through:
CloudFront CDN

Backend Hosting
Flask API hosted on:
AWS Elastic Beanstalk
Benefits:
simple deployment
automatic scaling
minimal infrastructure configuration

Architecture Flow
User Browser
↓
CloudFront CDN
↓
S3 (React frontend)
↓
Flask API (Elastic Beanstalk)

12. GitHub Repository
Repository will include:
frontend/
backend/
docs/
Documentation will include:
PRD
architecture overview
setup instructions
deployment guide

13. MVP Scope
Version 1 will include:
single homepage
four card hands
cards starting face down
card flip animation
card expansion modal
wooden table background
shuffle load animation
hover animation
basic Flask API
AWS deployment

14. Future Enhancements
Potential future features include:
AI assistant for exploring the portfolio
blog posts
interactive architecture diagrams
GitHub activity visualization
project deep dives

15. Success Criteria
The portfolio is successful if:
visitors quickly understand my experience
the design is memorable
the site demonstrates full-stack engineering ability
recruiters can easily explore projects and skills
the codebase is clean and well-documented