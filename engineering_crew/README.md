# 🚀 EngineeringCrew - CrewAI Project

This project defines a structured AI-powered software engineering team using **CrewAI**, a framework for building autonomous multi-agent workflows.

---

## 📌 Purpose

The goal of this project is to simulate an **AI-based software engineering crew** that can collaboratively:

- 🧠 Design
- 💻 Develop (Backend & Frontend)
- 🧪 Test  

software solutions autonomously and safely.

---

## 🛠️ Tools & Technologies Used

- **CrewAI**: Multi-agent orchestration framework
- **Python**: Core implementation language
- **YAML**: For agent and task configuration
- **Docker-safe Code Execution**: Enables secure agent code execution
- **Type Hints**: For better structure and clarity in Python

---

## 👥 Agents

Each agent performs a specific role in the software engineering process:

- **👨‍💼 Engineering Lead**
  - Oversees and coordinates all engineering activities

- **🛠 Backend Engineer**
  - Writes and executes backend code
  - Supports safe code execution via Docker

- **🎨 Frontend Engineer**
  - Handles UI development and client-side tasks

- **🧪 Test Engineer**
  - Executes test cases and validates outputs
  - Also runs code safely in Docker

---

## ✅ Tasks

Defined in `config/tasks.yaml` and assigned to appropriate agents:

- `design_task`: Defines the system architecture or plan
- `code_task`: Backend development work
- `frontend_task`: UI component creation
- `test_task`: Software testing and validation

---

## 🔁 Process Flow

- **Sequential Task Execution** using `Process.sequential`
  - Tasks run one after the other
  - Ensures clean transitions between roles

---

