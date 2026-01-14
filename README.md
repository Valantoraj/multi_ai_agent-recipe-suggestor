# Multi-Agent Food Advisor

A sophisticated multi-agent system that provides personalized food recommendations and recipe generation based on user preferences, dietary restrictions, and meal context.

## Overview

This project implements a coordinated multi-agent architecture where specialized agents work together to deliver intelligent food recommendations and recipes. The system analyzes user preferences, meal context, and cuisine preferences to generate tailored suggestions.

## Architecture

The system consists of the following specialized agents:

### Coordinating Agent
- **Location**: `coordinating_agent/`
- **Purpose**: Orchestrates the workflow between all agents
- **Responsibilities**: Manages agent coordination and flow control

### Context Agent
- **Location**: `context_agent/`
- **Purpose**: Analyzes the user's meal context
- **Responsibilities**: Determines time of day, occasion, and situational factors

### Preference Agent
- **Location**: `preference_agent/`
- **Purpose**: Manages user dietary preferences and restrictions
- **Responsibilities**: Handles allergies, dietary restrictions, and food preferences

### Meal Type Agent
- **Location**: `meal_type_agent/`
- **Purpose**: Determines appropriate meal types
- **Responsibilities**: Suggests breakfast, lunch, dinner, or snack options

### Cuisine Mapping Agent
- **Location**: `cuisine_mapping_agent/`
- **Purpose**: Maps user preferences to cuisine types
- **Responsibilities**: Identifies suitable cuisines (Italian, Asian, Mexican, etc.)

### Dish Selection Agent
- **Location**: `dish_selection_agent/`
- **Purpose**: Selects specific dishes based on all gathered information
- **Responsibilities**: Recommends specific dishes matching all criteria

### Recipe Generation Agent
- **Location**: `recipe_generation_agent/`
- **Purpose**: Generates detailed recipes
- **Responsibilities**: Provides ingredients, instructions, and cooking tips

## Project Structure

```
multi_ai_agent/
├── main.py                      # Entry point
├── README.md                    # This file
├── coordinating_agent/          # Workflow orchestration
├── context_agent/               # Context analysis
├── preference_agent/            # Preference management
├── meal_type_agent/             # Meal type determination
├── cuisine_mapping_agent/       # Cuisine selection
├── dish_selection_agent/        # Dish recommendation
├── recipe_generation_agent/     # Recipe generation
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Required dependencies (see requirements.txt)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd multi_ai_agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

Run the main application:
```bash
adk web
```

## How It Works

1. **Context Analysis**: The system first analyzes the current context (time, occasion)
2. **Preference Gathering**: Collects user dietary preferences and restrictions
3. **Meal Type Selection**: Determines appropriate meal type based on context
4. **Cuisine Mapping**: Identifies suitable cuisines matching preferences
5. **Dish Selection**: Recommends specific dishes
6. **Recipe Generation**: Provides detailed cooking instructions

## Features

- ✅ Personalized food recommendations
- ✅ Dietary restriction handling
- ✅ Context-aware suggestions
- ✅ Multi-cuisine support
- ✅ Detailed recipe generation
- ✅ Modular agent architecture

## Agent Communication

Agents communicate through a coordinated workflow managed by the coordinating agent. Each agent specializes in a specific domain and contributes to the final recommendation.

## Acknowledgments

Built with a multi-agent architecture for intelligent food recommendations.
